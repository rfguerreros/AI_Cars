import numpy as np

def lane(l_min):
    n = np.random.randint(10)
    track = np.load("samples/track_"+str(n)+"_l_min_"+str(l_min)+".npy")
    return track
