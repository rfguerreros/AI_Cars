import numpy as np
import matplotlib.pyplot as plt
import math
import track as t
import world as w
import lane as l
import car as c
import driver as d
import network as n
import locator as loc

pixels = 100
min_l = 0.05
deltaT = 0.01
lane_l = 0.6

np.random.seed(16)

earth = w.World(pixels)
monza = t.Track(l.lane(lane_l))

t.map(monza,earth,pixels)

xmin = monza.min_Xcoor
xmax = monza.max_Xcoor
ymin = monza.min_Ycoor
ymax = monza.max_Ycoor

print("Space is between %d<%d and %d<%d."%(xmin,xmax,ymin,ymax))

i=0
j=0
while i<50:
    l = loc.locate_cars(earth,np.mod(j,4))
    if(l==True): 
        i+=1
    j+=1

plt.matshow(earth.Space)

plt.show()

""" aveo = c.Car([0.42*(xmax-xmin),0.5*(ymax+ymin)],np.pi,monza,earth,5)
brain = n.Network(2,[6,7,7,2],False)
deo = d.Driver(aveo,brain)

aveo.map(aveo.id)

t=0

while(deo.crash==False and t<1000):
    deo.drive(deltaT,min_l)
    t+=1

cars = []
brains = []
drivers = []
"""