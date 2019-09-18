import numpy as np
import math
import car as c

class Driver:
    def __init__(self,car):
        self.dec = np.random.randn(6,2)
        self.dir = np.zeros(2)
        self.car_in = car
        self.crash = False

    def check_crash(self):
        if self.car_in.sense_world(self.car_in.pos[0],self.car_in.pos[1]>0) and self.crash==False:
            self.crash = True

    def drive(self,deltaT):
        self.check_crash()
        if self.crash == False:
            self.car_in.sensor_fill()
            self.dir = np.matmul(self.car_in.sensor,self.dec)
            self.car_in.move(self.dir,deltaT)
        if self.crash==True:
            print("Car %d has crashed" %self.car_in.id)