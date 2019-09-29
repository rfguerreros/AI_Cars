import numpy as np
import math

class Track:
    def __init__(self,lane):
        self.lane = lane
        self.max_Xcoor = np.max(self.lane[:,0])
        self.max_Ycoor = np.max(self.lane[:,1])
        self.min_Xcoor = np.min(self.lane[:,0])
        self.min_Ycoor = np.min(self.lane[:,1])
        self.lx = self.max_Xcoor - self.min_Xcoor
        self.ly = self.max_Ycoor - self.min_Ycoor
        print("Track created.")

def map(track,world,pixels):
    for i in range(len(track.lane)):
        xi = int((track.lane[i,0]*(pixels-9)+(4*track.max_Xcoor-(pixels-5)*track.min_Xcoor))/track.lx)
        yi = int((track.lane[i,1]*(pixels-9)+(4*track.max_Ycoor-(pixels-5)*track.min_Ycoor))/track.ly)
        world.Space[xi,yi] = 1
        world.Space[xi+1,yi] = 1
        world.Space[xi,yi+1] = 1
        world.Space[xi-1,yi] = 1
        world.Space[xi-1,yi-1] = 1
        world.Space[xi+1,yi-1] = 1
        world.Space[xi+1,yi+1] = 1
        world.Space[xi-1,yi+1] = 1
