#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:56:43 2023

@author: ecastro
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



#%% Structured mesh
xNodes = np.array([0, 0.3, 0.6, 0.9, 1.1, 1.2, 1.3])
yNodes = np.array([0, 0.1, 0.3, 0.6, 0.9])


fig, ax = plt.subplots()

for xNode in xNodes:
    ax.axvline(xNode, color='k')
    
for yNode in yNodes:
    ax.axhline(yNode, color='k')
    

# Una celda
x=np.array([0.3, 0.6])
y1 = np.array([0.3, 0.3])
y2 = np.array([0.6, 0.6])
ax.fill_between(x, y1, y2, color='lightgray')
ax.annotate("Celda", xy=(0.45, 0.35), ha='center', va='center')

# Un centroide
ax.plot(0.45, 0.45, ls="", marker='o', color="k", markersize=10)
arrNode = mpatches.FancyArrowPatch((0.52, 0.50), (0.45, 0.45),
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrNode)
ax.annotate("\nNodo", xy=(0.53, 0.55), va='center', ha='center')



# Un nodo
ax.plot(0.9, 0.6, ls="", marker='o', 
        color="k", markerfacecolor="None", markersize=10)
arrNode = mpatches.FancyArrowPatch((0.95, 0.7), (0.9, 0.6),
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrNode)
ax.annotate("\nVertice", xy=(1.0, 0.75), va='center', ha='center')

# Una cara
arrFace = mpatches.FancyArrowPatch((0.7, 0.2), (0.6, 0.2),
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrFace)
ax.annotate("Cara", xy=(0.75, 0.2), va='center', ha='center')

# Finishing touches
ax.set_xlim(0, 1.3)
ax.set_ylim(0, 0.9)
#ax.set_axis_off()



#%% Unstructured mesh

fig, ax = plt.subplots()

t1x = np.array([0.5,  0.1, -0.4, -0.5, -0.3, -0.2, 0.2, 0.5])
t1y = np.array([0.0, -0.5, -0.4, -0.1,  0.2,  0.5, 0.4, 0.0])


ax.plot(t1x, t1y, ls='-', marker='', color='k',)
for x, y in zip(t1x, t1y):
    ax.plot([0, x], [0, y], ls='-', marker='', color='k')
    

t2x = np.array([-0.3, -0.5, -0.7, -0.7, -0.5, -0.2])
t2y = np.array([ 0.2, -0.1,  0.2,  0.4,  0.5, 0.5])

ax.plot(t2x, t2y, ls='-', marker='', color='k',)
for x, y in zip(t2x[:-1], t2y[:-1]):
    ax.plot([-0.5, x], [0.3, y], ls='-', marker='', color='k')
    
    
# Vertices
ax.plot(0.0, 0.0, ls='', marker='o', color='k', 
        markerfacecolor='None', markersize=10)
ax.plot(t1x, t1y, ls='', marker='o', color='k',
        markerfacecolor='None', markersize=10)
ax.plot(-0.5, 0.3, ls='', marker='o', color='k',
        markerfacecolor='None', markersize=10)
ax.plot(t2x, t2y, ls='', marker='o', color='k',
        markerfacecolor='None', markersize=10)





arrVertex = mpatches.FancyArrowPatch((0.1, 0.05), (0, 0), color='k',
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrVertex)
ax.annotate("Vertice", xy=(0.17, 0.05), ha='center', va='center', color='k')


ax.annotate("Celda", xy=(-0.37, 0.37), ha='center', va='center', color='k')