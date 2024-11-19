#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:20:23 2023

@author: ecastro
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


fig, ax = plt.subplots(figsize=(6, 4))

# geometry
crNodes = np.array([1.5, 2.5, 3.5])
cyNodes = np.zeros_like(crNodes)
cLabels = ['W', 'P', 'E']
arNodes = np.array([2, 3])
ayNodes = np.zeros_like(arNodes)
r = np.linspace(2, 4, 11)
theta = np.linspace(-0.5, 0.5, 101)

# draw r-axis
ax.axhline(0, color='k', alpha=0.25)

# draw fv cell nodes
for xPoint, yPoint, label in zip(crNodes, cyNodes, cLabels):
    ax.plot(xPoint, yPoint, ls='', marker='o', color='k', markerfacecolor='w')
    ax.annotate(label, xy=(xPoint, yPoint-0.3), ha='center', va='bottom')

# Plot distances between nodes
for rPoint in crNodes:
    ax.plot([rPoint, rPoint], [0.2, 0.8], ls='-', color='k')
arrWP = mpatches.FancyArrowPatch((1.5, 0.5), (2.5, 0.5),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
arrPE = mpatches.FancyArrowPatch((2.5, 0.5), (3.5, 0.5),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrWP)
ax.add_patch(arrPE)
ax.annotate(r"$(\delta r)_w$", xy=(2, 0.5), ha='center', va='bottom')
ax.annotate(r"$(\delta r)_e$", xy=(3, 0.5), ha='center', va='bottom')


# plot positions of surfaces between FV cells
aLabels = ['w', 'e']
for xPoint, yPoint, label in zip(arNodes, ayNodes, aLabels):
    ax.plot(xPoint, yPoint, ls='', marker='.', color='k')
    ax.annotate(label, xy=(xPoint, yPoint-0.15), ha='center', va='bottom')

# plot surfaces between FV cells
for arNode in arNodes:
    ax.plot(arNode*np.cos(theta), arNode*np.sin(theta), ls='--', color='red')
arrAw = mpatches.FancyArrowPatch((2, 0), (1.6, 0), color='red',
                            arrowstyle='->,head_width=.15', mutation_scale=20)
arrAe = mpatches.FancyArrowPatch((3, 0), (3.4, 0), color='red',
                            arrowstyle='->,head_width=.15', mutation_scale=20)
ax.add_patch(arrAw)
ax.add_patch(arrAe)
ax.annotate("Aw", xy=(1.8, 0.15), ha='center', va='center', color='red')
ax.annotate("Ae", xy=(3.2, 0.15), ha='center', va='center', color='red')

# draw the delta r    
ax.plot(arNodes*np.cos(-0.5), arNodes*np.sin(-0.5), ls='--', color='k')
ax.plot(arNodes*np.cos(0.5), arNodes*np.sin(0.5), ls='--', color='k')

for rPoint in arNodes:
    ax.plot([rPoint, rPoint], [-0.2, -0.8], ls='-', color='k')
arrDR = mpatches.FancyArrowPatch((2, -0.5), (3, -0.5),
                            arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arrDR)
ax.annotate(r"$\Delta r$", xy=(2.5, -0.7), ha='center', va='bottom')


# d theta
rNodes = np.array([0, 1])
ax.plot(rNodes*np.cos(-0.5), rNodes*np.sin(-0.5), ls='-', color='g')
ax.plot(rNodes*np.cos(0.5), rNodes*np.sin(0.5), ls='-', color='g')
ax.plot(0.5*np.cos(theta), 0.5*np.sin(theta), ls='--', color='g')
ax.annotate(r"$\Delta \theta$", xy=(0.5, 0), ha='left', va='bottom', color='g')



ax.set_xlim(0, 5)
ax.set_ylim(-1.5, 1.5)
ax.set_axis_off()