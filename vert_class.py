# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:59:36 2019

@author: Alex
"""

import numpy as np
import matplotlib.pyplot as plt
import copy

np.random.seed(20190918)

def vert_dist(v1, v2):
    d = np.sqrt((v1.x-v2.x)**2 + (v1.y-v2.y)**2)
    return d

class vert():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = 0
        self.visit = 0
        self.order = -1
        
    def reset(self):
        self.dist = 0
        self.visit = 0
        self.order = -1
                 
n = 15
best_dist = 1000

x = np.random.randint(0, 50, n)
y = np.random.randint(0, 100, n)

fig = plt.figure()
ax = fig.add_subplot(121)
ax.scatter(x, y, marker='s', c='b')
ax.set_xlim((0,50))
ax.set_ylim((0,100))

ax2 = fig.add_subplot(122)
ax2.scatter(x, y, marker='s', c='g')
ax2.set_xlim((0,50))
ax2.set_ylim((0,100))

vert_list = []

for idx in range(n):
    vi = vert(x[idx], y[idx])
    vert_list.append(vi)
    
for idx in range(n):
    ## main loop
    ax.clear()
    ax.scatter(x, y, marker='s', c='b')
    ax.set_xlim((0,50))
    ax.set_ylim((0,100))

    start_vert = vert_list[idx]
    
    start_vert.visit = 1
    start_vert.order = 0
    
    u = start_vert
    ax.scatter(u.x,u.y,marker='s', c='g')
    ax.set_title('Starting from {}'.format(idx))
    remain = [i for i in vert_list if i.visit==0]
    while len(remain) > 0:
        min_dist = 500
        for v in remain:
            d = vert_dist(u, v)
            ax.plot([u.x, v.x], [u.y, v.y], 'r-')
            plt.draw()
            plt.pause(0.00001)
            if d < min_dist:
                min_dist = d
                min_dist_vert = v
        b = ax.lines
        
        bidx = 0
        while True:
            if len(b) == 0:
                break
            bi = b[len(b)-1-bidx]
            if bi.get_color() == 'r':
                bi.remove()
            else:
                bidx += 1
                if bidx > len(b):
                    break
                
            
#        for bi in b:
#            if bi.get_color() == 'r':
#                bi.remove()
                
#        for bidx in range(len(b)):
#            bi = b.pop(bidx)
#            if bi.get_color() == 'r':
#                bi.remove()
        
        min_dist_vert.visit = 1
        min_dist_vert.order = u.order + 1
        min_dist_vert.dist = min_dist
        
        ax.plot([u.x, min_dist_vert.x], [u.y, min_dist_vert.y], 'g-')
        
        u = min_dist_vert
        ax.scatter(u.x,u.y,marker='s', c='g')
        remain = [i for i in vert_list if i.visit==0]
        
    plt.pause(0.5)
    total_dist = 0
    for v in vert_list:
        total_dist += v.dist
    
    if total_dist <= best_dist:
        best_dist = total_dist
        best_collection = [copy.deepcopy(v) for v in vert_list]
        b = ax.lines
        for idx in range(len(b)):
            ax2.plot([best_collection[idx].x,best_collection[idx+1].x], [best_collection[idx].y,best_collection[idx+1].y], 'g-')
        ax2.set_title('Best Distance: {}'.format(best_dist.round(2)))
        
    for v in vert_list:
        v.reset()
        
    b = ax.lines
    for idx2 in range(len(b)):
        b[0].remove()
         
 