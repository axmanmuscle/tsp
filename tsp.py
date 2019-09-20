# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:10:37 2019

@author: Alex
"""
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter


def get_dist(v1, v2):
    return np.sqrt(v1[0]*v2[0] + v1[1]*v2[1])

np.random.seed(20190917)

n = 7

x = np.random.randint(0, 50, n)
y = np.random.randint(0, 100, n)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y)
ax.set_xlim((0,50))
ax.set_ylim((0,100))

verts = [[x[i], y[i], 0] for i in range(n)]

start = np.random.randint(0, n-1)

verts[start][2] = 1
u = verts[start]
total_dist = 0
cont = True
while cont:
    verts = [vert for vert in verts if vert[2] == 0]
    if len(verts)==0:
        break
    dist_list = [get_dist(u, v) for v in verts]
    argmin = min(enumerate(dist_list), key=itemgetter(1))[0]
    dist = dist_list[argmin]
    total_dist += dist
    verts[argmin][2] = 1
    u = verts[argmin]
    


plt.show()