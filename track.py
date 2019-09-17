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

def map(track,world,pixels):
    for i in range(len(track.lane)):
        xi = int((track.lane[i,0] - track.min_Xcoor) * (pixels-3)/track.lx)+1
        yi = int((track.lane[i,1] - track.min_Ycoor) * (pixels-3)/track.ly)+1
        world.Space[xi,yi] = 1
        world.Space[xi+1,yi] = 1
        world.Space[xi,yi+1] = 1
        world.Space[xi-1,yi] = 1
        world.Space[xi,yi-1] = 1