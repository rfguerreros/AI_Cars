import numpy as np
import matplotlib.pyplot as plt
import math
import track as t
import world as w
import lane as l
import car as c

pixels = 100

min_l = 0.7

earth = w.World(pixels)
monza = t.Track(l.lane(min_l))

t.map(monza,earth,pixels)

xmin = monza.min_Xcoor
xmax = monza.max_Xcoor
ymin = monza.min_Ycoor
ymax = monza.max_Ycoor

mecho = c.Car([0.4*(xmax-xmin),0.5*(ymax+ymin)],0,monza,earth,1)

print(xmin)
print(xmax)
print(ymin)
print(ymax)

print(mecho.pos)

mecho.map()

plt.matshow(earth.Space)

plt.show()
