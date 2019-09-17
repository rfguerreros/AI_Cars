import numpy as np
import math

class Car:
    def __init__(self,pos,ori,track,world,c_id):
        self.pos = np.asarray(pos)
        self.ori = math.fmod(ori,2*np.pi)
        self.xi = 0
        self.yi = 0
        self.sensor = np.zeros(6)
        self.track_in = track
        self.world_in = world
        self.vel = 0
        self.id = c_id

    def sense_world(self,x,y):
        xi = int((x*(self.world_in.pixels-9)+(4*self.track_in.max_Xcoor-(self.world_in.pixels-5)*self.track_in.min_Xcoor))/self.track_in.lx)
        yi = int((y*(self.world_in.pixels-9)+(4*self.track_in.max_Ycoor-(self.world_in.pixels-5)*self.track_in.min_Ycoor))/self.track_in.ly)
        return self.world_in.Space[xi,yi]

    def map(self):
        xi = int((self.pos[0]*(self.world_in.pixels-9)+(4*self.track_in.max_Xcoor-(self.world_in.pixels-5)*self.track_in.min_Xcoor))/self.track_in.lx)
        yi = int((self.pos[1]*(self.world_in.pixels-9)+(4*self.track_in.max_Ycoor-(self.world_in.pixels-5)*self.track_in.min_Ycoor))/self.track_in.ly)
        self.world_in.Space[xi,yi]=self.id