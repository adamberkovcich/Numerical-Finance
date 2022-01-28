from PseudoGenerator import*

class LinearCongruential(PseudoGenerator):
    
    def __init__(self, seed, multiplier, increment, modulus):
        
        super(LinearCongruential, self).__init__(seed, seed) #seed, currentNumber
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
    
    def GetcurrentNumber(self):
        return self.currentNumber
        
    def Generate(self):
        
        self.currentNumber = (self.multiplier * self.currentNumber + self.increment) % self.modulus
        return self.currentNumber / self.modulus


