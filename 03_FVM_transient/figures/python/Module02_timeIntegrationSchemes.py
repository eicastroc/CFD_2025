#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:21:25 2023

@author: ecastro
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(6, 4))


Tp0 = 1
Tp1 = 0

t0 = 0
t1 = 1



# horizontal marking lines
ax.vlines(t0, -1, Tp0, ls='--', color='gray')
ax.vlines(t1, -1, Tp0, ls='--', color='gray')

# vertical marking lines
ax.hlines(Tp0, -0.25, 1, ls='--', color='gray')
ax.hlines(Tp1, -0.25, 1, ls='--', color='gray')



# temperature at time t
ax.plot(t0, Tp0, ls='', marker='o', color='k',)

# temperature at time t+dt
ax.plot(t1, Tp1, ls='', marker='o', color='k',)


# Fully explicit scheme
xExpl = np.array([0, 0.9, 0.95, 0.96, 0.97, 0.98, 0.99, 1])
yExpl = np.array([1, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95, 0])
ax.plot(xExpl, yExpl, label="Explicito")


# Fully implicit scheme
xImpl = np.array([0, 0.01, 0.02, 0.03, 0.04, 0.05, 1])
yImpl = np.array([1, 0.05, 0.04, 0.03, 0.02, 0.01, 0])
ax.plot(xImpl, yImpl, label="Implicito")

# Crank-Nicolson
xCN = np.array([0, 1])
yCN = np.array([1, 0])
ax.plot(xCN, yCN, label='Crank-Nicolson')


# finishing touches
ax.set_xlim(-0.25, 1.25)
ax.set_ylim(-0.25, 1.25)

ax.set_xticks([0, 1], labels=[r"$t$", r"$t + \Delta t$"])
ax.set_yticks([0, 1], labels=[r"$T_P^1$", r"$T_P^0$"])
ax.legend(ncols=python3)
