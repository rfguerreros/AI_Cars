import numpy as np
import math

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
