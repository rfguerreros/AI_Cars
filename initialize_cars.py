import numpy as np
import random as rand
import math
import car as c
import track as t


def initialize_car(cars,seed):
    rand.seed(seed)
    total_cars= np.size(cars)
    for jj in range(total_cars):
        pixels=cars[jj].world_in.pixels
        world=cars[jj].world_in
        t.map(cars[jj].track_in,cars[jj].world_in,cars[jj].world_in.pixels)
        x0=rand.randint(0,pixels-1)
        print(x0)
        y1=0
        while(world.Space[x0,y1]==0):
            y1+=1
            
        print(y1)    
        i=y1
        while(world.Space[x0,i]==1):
            i+=1
        
        y1=i
        y2=y1
        while(world.Space[x0,y2]==0):
            y2+=1
        print(y2)
        y4=pixels-1
        while(world.Space[x0,y4]==0):
            y4-=1

        i=y4
        while(world.Space[x0,i]==1):
            i-=1
        
        y4=i
        y3=y4
        print(y4)
        while(world.Space[x0,y3]==0):
            y3-=1
        print(y3)
        
        a=rand.randint(0,1)
        if(a==0):
            y0=rand.randint(y1,y2)
        else:
            y0=rand.randint(y3,y4)
        print(x0,y0)
        print(pixels)
        xmax=cars[jj].track_in.max_Xcoor
        xmin=cars[jj].track_in.min_Xcoor
        ymax=cars[jj].track_in.max_Ycoor
        ymin=cars[jj].track_in.min_Ycoor
        lx=xmax-xmin
        ly=ymax-ymin
    
        pos_x=(lx*x0-(4*xmax-(pixels -5)*xmin))/(pixels-9)
        pos_y=(lx*y0-(4*ymax-(pixels -5)*ymin))/(pixels-9)
        cars[jj].pos=np.array([pos_x,pos_y])
        print(cars[jj].pos)
    return 0    


