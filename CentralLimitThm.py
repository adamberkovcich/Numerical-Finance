from NormalGenerator import *
from EcuyerCombined import *

class CentralLimitThm(NormalGenerator):
    
    def __init__(self, gen):
        super(CentralLimitThm, self).__init__(0)
        self.gen = gen
    
    def Generate(self):
        somme = sum([self.gen.Generate() for i in range(12)])
        result = somme - 6
        self.currentNumber = result
       
        return result