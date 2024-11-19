#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:12:36 2024

@author: ecastro
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import matplotlib.patches as mpatches


centroids = True
areaVectors = False
distances = True
saveFig = True

xy = [1, 3, 5]

X, Y = np.meshgrid(xy, xy)

#%%
fig, ax = plt.subplots(figsize=(4, 4))


# centroids
ax.scatter(X, Y, marker='o', s=150, 
           c='lightblue', alpha=0.5, edgecolors='k')


if centroids == True:
    
    # centroids
    ax.annotate("P", xy=[3, 3], fontweight='bold', ha='center', va='center')
    ax.annotate("E", xy=[5, 3], fontweight='bold', ha='center', va='center')
    ax.annotate("W", xy=[1, 3], fontweight='bold', ha='center', va='center')
    ax.annotate("N", xy=[3, 5], fontweight='bold', ha='center', va='center')
    ax.annotate("S", xy=[3, 1], fontweight='bold', ha='center', va='center')
    

if areaVectors == True:
    # area vectors
    arrowAe = mpatches.FancyArrowPatch((4, 3), (4.5, 3), color='orange', mutation_scale=5)
    ax.annotate(r"$A_e$", xy=(4.25, 3), color='orange', ha='center', va='bottom')
    ax.add_patch(arrowAe)
    
    arrowAw = mpatches.FancyArrowPatch((2, 3), (1.5, 3), color='orange', mutation_scale=5)
    ax.annotate(r"$A_w$", xy=(1.75, 3), color='orange', ha='center', va='bottom')
    ax.add_patch(arrowAw)

    arrowAn = mpatches.FancyArrowPatch((3, 4), (3, 4.5), color='orange', mutation_scale=5)
    ax.annotate(r"$A_n$", xy=(3, 4.25), color='orange', ha='left', va='center')
    ax.add_patch(arrowAn)

    arrowAs = mpatches.FancyArrowPatch((3, 2), (3, 1.5), color='orange', mutation_scale=5)
    ax.annotate(r"$A_s$", xy=(3, 1.75), color='orange', ha='left', va='center')
    ax.add_patch(arrowAs)
    

if distances == True:
    # disteances between centroids
    ax.plot([3, 5], [2.75, 2.75], ls='--', marker='|', color='green')
    ax.annotate(r"$(\delta_x)_e$", xy=(4, 2.75), color="green", ha='center', va="top")
    
    ax.plot([3, 1], [2.75, 2.75], ls='--', marker='|', color='green')
    ax.annotate(r"$(\delta_x)_w$", xy=(2, 2.75), color="green", ha='center', va="top")
    
    ax.plot([2.75, 2.75], [3, 5], ls='--', marker='_', color='green')
    ax.annotate(r"$(\delta_x)_n$", xy=(2.75, 4), color="green", ha='right', va="center") 

    ax.plot([2.75, 2.75], [3, 1], ls='--', marker='_', color='green')
    ax.annotate(r"$(\delta_x)_s$", xy=(2.75, 2), color="green", ha='right', va="center") 

       
# grid
ax.set_xticklabels([])
ax.set_xlim(-0.01, 6.01)
ax.set_yticklabels([])
ax.set_ylim(-0.01, 6.01)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.grid()

fig.tight_layout()

if saveFig == True:
    name = "compassWithDistancesBetweenCentroids"
    fig.savefig(".".join([name,"pdf"]), dpi=300)
    fig.savefig(".".join([name,"png"]), dpi=300)