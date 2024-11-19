#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:46:46 2023

@author: ecastro
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


xmin = 0
xmax = 0.05
dx = 0.005
hiBound = 0.005
loBound = -hiBound


xCoords = np.array([xmin, xmax])
yCoords = np.array([0, 0])

#%%
""" Plot of calculation domain """
fig, ax = plt.subplots(figsize=(8, 4))

# domain
ax.plot(xCoords, yCoords, ls='-', color='gray')

# west bound
ax.plot([xmin, xmin], [loBound, hiBound], ls='--', color='C0')
ax.annotate(r'$x=0$', xy=(0, -0.007), 
            ha='center', va='center', color='C0')

# east bound
ax.plot([xmax, xmax], [loBound, hiBound], ls='--', color='C1')
ax.annotate(r'$x=0.05 \, m$', xy=(0.05, -0.007), 
            ha='center', va='center', color='C1')

# Showing the x-axis
ax.annotate(r"$x$", xy=(0.005, 0.003), ha='center', va='center')
arrWP = mpatches.FancyArrowPatch((0, 0.001), (0.01, 0.001),
                                 color = 'k',
                                 arrowstyle='->,head_width=.15', 
                                 mutation_scale=20)
ax.add_patch(arrWP)

# finishing touches
ax.set_xlim(-0.005, 0.055)
ax.set_ylim(-0.015, 0.015)
ax.set_axis_off()



#%%
""" Plot of discretized calculation domain """
fig, ax = plt.subplots(figsize=(8, 4))



# domain
# domain
ax.plot(xCoords, yCoords, ls='-', color='gray')
ax.plot(xCoords, yCoords+hiBound, ls = '--', color='k')
ax.plot(xCoords, yCoords+loBound, ls = '--', color='k')

# boundary faces
ax.annotate(r'$A_{0,1}$', xy=(xmin, -0.006), 
            ha='center', va='center', color='C0')
ax.plot([xmin, xmin], [loBound, hiBound], ls='--', color='C0')

ax.annotate(r'$A_{10,11}$', xy=(xmax, -0.006), 
            ha='center', va='center', color='C1')
ax.plot([xmax, xmax], [loBound, hiBound], ls='--', color='C1')

# inner faces
xInnerFaces = np.arange(dx, 0.05, dx)
for i, x in enumerate(xInnerFaces):
    faceLabel = ''.join([r'$A_{', str(i+1),',', str(i+2),'}$'])
    ax.annotate(faceLabel, xy=(x, -0.006), ha='center', va='center', color='r')
    ax.plot([x, x], [loBound, hiBound], ls='--', color='r')
    
# cell centroids
xCellCentroids = np.arange(dx/2, 0.05, dx)
for i, x in enumerate(xCellCentroids):
    cellLabel = ''.join([r'$C_{', str(i+1),'}$'])
    ax.annotate(cellLabel, xy=(x, -0.0012), ha='center', va='center')
    ax.plot(x, 0, ls='-', marker='o', color='k')
    
    
# boundary nodes
ax.annotate(r'$C_{0}$', xy=(xmin-0.0025, 0), ha='center', va='center')
ax.annotate(r'$x=0$', xy=(xmin, -0.01), 
            ha='center', va='center', color='C0')
ax.plot(xmin, 0, marker='o', color='k', markerfacecolor='w')

ax.annotate(r'$C_{11}$', xy=(xmax+0.0025, 0), ha='center', va='center')
ax.annotate(r'$x=0.05 \, m$', xy=(xmax, -0.01), 
            ha='center', va='center', color='C1')
ax.plot(xmax, 0, marker='o', color='k', markerfacecolor='w')

# finishing touches
ax.set_xlim(-0.005, 0.055)
ax.set_ylim(-0.015, 0.015)
ax.set_axis_off()