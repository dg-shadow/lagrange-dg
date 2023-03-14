#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

G=6.6743e-11

class GravitationalMass(object):
    def __init__(self, mass, location, name=None):
        self._mass = mass
        self._location = np.asarray(location)
        self._name = name

    def field_contribution(self, location):
        r = location - self._location  # Vector of distance
        r2 = numpy.square(r).sum()
        field = -G*self._mass/r2
        return field




earth = GravitationalMass(5.972e24, [0,0])


x = np.arange(-1e8, 5e8, 10e5)
y = np.arange(-1e8, 1e8, 10e5)

xv, yv = np.meshgrid(x, y)


h = np.empty((y.shape[0], x.shape[0])) #-1/((xv**2 + yv**2)+1e-10)
print (h.shape)


for i, x_ in enumerate(x):
    for j, y_ in enumerate(y):
        h[j][i]  = -1/((x_**2 + y_**2)+1e-10)



exit()


print (np.min(h))
print (np.max(h))

lev=np.linspace(-1e15, 0, 500)

lev = [(i - 500) * 1e-15 for i in range(501)]




cs = plt.contour(x, y, h, levels=lev) #, levels=[-50, -25, 0, 25, 50],
#                  colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
#cs.cmap.set_over('red')
#cs.cmap.set_under('blue')
#cs.changed()


plt.show()
