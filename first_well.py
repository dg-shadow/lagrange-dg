#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
from time import process_time
from math import sqrt

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

    def centripetal_acc(self, x,  y, angular_v):
        return sqrt(x*x + y*y) * angular_v*angular_v

    # def get_scalar_field(self, xx, yy):
    #     area = np.dstack((xx, yy))
    #     return np.apply_along_axis(self.scalar_field_contribution, 2, area)

    # d = area - self._location
    # magnitudes = np.apply_along_axis(np.linalg.norm,  2, d)
    # units = d / magnitudes


sun   = GravitationalMass(1.989e30, [0,        0], 6.963e8)
earth = GravitationalMass(5.972e24, [1.496e11, 0], 6.371e6)
moon  = GravitationalMass(7.348e22, [3.844e8 + earth._x,  0], 1.737e6)

x = np.linspace(1.45e11,  1.55e11, 1000)
y = np.linspace(-5e9, 5e9, 500)

xv, yv = np.meshgrid(x, y)

start = process_time()
h = np.empty((y.shape[0], x.shape[0])) #-1/((xv**2 + yv**2)+1e-10)

for i, x_ in enumerate(x):
    for j, y_ in enumerate(y):
        h[j][i]  = sun.scalar_field_contribution(x_, y_) + earth.scalar_field_contribution(x_, y_)# + moon.scalar_field_contribution(x_,y_)

print (process_time() - start)

# start = process_time()
# h2 = earth.get_scalar_field(xv, yv)
# print (process_time() - start)



#exit()


print (np.min(h))
print (np.max(h))

lev=np.linspace(-0.0066, -0.005, 500)




cs = plt.contour(x, y, h, levels=lev)
plt.colorbar(cs)
#, levels=[-50, -25, 0, 25, 50],
#                  colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
#cs.cmap.set_over('red')
#cs.cmap.set_under('blue')
#cs.changed()
#cs.add

plt.show()
