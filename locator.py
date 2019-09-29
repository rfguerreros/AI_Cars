import numpy as np

def locate_cars(world, dire, car):
    a = np.random.randint(0,100)
    i=1
    foundl = False
    foundr = False
    xi = 0
    xf = 0
    if(dire == 0):
        while (foundl == False or foundr == False) and i <world.pixels:
            if world.Space[a,i-1] == 1 and world.Space[a,i] == 0:
                xi = i
                foundl = True
            if world.Space[a,i-1] == 0 and world.Space[a,i] == 1 and foundl == True:
                xf = i
                foundr=True
            i+=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if check_surr(a,xm,world) == True:
                world.Space[a,xm] = 2
                return True
            else:
                return False
        else:
            return False
    elif (dire == 1):
        while (foundl == False or foundr == False) and i <world.pixels:
            if world.Space[i-1,a] == 1 and world.Space[i,a] == 0:
                xi = i
                foundl = True
            if world.Space[i-1,a] == 0 and world.Space[i,a] == 1 and foundl == True:
                xf = i
                foundr=True
            i+=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if check_surr(xm,a,world) ==True:
                world.Space[xm,a] = 2
                return True
            else:
                return False
        else:
            return False
    elif (dire == 2):
        i = world.pixels - 1
        while (foundl == False or foundr == False) and i >0:
            if world.Space[a,i-1] == 0 and world.Space[a,i] == 1:
                xf = i
                foundl = True
            if world.Space[a,i-1] == 1 and world.Space[a,i] == 0 and foundl == True:
                xi = i
                foundr=True
            i-=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if check_surr(a,xm,world) == True:
                world.Space[a,xm] = 2
                return True
            else:
                return False
        else:
            return False
    elif (dire == 3):
        i = world.pixels - 1
        while (foundl == False or foundr == False) and i >0:
            if world.Space[i-1,a] == 0 and world.Space[i,a] == 1:
                xf = i
                foundl = True
            if world.Space[i-1,a] == 1 and world.Space[i,a] == 0 and foundl == True:
                xi = i
                foundr=True
            i-=1
        if(xi+20<xf and foundl == True and foundr == True):
            xm = np.random.randint(xi+1,xf-1)
            if(check_surr(xm,a,world)==True):
                world.Space[xm,a] = 2
                return True
            else:
                return False
        else:
            return False

def check_surr(a,xm, world):
    b = 0
    for ii in range(a-3,a+4):
        for jj in range(xm-3,xm+4):
            b+=world.Space[ii,jj]
    if b==0:
        return True
    else:
        return False