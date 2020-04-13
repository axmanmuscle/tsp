# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:48:48 2020

@author: Alex
"""

import numpy as np
import numpy.polynomial as npp
import matplotlib.pyplot as plt

def neighbor_unif(p):
    x, y = p.linspace()
    s = np.random.uniform(x[0], x[-1])
    return s

def neighbor_local(x, p):
    x1, y1 = p.linspace()
    
    rng = 0.5
    low = x - rng/2
    high = x + rng/2
    
    if low < x1[0]:
        low = x1[0]
    if high > x1[-1]:
        high = x1[-1]
    
    s = np.random.uniform(low, high)
    return s

def E(y):
    return -y

def P(s, snew, t, p):
    ys = p(s)
    ys_new = p(snew)
    
    es = E(ys)
    es_new = E(ys_new)
    
    if es_new < es:
        return 1
    else:
        prob = np.exp(-(es_new - es)/(t/20))
        print(prob)
        return prob
    

if __name__ == "__main__":
    deg = 6
    x_pt = [0, 1, 2, 3, 4, 5, 6]
    y_pt = [0, 4, 2, 8, 5, 2, 0]
    
    p = npp.Polynomial.fit(x_pt, y_pt, deg)
    
    x, y = p.linspace(1000)
    
    plt.plot(x, y)
    
    x0 = np.random.uniform(0, 6)
    y0 = p(x0)
    naught, = plt.plot(x0, y0, 'r*')
        
    t0 = 20
    dt = 0.1
    num_iter = (t0 - 1)/dt
    t = t0
    plt.draw()
    plt.title('Temperature: {} Value: {:.2f}'.format(t, y0))
    
    xn = neighbor_unif(p)
    yn = p(xn)
    
    #naught.remove()
    while t > 1:
        t = t - dt
        
        current = xn
        #candidate = neighbor_unif(p)
        candidate = neighbor_local(current, p)
        switch = P(current, candidate, t, p)
        
        thresh = np.random.uniform()
        
        if switch > thresh:
            xn = candidate
        
        yn = p(xn)
        
        pt, = plt.plot([xn, xn], [0, yn], 'r')
        plt.title('Temperature: {:.2f} Value: {:.2f}'.format(t, yn))
        plt.draw()
        plt.pause(.1)
        pt.remove()
        
    pt, = plt.plot([xn, xn], [0, yn], 'r')
    plt.title('Temperature: {:.2f} Value: {:.2f}'.format(t, yn))
    plt.draw()