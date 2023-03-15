#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
from time import process_time


G=6.6743e-11

class GravitationalMass(object):
    def __init__(self, mass, location, radius, name=None):
        self._mass = mass
        self._x = location[0]
        self._y = location[1]
        self._name = name
        self._radius = radius
        self._r2 = radius**2

    def scalar_field_contribution(self, x, y):
        x -= self._x
        y -= self._y

        r2 = y*y + x*x

        if r2 <= self._r2:
            return 0

        field = -G*self._mass/r2
        return field

    # def get_scalar_field(self, xx, yy):
    #     area = np.dstack((xx, yy))
    #     return np.apply_along_axis(self.scalar_field_contribution, 2, area)

    # d = area - self._location
    # magnitudes = np.apply_along_axis(np.linalg.norm,  2, d)
    # units = d / magnitudes




earth = GravitationalMass(5.972e24, [0,       0], 6.371e6)
moon  = GravitationalMass(7.348e22, [3.844e8, 0], 1.737e6)

x = np.arange(-4e8, 10e8, 10e5)
y = np.arange(-4e8, 4e8, 10e5)

xv, yv = np.meshgrid(x, y)

start = process_time()
h = np.empty((y.shape[0], x.shape[0])) #-1/((xv**2 + yv**2)+1e-10)

for i, x_ in enumerate(x):
    for j, y_ in enumerate(y):
        h[j][i]  = earth.scalar_field_contribution(x_, y_) + moon.scalar_field_contribution(x_,y_)

print (process_time() - start)

# start = process_time()
# h2 = earth.get_scalar_field(xv, yv)
# print (process_time() - start)



#exit()


print (np.min(h))
print (np.max(h))

lev=np.linspace(-0.02, 0, 500)




cs = plt.contour(x, y, h, levels=lev) #, levels=[-50, -25, 0, 25, 50],
#                  colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
#cs.cmap.set_over('red')
#cs.cmap.set_under('blue')
#cs.changed()
#cs.add

plt.show()
