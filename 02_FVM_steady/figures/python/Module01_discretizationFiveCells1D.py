#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:01:09 2023

@author: ecastro
"""

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(6, 4))


cxNodes = np.array([1, 2, 3, 4, 5])
cyNodes = np.zeros_like(cxNodes)
cLabels = [r"$C_1$", r"$C_2$", r"$C_3$", r"$C_4$", r"$C_5$"]
TLabels = [r"$T_1$", r"$T_2$", r"$T_3$", r"$T_4$", r"$T_5$"]

axNodes = np.arange(1.5, 5.5, 1)
ayNodes = np.zeros_like(axNodes)


# plot horizontal line (x-axis)
ax.axhline(0, ls='-', color='k', alpha=0.5)

# Plot the cell nodes
ax.plot(cxNodes, cyNodes, ls='', marker='o', color='k', markerfacecolor='w')
for x, y, clabel, Tlabel in zip(cxNodes, cyNodes, cLabels, TLabels):
    ax.annotate(clabel, xy=(x, y-0.005), ha='center', va='center')
    ax.annotate(Tlabel, xy=(x, y+0.005), ha='center', va='bottom', color='b')
    
    
# plot the nodes of exchange surfaces
ax.plot(axNodes, ayNodes, ls='', marker='.', color='k')
for x in axNodes:
    ax.axvline(x, ymin=0.3, ymax=0.7, ls='--', color='red')
    
# plot the delta x
ax.plot([0.5, 5.5], [0.02, 0.02], ls='--', color='k')
ax.plot([0.5, 5.5], [-0.02, -0.02], ls='--', color='k')

# plot boundaries
ax.axvline(0.5, ymin=0.3, ymax=0.7, ls='--', color='C0')
ax.annotate("Frontera", xy=(0.4, 0), color='C0',
            ha='right', va='center', rotation=90)
ax.axvline(5.5, ymin=0.3, ymax=0.7, ls='--', color='C1')
ax.annotate("Frontera", xy=(5.6, 0), color='C1',
            ha='left', va='center', rotation=90)

ax.set_xlim(0, 6)
ax.set_ylim(-0.05, 0.05)
ax.set_axis_off()