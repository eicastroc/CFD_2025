using LinearAlgebra


"""
Método iterativo para resolver mediante un algoritmo de 
pseudo-avance de tiempo el sistema de ecuaciones que describe 
conducción de calor 1D con un término fuente en régimen estacionario. 

El algoritmo se detiene cuando la diferencia de temperaturas 
entre dos iteraciones es menor a la tolerancia especificada, 
o cuando se alcanza el numero de iteraciones máximas especificadas.
"""
function heatStationary(X, nCells, Told, λ, htc, TfarW, TfarE, niters, tol=1e-16)

	# Valores iniciales para el metodo numerico
	Tnew = copy(Told)
	error = ones(Float64, niters)
	
	# Metodo iterativo
	for i=1:niters
		# Construccion del sistema de ecuaciones
		A = constructLHS_stat(X, nCells, Told, λ, htc)
		b = constructRHS_stat(X, nCells, Told, λ, htc, TfarW, TfarE)
		# Resolucion del sistema
		Tnew = A\b
		# Estimacion del error numerico
		err = abs(maximum(@. (Tnew - Told) / Told))
		error[i] = err
		# Actualizacion de los valores de temperatura iterados
		Told = copy(Tnew)
        # Parar el cálculo en caso que se haya logrado convergencia
		if err <= tol
			if err < 1e-16
				error[i] = 1e-16 # para poder graficar
			end
			error = first(error, i)
			print("El problema ha convergido tras ", i, " iteraciones")
			break
		end
	end

	return Tnew, error

end


"""
Función para calcular la parte constante, Sc, 
de la ecuación de un término fuente linealizado, 
de la forma: S = Sc + Sp * T
"""
function Sc_(T)
	return @. 4e7 + 150 * (T^2 - 273.15^2)
end


"""
Función para calcular la pendiente, Sp, 
de la ecuación de un término fuente linealizado, 
de la forma: S = Sc + Sp * T
"""
function Sp_(T)
	return @. -300 * (T - 273.15)
end


"""
Construcción de la matriz de coeficientes [A], al lado izquierdo 
del sistema de ecuaciones para régimen estacionario.
"""
function constructLHS_stat(X, nCells, Told, λ, htc)

	# Discretizacion espacial
	Δx = X/nCells 	# [m]
	A = 1.0 		# [m2]
	ΔV = Δx * A 	# [m3]

	# Coeficientes aE, aW:
	aE = λ * A / Δx
	aW= λ * A / Δx

	# Resistencia a las fronteras por conveccion + difusion
	Rth = (htc * (λ/(Δx/2))) / (htc + (λ/(Δx/2))) 

	
	# diagonal inferior de la matriz A (coeficientes aW)
	dl = @. -aW * ones(Float64, nCells-1)
	# diagonal superior de la matriz A (coeficientes aE)
	du = @. -aE * ones(Float64, nCells-1)
	# diagonal de la matriz A (coeficientes aP)
	d = zeros(Float64, nCells)
	d[1] = aE + Rth * A - Sp_(Told[1]) * ΔV
	for i=2:nCells-1
		d[i] = aE + aW - Sp_(Told[i]) * ΔV
	end
	d[nCells] = aW + Rth * A - Sp_(Told[nCells]) * ΔV

	# Regresar una matriz tridiagonal
	return Tridiagonal(dl, d, du)
end



"""
Construcción del vector constante [b], al lado derecho 
del sistema de ecuaciones en régimen estacionario.
"""
function constructRHS_stat(X, nCells, Told, λ, htc, Tw, Te)

	# Discretizacion espacial
	Δx = X/nCells 	# [m]
	A = 1 			# [m2]
	ΔV = Δx * A 	# [m3]
	
	# Resistencia a las fronteras por conveccion + difusion
	Rth = (htc * (λ/(Δx/2))) / (htc + (λ/(Δx/2))) 

	# Construccion de vector b
	RHS = zeros(Float64, nCells)
	RHS[1] = Rth*A*Tw + Sc_(Told[1]) * ΔV
	for i=2:nCells-1
		RHS[i] = Sc_(Told[i]) * ΔV
	end
	RHS[nCells] = Rth*A*Te + Sc_(Told[nCells]) * ΔV

	return Vector(RHS)
end


"""
Calculo de la temperatura en la frontera para una 
condición a la frontera tipo Cauchy, 
mediante un método de resistencias térmicas equivalentes.
"""
function tempBound(X, nCells, λ, htc, Tinf, Tcell)

	# Discretizacion espacial
	Δx = X/nCells 	# [m]

	# Resistencias termicas
	rConv = htc  		# W/(m2 K)
	rDiff = λ / (Δx/2) 	# W/(m2 K)
	
	return (rConv*Tinf + rDiff*Tcell) / (rConv + rDiff)
end


"""
Balance de energía para el régimen estacionario, en [W]:

		Acumulación = Entradas - Salidas + Generación = 0
"""
function stationaryHeatBalance(X, nCells, λ, T, Twest, Teast)

	# Discretizacion espacial
	Δx = X/nCells 	# [m]
	A = 1 			# [m2]
	ΔV = Δx * A 	# [m3]

	# Flujo en la frontera oeste
	ϕ_w = λ/(Δx/2) * A * (Twest - T[begin])
	# Flujo en la frontera este
	ϕ_e = λ/(Δx/2) * A * (Teast - T[end])
	# Generacion
	Gen = sum(@. ΔV * (Sc_(T) + Sp_(T) * T))

	return ϕ_w, ϕ_e, Gen
end


"""
Conversión de unidades de temperatura de Celcius a Kelvin.
"""
function CtoK(T)
	# convert temperature: Celcius to Kelvin
	return @. T + 273.15
end


"""
Conversión de unidades de temperatura de Kelvin a Celcius
"""
function KtoC(T)
	# convert temperature: Kelvin to Celcius
	return @. T - 273.15
end


println("heatSteady.jl has been imported")