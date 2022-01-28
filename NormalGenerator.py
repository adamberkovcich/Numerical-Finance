from ContinuousGenerator import*

class NormalGenerator(ContinuousGenerator):
    
    def __init__(self, currentNumber):
        super(NormalGenerator, self).__init__()
        self.currentNumber = currentNumber
    
    def GetcurrentNumber(self):
        return self.currentNumber

