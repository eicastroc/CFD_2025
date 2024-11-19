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
ax.axhline(0, ls='-', color='k', alpha=0.25)

# plot nodes on the FV grid
cNodes = [0, 1]
cLabels = ['P', 'E']
for xPoint, label in zip(cNodes, cLabels):
    ax.plot(xPoint, yPoint, ls='', marker='o', color='k', markerfacecolor='w')
    ax.annotate(label, xy=(xPoint, yPoint-0.01), ha='center', va='bottom')

# Plot distances between nodes
ax.plot([-0.5, -0.5], [0.01, 0.04], ls='-', color='k')
for xPoint in cNodes:
    ax.plot([xPoint, xPoint], [0.01, 0.04], ls='-', color='k')
arrWP = mpatches.FancyArrowPatch((-0.5, 0.025), (0, 0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
arrPE = mpatches.FancyArrowPatch((0, 0.025), (1, 0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrWP)
ax.add_patch(arrPE)
ax.annotate(r"$(\delta x)_b$", xy=(-0.25, 0.03), ha='center', va='bottom')
ax.annotate(r"$(\delta x)_e$", xy=(0.5, 0.03), ha='center', va='bottom')


# plot positions of surfaces between FV cells
aNodes = [-0.5, 0.5]
aLabels = ['b', 'e']
for xPoint, label in zip(aNodes, aLabels):
    ax.plot(xPoint, yPoint, ls='', marker='.', color='k')
    ax.annotate(label, xy=(xPoint+0.02, yPoint-0.005), ha='left', va='bottom')

# plot surfaces between FV cells
colors = ['C0', 'red']
for xPoint, color in zip(aNodes, colors):
    ax.plot([xPoint, xPoint], [-0.02, 0.02], ls='--', color=color)
arrAw = mpatches.FancyArrowPatch((-0.75, 0), (-0.5, 0), color='C0',
                            arrowstyle='<-,head_width=.15', mutation_scale=20)
arrAe = mpatches.FancyArrowPatch((0.5, 0), (0.75, 0), color='red',
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrAw)
ax.add_patch(arrAe)
ax.annotate(r"$A_b$", xy=(-0.6, 0.008), ha='center', va='center', color='C0')
ax.annotate(r"$A_e$", xy=(0.6, 0.008), ha='center', va='center', color='red')


# plot the delta-x distance
ax.plot([-0.5, 0.5], [-0.02, -0.02], ls='--', color='k')
ax.plot([-0.5, 0.5], [0.02, 0.02], ls='--', color='k')
arrdx = mpatches.FancyArrowPatch((-0.5, -0.025), (0.5, -0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrdx)
ax.annotate(r"$\Delta x$", xy=(0, -0.03), ha='center', va='center')

# finishing touches
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.05, 0.05)
ax.set_axis_off()


