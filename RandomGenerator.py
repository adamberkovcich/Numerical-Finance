from abc import abstractmethod
import numpy as np

class RandomGenerator:
    
    def __init__(self): #ctor
        pass
    
    @abstractmethod
    def Generate(self):
        pass
    
    def Mean(self, nbSim):
        return sum([self.Generate() for i in range(nbSim)]) / nbSim
    
    def Variance(self, nbSim):
        mean = self.Mean(nbSim)
        return sum([(self.Generate() - mean)**2 for i in range(nbSim)]) / (nbSim - 1)


