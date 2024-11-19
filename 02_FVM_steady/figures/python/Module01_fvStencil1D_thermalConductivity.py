# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


fig, ax = plt.subplots(figsize=(6, 4))

# y-coord for plotitng
yPoint = 0

# plot horizontal line (x-axis)
ax.axhline(yPoint, ls='-', color='k', alpha=0.25)

# plot nodes on the FV grid
cNodes = [0, 1]
cLabels = ['P', 'E']
for xPoint, label in zip(cNodes, cLabels):
    ax.plot(xPoint, yPoint, ls='', marker='o', color='k', markerfacecolor='w')
    ax.annotate(label, xy=(xPoint, yPoint-0.008), ha='center', va='bottom')


# Plot distances between nodes P, E
for xPoint in cNodes:
    ax.plot([xPoint, xPoint], [0.01, 0.04], ls='-', color='k')
arrPE = mpatches.FancyArrowPatch((0, 0.025), (1, 0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrPE)
ax.annotate(r"$(\delta x)_e$", xy=(0.5, 0.03), ha='center', va='bottom')


# plot positions of surfaces between FV cells
aNodes = [0.5]
aLabels = ['e']
for xPoint, label in zip(aNodes, aLabels):
    ax.plot(xPoint, yPoint, ls='', marker='.', color='k')
    ax.annotate(label, xy=(xPoint, yPoint-0.006), ha='left', va='bottom')

# plot surfaces between FV cells
for xPoint in aNodes:
    ax.plot([xPoint, xPoint], [-0.02, 0.02], ls='--', color='red')
arrAe = mpatches.FancyArrowPatch((0.5, 0), (0.75, 0), color='red',
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrAe)
ax.annotate(r"$A_e$", xy=(0.6, 0.005), ha='center', va='center', color='red')


# thermal conductivities
ax.annotate(r"$\lambda_e$", xy=(0.5, -0.035), weight='bold', size=15,
            ha='center', va='center', color='C0')
ax.annotate(r"$\lambda_P$", xy=(0, -0.045), weight='bold', size=15,
            ha='center', va='center', color='b')
ax.annotate(r"$\lambda_E$", xy=(1, -0.045), weight='bold', size=15,
            ha='center', va='center', color='b')

# Plot distances between nodes P:e  and between nodes e:E
for xPoint in cNodes:
    ax.plot([xPoint, xPoint], [-0.01, -0.04], ls='-', color='k')
for xPoint in aNodes:
    ax.plot([xPoint, xPoint], [-0.02, -0.03], ls='-', color='k')

arrPe = mpatches.FancyArrowPatch((0, -0.025), (0.5, -0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrPe)
ax.annotate(r"$(\delta x)_{e-}$", xy=(0.25, -0.035), ha='center', va='bottom')

arreE = mpatches.FancyArrowPatch((0.5, -0.025), (1, -0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arreE)
ax.annotate(r"$(\delta x)_{e+}$", xy=(0.75, -0.035), ha='center', va='bottom')


# finishing touches
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.05, 0.05)
ax.set_axis_off()


