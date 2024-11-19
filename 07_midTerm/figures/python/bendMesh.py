#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:12:36 2024

@author: ecastro
"""


import numpy as np
import matplotlib.pyplot as plt


centroids = True
saveFig = True

X = [[1, 3, 5], [1, 3, 5], [1, 3, np.nan]]
Y = [[1, 1, 1], [3, 3, 3], [5, 5, np.nan]]

#%%
fig, ax = plt.subplots(figsize=(4, 4))


# centroids
ax.scatter(X, Y, marker='o', s=150, 
           c='lightblue', alpha=0.5, edgecolors='k')


if centroids == True:
    
    # centroids
    ax.annotate("1", xy=[1, 1], fontweight='bold', ha='center', va='center')
    ax.annotate("2", xy=[3, 1], fontweight='bold', ha='center', va='center')
    ax.annotate("3", xy=[5, 1], fontweight='bold', ha='center', va='center')
    ax.annotate("4", xy=[1, 3], fontweight='bold', ha='center', va='center')
    ax.annotate("5", xy=[3, 3], fontweight='bold', ha='center', va='center')
    ax.annotate("6", xy=[5, 3], fontweight='bold', ha='center', va='center')
    ax.annotate("7", xy=[1, 5], fontweight='bold', ha='center', va='center')
    ax.annotate("8", xy=[3, 5], fontweight='bold', ha='center', va='center')
    
# grid  
ax.hlines([0, 2, 4, 6], xmin=[0, 0, 0, 0], xmax=[6, 6, 6, 4],
          linestyle='-', color='gray')
ax.vlines([0, 2, 4, 6], ymin=[0, 0, 0, 0], ymax=[6, 6, 6, 4],
          linestyle='-', color='gray')


ax.spines[['left', 'right', 'top', 'bottom']].set_visible(False) 
# grid
ax.set_xticklabels([])
ax.set_xlim(-0.01, 6.01)
ax.set_yticklabels([])
ax.set_ylim(-0.01, 6.01)


fig.tight_layout()

if saveFig == True:
    name = "bendMesh"
    fig.savefig(".".join([name,"pdf"]), dpi=300)
    fig.savefig(".".join([name,"png"]), dpi=300)