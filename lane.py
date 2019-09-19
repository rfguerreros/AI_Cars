import numpy as np
import os

def lane(l_min):
    n = np.random.randint(40)

    if not os.path.exists('samples'):
        print("Missing track samples. Please run track_gen.py")

    track = np.load("samples/track_"+str(n)+"_l_min_"+str(l_min)+".npy")
    return track
