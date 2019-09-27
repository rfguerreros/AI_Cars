import numpy as np
import matplotlib.pyplot as plt
import math
import track as t
import world as w
import lane as l
import car as c
import driver as d

pixels = 100
min_l = 0.05
deltaT = 0.01
lane_l = 0.6

earth = w.World(pixels)
monza = t.Track(l.lane(lane_l))

t.map(monza,earth,pixels)

xmin = monza.min_Xcoor
xmax = monza.max_Xcoor
ymin = monza.min_Ycoor
ymax = monza.max_Ycoor

mecho = c.Car([0.42*(xmax-xmin),0.5*(ymax+ymin)],0,monza,earth,5)

deo = d.Driver(mecho)

mecho.map(mecho.id)

plt.matshow(earth.Space)

t=0

while(deo.crash == False and t<1000):
    t+=1
    deo.drive(deltaT,min_l)

plt.matshow(earth.Space)

plt.show()
