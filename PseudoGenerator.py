from UniformGenerator import*

class PseudoGenerator(UniformGenerator):
    
    def __init__(self, seed, currentNumber):
        super(PseudoGenerator, self).__init__()
        self.seed = seed
        self.currentNumber = currentNumber
        
    def GetcurrentNumber(self):
        return self.currentNumber
