#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:36:04 2024

@author: ecastro
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([0, 1, 2, 3])

coor = [[0.5, 2.5], [1.5, 2.5], [2.5, 2.5],
        [0.5, 1.5], [1.5, 1.5], [2.5, 1.5],
        [0.5, 0.5], [1.5, 0.5], [2.5, 0.5]]


def plotgrid(tags):

    fig, ax = plt.subplots(figsize=(2, 2))
    
    for x in X:
        # cell boundaries
        ax.axhline(x)
        ax.axvline(x)

    for xy, tag in zip(coor, tags):
        # tags at center
        ax.annotate(tag, xy=(xy), ha='center', va='center')    
    
    ax.set_xlim(-0.1, 3.1)
    ax.set_ylim(-0.1, 3.1)
    
    ax.axis('off')
    
#%%
plotgrid([1, 2, 3, 4, 5, 6, 7, 8, 9])
plotgrid([1, 3, 6, 2, 5, 8, 4, 7, 9])
plotgrid([9, 2, 3, 8, 1, 4, 7, 6, 5])