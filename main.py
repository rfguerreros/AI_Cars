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

#############################################################
################# CONSTANTS FOR PROGRAM ##################### 
pixels = 100 # CALCULATION SPACE LATERAL SIZE
min_l = 0.05 # MINIMUM LENGTH FOR DISTANCE MEASUREMENT
deltaT = 0.01 # TIME INTERVAL
lane_l = 0.6 # PARAMETER FOR TRACK
np.random.seed(16)
n_cars = 10 # NUMBER OF CARS PER GENERATION
#############################################################

#############################################################
################# START WORLD AND TRACK #####################
earth = w.World(pixels)
monza = t.Track(l.lane(lane_l))
t.map(monza,earth,pixels)
xmin, xmax, ymin, ymax = monza.min_Xcoor, monza.max_Xcoor, monza.min_Ycoor, monza.max_Ycoor
print("Space is between %d<%d and %d<%d."%(xmin,xmax,ymin,ymax))
#############################################################

#############################################################
################## FIRST CAR GENERATION #####################
cars = []
brains = []
drivers = []

for ii in range(n_cars):
    cars.append(c.Car([0,0],np.random.randn(1),monza,earth,5+ii))
    l = False
    while l == False:
        l = loc.locate_cars(np.mod(ii,4),cars[ii])
    brains.append(n.Network(2,[6,10,10,2],False))
    drivers.append(d.Driver(cars[ii],brains[ii]))
#############################################################

for t in range(1000):
    for ii in range(n_cars):
        if drivers[ii].crash == False:
            drivers[ii].drive(deltaT, min_l)