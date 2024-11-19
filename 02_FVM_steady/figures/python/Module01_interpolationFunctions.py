# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 


import matplotlib.pyplot as plt



fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 4))

# y-coord for plotitng
yPoint = 0
cNodes = [-1, 0, 1]
Temps = [10, 20, 25]
Tlabels = [r'$T_W$', r'$T_P$', r'$T_E$']

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
    cLabels = ['W', 'P', 'E']
    for xPoint, label in zip(cNodes, cLabels):
        ax.plot(xPoint, yPoint, ls='', marker='o', 
                color='k', markerfacecolor='w')
        ax.annotate(label, xy=(xPoint, yPoint-3), ha='center', va='bottom')

    # plot positions of surfaces between FV cells
    aNodes = [-0.5, 0.5]
    aLabels = ['w', 'e']
    for xPoint, label in zip(aNodes, aLabels):
        ax.plot(xPoint, yPoint, ls='', marker='.', color='k')
        ax.annotate(label, xy=(xPoint, yPoint-3), ha='center', va='bottom')

    # plot surfaces between FV cells
    aLabels=['Aw', 'Ae']
    for xPoint, label in zip(aNodes, aLabels):
        ax.axvline(xPoint, ls='--', color='red', alpha=0.5)
        ax.annotate(label, xy=(xPoint, yPoint+5), 
                    ha='right', va='top', color='red', alpha=0.5)

# Plotting of constant profile
ax = axes[0]
ax.set_title('Constante por segmentos')
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$T$")
for xPoint, Temp in zip(cNodes, Temps):
    ax.plot([xPoint-0.5, xPoint+0.5], [Temp, Temp], color='C0')

# Plotting of linear profile
ax = axes[1]
ax.set_title('Lineal por segmentos')
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$T$")
ax.plot(cNodes, Temps, color='C0')

# finishing touches
for ax in axes:
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-5, 35)
    ax.set_xticks([])
    ax.set_yticks([])


