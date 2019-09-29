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
#############################################################

#############################################################
################# START WORLD AND TRACK #####################
earth = w.World(pixels)
monza = t.Track(l.lane(lane_l))
t.map(monza,earth,pixels)
xmin, xmax, ymin, ymax = monza.min_Xcoor, monza.max_Xcoor, monza.min_Ycoor, monza.max_Ycoor
print("Space is between %d<%d and %d<%d."%(xmin,xmax,ymin,ymax))
#############################################################
