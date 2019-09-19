import numpy as np

class World:
    def __init__(self,pixels):
        self.Space = np.zeros((pixels,pixels),dtype=int)
        self.pixels = pixels
        # i = 0 -> Nothing
        # i = 1 -> Track
        # i >= 5 -> c_id