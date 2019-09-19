import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
import numpy as np
import math
import os

test = False
n_samples = 20
l_min = 0.6

def generate_track(l_min):      #l_min between 0 - 1 (avoid <~ 0.001)
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

    resolution_points = 200

    draw = np.linspace(np.pi,3.*np.pi,8*resolution_points)

    vi_x = poly_x_inner.derivative()(draw)
    vi_y = poly_y_inner.derivative()(draw)
    vo_x = poly_x_outer.derivative()(draw)
    vo_y = poly_y_outer.derivative()(draw)

    length_I = np.trapz(np.sqrt(vi_x**2. + vi_y**2.))
    resolution_I = int(4*resolution_points*(1.-l_min))
    #print resolution_I
    s_I = np.linspace(0,length_I,resolution_I)

    length_O = np.trapz(np.sqrt(vo_x**2. + vo_y**2.))
    resolution_O = int((length_O/length_I)*4*resolution_points*(1.-l_min))
    #print resolution_O
    s_O = np.linspace(0,length_O,resolution_O)

    theta_I = []
    theta_O = []

    for i in range(resolution_I):
        for j in range(8*resolution_points):
            if np.trapz(np.sqrt(vi_x[:j]**2. + vi_y[:j]**2.)) >= s_I[i]:
                theta_I.append(draw[j])
                break
    for i in range(resolution_O):
        for k in range(8*resolution_points):
            if np.trapz(np.sqrt(vo_x[:k]**2. + vo_y[:k]**2.)) >= s_O[i]:
                theta_O.append(draw[k])
                break

    track_i_x = poly_x_inner(theta_I)
    track_i_y = poly_y_inner(theta_I)
    track_o_x = poly_x_outer(theta_O)
    track_o_y = poly_y_outer(theta_O)

    points = []
    for i in range(resolution_I-1):
        points.append([track_i_x[i],track_i_y[i]])
    for i in range(resolution_O-1):
        points.append([track_o_x[i],track_o_y[i]])
    
    return np.array(points)

if test == True:
    points = lane(0.7)
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i,0])
        y.append(points[i,1])
    plt.plot(x,y,'o')
    plt.show()

if not os.path.exists('samples'):
    os.makedirs('samples')

for n in range(n_samples):
    print (n)
    np.save("samples/track_"+str(n)+"_l_min_"+str(l_min)+".npy",generate_track(l_min))

def lane_square(min_l):
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
