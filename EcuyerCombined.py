from PseudoGenerator import *
from LinearCongruential import *

class EcuyerCombined(PseudoGenerator):

    def __init__(self):
        
        PseudoGenerator.__init__(self,0,0)
        self.Generator1 = LinearCongruential(2147483562, 40014, 0, 2147483563)
        self.Generator2 = LinearCongruential(2147483398, 40692, 0, 2147483399)
        self.x1 = self.Generator1.Generate() * 2147483563
        self.x2 = self.Generator2.Generate() * 2147483399

    def Generate(self):
        
        unif1 = self.x1
        unif2 = self.x2

        X = (unif1 - unif2) % (2147483563 - 1)
        
        if X > 0:
            result =  X/2147483563
        else:
            result = (2147483563 - 1) / 2147483563
            
        self.currentNumber = result
        self.Generator1.Generate() * 2147483563
        self.Generator2.Generate() * 2147483399
        self.x1 = self.Generator1.GetcurrentNumber()
        self.x2 = self.Generator2.GetcurrentNumber()

        return result


