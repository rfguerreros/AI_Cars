import numpy as np
import math

def extend_line(x,t,min_l):
    x[0] = x[0] + 2.*min_l * np.cos(t)
    x[1] = x[1] + 2.*min_l * np.sin(t)

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

    def map(self,a):
        xi = int((self.pos[0]*(self.world_in.pixels-9)+(4*self.track_in.max_Xcoor-(self.world_in.pixels-5)*self.track_in.min_Xcoor))/self.track_in.lx)
        yi = int((self.pos[1]*(self.world_in.pixels-9)+(4*self.track_in.max_Ycoor-(self.world_in.pixels-5)*self.track_in.min_Ycoor))/self.track_in.ly)
        if self.world_in.Space[xi,yi]==0:
            self.world_in.Space[xi,yi]=a
    
    def sensor_f(self,min_l):
        a = 0
        f = np.zeros(2)
        f[0] = self.pos[0]
        f[1] = self.pos[1]
        touch =  False
        while touch == False:
            if self.sense_world(f[0],f[1]) == 0 or self.sense_world(f[0],f[1]) == self.id:
                a+=2.*min_l
                extend_line(f,self.ori,min_l)
            else:
                 touch = True
        self.sensor[0] = a
        return a

    def sensor_rc(self,min_l):
        a = 0
        rc =np.zeros(2)
        rc[0] = self.pos[0]
        rc[1] = self.pos[1]
        touch =  False
        while touch == False:
            if self.sense_world(rc[0],rc[1]) == 0 or self.sense_world(rc[0],rc[1]) == self.id:
                a+=2.*min_l
                extend_line(rc,self.ori-np.pi/4.,min_l)
            else:
                 touch = True
        self.sensor[1] = a
        return a

    def sensor_lc(self,min_l):
        a = 0
        lc = np.zeros(2)
        lc[0] = self.pos[0]
        lc[1] = self.pos[1]
        touch =  False
        while touch == False:
            if self.sense_world(lc[0],lc[1]) == 0 or self.sense_world(lc[0],lc[1]) == self.id:
                a+=2.*min_l
                extend_line(lc,self.ori+np.pi/4.,min_l)
            else:
                 touch = True
        self.sensor[2] = a
        return a
    def sensor_r(self,min_l):
        a = 0
        r = np.zeros(2)
        r[0] = self.pos[0]
        r[1] = self.pos[1]
        touch =  False
        while touch == False:
            if self.sense_world(r[0],r[1]) == 0 or self.sense_world(r[0],r[1]) == self.id:
                a+=2.*min_l
                extend_line(r,self.ori-np.pi/2.,min_l)
            else:
                 touch = True
        self.sensor[3] = a
        return a

    def sensor_l(self,min_l):
        a = 0
        l = np.zeros(2)
        l[0] = self.pos[0]
        l[1] = self.pos[1]
        touch =  False
        while touch == False:
            if self.sense_world(l[0],l[1]) == 0 or self.sense_world(l[0],l[1]) == self.id:
                a+=2.*min_l
                extend_line(l,self.ori+np.pi/2.,min_l)
            else:
                 touch = True
        self.sensor[4] = a
        return a

    def sensor_fill(self,min_l):
        self.sensor_f(min_l)
        self.sensor_rc(min_l)
        self.sensor_lc(min_l)
        self.sensor_r(min_l)
        self.sensor_l(min_l)
        self.sensor[5] = self.vel

    def move(self,dir,deltaT):
        self.map(0)
        self.ori += dir[0]*deltaT
        self.ori = math.fmod(self.ori,2*np.pi)
        self.vel += dir[1]*deltaT
        self.pos[0] += (self.vel) *deltaT* np.cos(self.ori)
        self.pos[1] += (self.vel) *deltaT* np.sin(self.ori)
        self.map(self.id)