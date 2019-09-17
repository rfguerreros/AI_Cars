import numpy as np
import matplotlib.pyplot as plt
import math
import track as t
import world as w
import lane as l

pixels = 100

min_l = 0.7

earth = w.World(pixels)
monza = t.Track(l.lane(min_l))

t.map(monza,earth,pixels)

plt.matshow(earth.Space)

plt.show()
