import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy


x = np.arange(-12e6, 12e6, 10e4)
y = x.reshape(-1, 1)
h = -1/((x*x + y*y)+1e-10)

lev = [(i - 500) * 1e-15 for i in range(501)]

print np.min(h)
print np.max(h)
print lev

cs = plt.contour(x, x, h, levels=lev) #, levels=[-50, -25, 0, 25, 50],
                  #colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
cs.cmap.set_over('red')
cs.cmap.set_under('blue')
cs.changed()


plt.show()
