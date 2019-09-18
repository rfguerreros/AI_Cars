import numpy as np
import matplotlib.pyplot as plt
import math
import track as t
import world as w
import lane as l
import car as c

print("Loading begins")

pixels = 100

min_l = 0.01

earth = w.World(pixels)
monza = t.Track(l.lane(min_l))

t.map(monza,earth,pixels)

print("Loading ends")

xmin = monza.min_Xcoor
xmax = monza.max_Xcoor
ymin = monza.min_Ycoor
ymax = monza.max_Ycoor

mecho = c.Car([0.45*(xmax-xmin),0.5*(ymax+ymin)],0,monza,earth,5)

mecho.map(mecho.id)

plt.matshow(earth.Space)

plt.show()
