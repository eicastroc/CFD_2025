# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 4))

# y-coord for plotitng
yPoint = 0
cNodes = [-1, 0, 1, 2]
cLabels = ['W', 'P', 'E', 'EE']
Temps = [20, 8, 12, 22]
Tlabels = [r'$T_W$', r'$T_P$', r'$T_E$', r'$T_{EE}$']

# Plotting shared between the two axes
for ax in axes:
    # plot horizontal line (x-axis)
    ax.axhline(0, ls='-', color='k')

    # Plot the discrete temperatures at fv nodes
    ax.stem(cNodes, Temps, linefmt='b-', markerfmt='b')
    for xPoint, Temp, label in zip(cNodes, Temps, Tlabels):
        ax.annotate(label, xy=(xPoint, Temp+4), 
                    ha='center', va='top', color='blue')
    
    # plot nodes on the FV grid
    for xPoint, label in zip(cNodes, cLabels):
        ax.plot(xPoint, yPoint, ls='', marker='o', 
                color='k', markerfacecolor='w')
        ax.annotate(label, xy=(xPoint, yPoint-3), ha='center', va='bottom')

    # plot positions of surfaces between FV cells
    aNodes = [0.5]
    aLabels = ['e']
    for xPoint, label in zip(aNodes, aLabels):
        ax.plot(xPoint, yPoint, ls='', marker='.', color='k')
        ax.annotate(label, xy=(xPoint, yPoint-3), ha='center', va='bottom')

    # plot surfaces between FV cells
    aLabels=['Ae']
    for xPoint, label in zip(aNodes, aLabels):
        ax.axvline(xPoint, ls='--', color='red', alpha=0.5)
        ax.annotate(label, xy=(xPoint, yPoint+5), 
                    ha='right', va='top', color='red', alpha=0.5)


### Plotting of linear profile
ax = axes[0]
ax.set_title('Perfil lineal')
ax.plot(cNodes[1:3], Temps[1:3], ls='-', color='C0')
ax.plot(cNodes[1:3], Temps[1:3], ls='--', color='C1')

#### Plotting of quadratic profile
ax = axes[1]
ax.set_title('Perfil cuadratico')
# Quadratic profile on P, calculated from W, P, E
prof_WPE = np.polynomial.Polynomial.fit(cNodes[:3], Temps[:3], deg=2)
xCoords = np.linspace(-1, 1, 50)
yCoords = prof_WPE(xCoords)
ax.plot(xCoords, yCoords)
# Quadratic profile on E, calculated from P, E, EE
prof_WPE = np.polynomial.Polynomial.fit(cNodes[1:], Temps[1:], deg=2)
xCoords = np.linspace(0, 2, 50)
yCoords = prof_WPE(xCoords)
ax.plot(xCoords, yCoords)


# finishing touches
for ax in axes:
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$T$")
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(-5, 35)
    ax.set_xticks([])
    ax.set_yticks([])


