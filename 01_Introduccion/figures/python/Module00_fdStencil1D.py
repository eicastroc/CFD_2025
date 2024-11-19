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

# plot nodes on the FD grid
cNodes = [-1, 0, 1]
cLabels = ['1', '2', '3']
for xPoint, label in zip(cNodes, cLabels):
    ax.plot(xPoint, yPoint, ls='', marker='o', color='k', markerfacecolor='w')
    ax.annotate(label, xy=(xPoint, yPoint-0.01), ha='center', va='bottom')

# Plot distances between nodes 
for xPoint in cNodes:
    ax.plot([xPoint, xPoint], [0.01, 0.04], ls='-', color='k')
arrWP = mpatches.FancyArrowPatch((-1, 0.025), (0, 0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
arrPE = mpatches.FancyArrowPatch((0, 0.025), (1, 0.025),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrWP)
ax.add_patch(arrPE)
ax.annotate(r"$\Delta x$", xy=(-0.5, 0.03), ha='center', va='bottom')
ax.annotate(r"$\Delta x$", xy=(0.5, 0.03), ha='center', va='bottom')




# finishing touches
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.02, 0.05)
ax.set_axis_off()


