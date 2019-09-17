import numpy as np
import math

class Car:
    def __init_(self,pos,ori,track,world,c_id):
        self.pos = np.asarray(pos)
        self.ori = math.fmod(ori,2*np.pi)
        self.xi = 0
        self.yi = 0
        self.sensor = np.zeros(6)
        self.track_in = track
        self.world_in = world
        self.vel = 0
        self.id = c_id
