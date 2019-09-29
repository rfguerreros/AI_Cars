import numpy as np
import car as c


def locate_cars(dire, car):
    a = np.random.randint(0,100)
    i=1
    foundl = False
    foundr = False
    xi = 0
    xf = 0
    if(dire == 0):
        while (foundl == False or foundr == False) and i <car.world_in.pixels:
            if car.world_in.Space[a,i-1] == 1 and car.world_in.Space[a,i] == 0:
                xi = i
                foundl = True
            if car.world_in.Space[a,i-1] == 0 and car.world_in.Space[a,i] == 1 and foundl == True:
                xf = i
                foundr=True
            i+=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if check_surr(a,xm,car) == True:
                find_coordinates(a,xm,car)
                car.map(car.id)
                #car.world_in.Space[a,xm] = 2
                return True
            else:
                return False
        else:
            return False
    elif (dire == 1):
        while (foundl == False or foundr == False) and i <car.world_in.pixels:
            if car.world_in.Space[i-1,a] == 1 and car.world_in.Space[i,a] == 0:
                xi = i
                foundl = True
            if car.world_in.Space[i-1,a] == 0 and car.world_in.Space[i,a] == 1 and foundl == True:
                xf = i
                foundr=True
            i+=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if check_surr(xm,a,car) ==True:
                find_coordinates(xm,a,car)
                car.map(car.id)
                #car.world_in.Space[xm,a] = 2
                return True
            else:
                return False
        else:
            return False
    elif (dire == 2):
        i = car.world_in.pixels - 1
        while (foundl == False or foundr == False) and i >0:
            if car.world_in.Space[a,i-1] == 0 and car.world_in.Space[a,i] == 1:
                xf = i
                foundl = True
            if car.world_in.Space[a,i-1] == 1 and car.world_in.Space[a,i] == 0 and foundl == True:
                xi = i
                foundr=True
            i-=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if check_surr(a,xm,car) == True:
                find_coordinates(a,xm,car)
                car.map(car.id)
                #car.world_in.Space[a,xm] = 2
                return True
            else:
                return False
        else:
            return False
    elif (dire == 3):
        i = car.world_in.pixels - 1
        while (foundl == False or foundr == False) and i >0:
            if car.world_in.Space[i-1,a] == 0 and car.world_in.Space[i,a] == 1:
                xf = i
                foundl = True
            if car.world_in.Space[i-1,a] == 1 and car.world_in.Space[i,a] == 0 and foundl == True:
                xi = i
                foundr=True
            i-=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if(check_surr(xm,a,car)==True):
                #car.world_in.Space[xm,a] = 2
                find_coordinates(xm,a,car)
                car.map(car.id)
                return True
            else:
                return False
        else:
            return False

def check_surr(a,xm, car):
    b = 0
    for ii in range(a-3,a+4):
        for jj in range(xm-3,xm+4):
            b+=car.world_in.Space[ii,jj]
    if b==0:
        return True
    else:
        return False

def find_coordinates(xi,yi,car):
    xp = (((xi*car.track_in.lx)-(4.*car.track_in.max_Xcoor-(car.world_in.pixels-5)*car.track_in.min_Xcoor))/(car.world_in.pixels-9.))
    xa = ((((xi+1)*car.track_in.lx)-(4.*car.track_in.max_Xcoor-(car.world_in.pixels-5)*car.track_in.min_Xcoor))/(car.world_in.pixels-9.))
    x = (xp+xa)/2.
    yp = (((yi*car.track_in.ly)-(4.*car.track_in.max_Ycoor-(car.world_in.pixels-5)*car.track_in.min_Ycoor))/(car.world_in.pixels-9.))
    ya = ((((yi+1)*car.track_in.ly)-(4.*car.track_in.max_Ycoor-(car.world_in.pixels-5)*car.track_in.min_Ycoor))/(car.world_in.pixels-9.))
    y = (yp+ya)/2.
    car.pos = np.asarray([x,y])

