#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:27:50 2023

@author: ecastro
"""

import numpy as np
import matplotlib.pyplot as plt

lamb_P = 1000
lamb_E = 1

# cell nodes
P = 0
E = 1

# shared cell face node
e = np.linspace(0, 1, 101)


# distances
dx_e = E - P

dx_eLeft  = e - P
dx_eRight = E - e




# Linear interpolation
lamb_eLinear = dx_eLeft * lamb_P + dx_eRight * lamb_E
# harmonic mean interpolation
lamb_eHarmonic = np.power(dx_eLeft / lamb_P + dx_eRight / lamb_E, -1)



fig, ax = plt.subplots(figsize=(6, 4))

ax.stem([0, 1], [lamb_P, lamb_E], linefmt='b-', markerfmt='b')
ax.annotate(r"$\lambda_P$", xy=(0.05, lamb_P), ha='center', va='center', color='b')
ax.annotate(r"$\lambda_P$", xy=(0.95, lamb_E), ha='center', va='center', color='b')

#ax.plot(e, lamb_eLinear, label=r"$\lambda_e$ (linear)")
ax.plot(e, lamb_eHarmonic, label=r"$\lambda_e$ (harmonic)")

ax.axhline(2, ls='--', color='k', alpha=0.5)

ax.plot(0.5, (2*lamb_P*lamb_E)/(lamb_P+lamb_E), ls='', 
        marker="o", color='k', markerfacecolor='w')

ax.set_yscale('log')
ax.set_xlabel(r'$f_{e-}$')
ax.set_ylabel(r'$\lambda$')
ax.legend(loc='center right')