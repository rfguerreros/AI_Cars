import numpy as np
import math
import car as c

class Driver:
    def __init__(self,car,network):
        self.brain = network
        self.dir = np.zeros(2)
        self.car_in = car
        self.crash = False
        self.arc = 0
        self.death = False
        print("Driver in car %i created." %self.car_in.id)
    
    def __del__(self):
        print("Driver in car %i deleted." %self.car_in.id)

    def check_crash(self):
        if self.car_in.sense_world(self.car_in.pos[0],self.car_in.pos[1])!=0 and self.car_in.sense_world(self.car_in.pos[0],self.car_in.pos[1])!=self.car_in.id and  self.crash==False:
            self.crash = True

    def drive(self,deltaT,min_l):
        self.check_crash()
        if self.crash == False:
            a0 = np.arctan2(self.car_in.pos[1],self.car_in.pos[0])
            self.car_in.sensor_fill(min_l)
            self.dir = self.brain.decide(self.car_in.sensor)
            self.car_in.move(self.dir,deltaT)
            a1 = np.arctan2(self.car_in.pos[1],self.car_in.pos[0])
            self.arc += a1-a0
        if self.crash == True and self.death == False:
            print("Car %i has crashed." %self.car_in.id)
            self.death = True
    
    def out_brain(self):
        return self.brain