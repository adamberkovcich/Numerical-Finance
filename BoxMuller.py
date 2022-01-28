from NormalGenerator import *
from EcuyerCombined import *

import numpy as np

class BoxMuller(NormalGenerator):
    
    def __init__(self, gen):
        super(BoxMuller, self).__init__(0)
        self.gen = gen
        
    
    def Generate(self):
        
        U1 = self.gen.Generate()
        U2 = self.gen.Generate()
        
        R = np.sqrt(-2 * np.log(U1))
        O = 2 * np.pi * U2
        
        X = R * np.cos(O)
        Y = R * np.sin(O)
        
        return X
        
        