# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:48:48 2020

@author: Alex
"""

import numpy as np
import numpy.polynomial as npp
import matplotlib.pyplot as plt

def neighbor(p):
    x, y = p.linspace()
    s = np.random.uniform(x[0], x[-1])
    return s

deg = 6
x_pt = [0, 1, 2, 3, 4, 5, 6]
y_pt = [0, 4, 2, 8, 5, 2, 0]

p = npp.Polynomial.fit(x_pt, y_pt, deg)

x, y = p.linspace(1000)

plt.plot(x, y)

x0 = np.random.uniform(0, 6)
y0 = p(x0)
plt.plot(x0, y0, 'r*')

plt.show()