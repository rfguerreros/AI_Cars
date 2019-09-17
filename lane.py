import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np
import math

def lane(resolution):
    resolution_points = resolution
    n_points = 15     #2*pi/n_points

    if n_points%2 == 0:
        n_points += 1

    theta = np.linspace(0.,4.*np.pi,n_points)

    x = []
    y = []

    for i in range(n_points):
        x.append(np.cos(4.*np.pi*i/n_points))
        y.append(np.sin(4.*np.pi*i/n_points))

    x = np.array(x)
    y = np.array(y)

    x = x + 0.7*np.random.random_sample((n_points))
    y = y + 0.7*np.random.random_sample((n_points))

    for i in range(int(n_points*0.5),n_points):
        x[i] = x[i-int(n_points*0.5)]
        y[i] = y[i-int(n_points*0.5)]


    for i in range(n_points):
        x[i] = (np.sqrt(x[i]**2. + y[i]**2.)+1.2)*x[i]/np.sqrt(x[i]**2. + y[i]**2.)
        y[i] = (np.sqrt(x[i]**2. + y[i]**2.)+1.2)*y[i]/np.sqrt(x[i]**2. + y[i]**2.)

    x_inner = np.copy(x)
    y_inner = np.copy(y)

    for i in range(n_points):
        x_inner[i] = (np.sqrt(x[i]**2. + y[i]**2.)+1.8)*x[i]/np.sqrt(x[i]**2. + y[i]**2.)
        y_inner[i] = (np.sqrt(x[i]**2. + y[i]**2.)+1.8)*y[i]/np.sqrt(x[i]**2. + y[i]**2.)

    poly_x_inner = CubicSpline(theta, x_inner)
    poly_y_inner = CubicSpline(theta, y_inner)

    poly_x_outer = CubicSpline(theta, x)
    poly_y_outer = CubicSpline(theta, y)

    draw = np.linspace(np.pi,3.*np.pi,resolution_points)

    track_i_x = poly_x_inner(draw)
    track_i_y = poly_y_inner(draw)
    track_o_x = poly_x_outer(draw)
    track_o_y = poly_y_outer(draw)

    points = []
    for i in range(resolution):
        points.append([track_i_x[i],track_i_y[i]])
        points.append([track_o_x[i],track_o_y[i]])
    
    return np.array(points)

points = lane(600)
x = []
y = []
for i in range(1200):
    x.append(points[i,0])
    y.append(points[i,1])
plt.plot(x,y,'o')
plt.show()


""" 
def lane(min_l):
    x_min_o = 0
    x_max_o = 5

    x_min_i = 1
    x_max_i = 4

    y_min_o = 0
    y_max_o = 5

    y_min_i = 1
    y_max_i = 4

    base_o_x = np.arange(x_min_o,x_max_o+min_l,min_l)
    base_o_x_d = np.c_[base_o_x,np.ones(len(base_o_x))*y_min_o]
    base_o_x_u = np.c_[base_o_x,np.ones(len(base_o_x))*y_max_o]
    base_o_y = np.arange(y_min_o,y_max_o+min_l,min_l)
    base_o_y_l = np.c_[np.ones(len(base_o_y))*x_min_o,base_o_y]
    base_o_y_r = np.c_[np.ones(len(base_o_y))*x_max_o,base_o_y]

    base_i_x = np.arange(x_min_i,x_max_i+min_l,min_l)
    base_i_x_d = np.c_[base_i_x,np.ones(len(base_i_x))*y_min_i]
    base_i_x_u = np.c_[base_i_x,np.ones(len(base_i_x))*y_max_i]
    base_i_y = np.arange(y_min_i,y_max_i+min_l,min_l)
    base_i_y_l = np.c_[np.ones(len(base_i_y))*x_min_i,base_i_y]
    base_i_y_r = np.c_[np.ones(len(base_i_y))*x_max_i,base_i_y]

    return np.concatenate((base_o_x_d,base_o_x_u,base_o_y_l,base_o_y_r,base_i_x_d,base_i_x_u,base_i_y_l,base_i_y_r),axis=0)
 """