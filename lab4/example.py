
class Example:
    def __init__(self, arg1, arg2):
        self._ex1 = arg1
        self._ex2 = arg2

    def getsum(self): return self._ex1 + self._ex2

    def setex1(self, set): self._ex1 = set
    
    def getprod(self): return self._ex2 * self._ex1

    def setex2(self, set): self._ex2 = set
    
    ex3 = property(getsum, setex1)

    ex4 = property(getprod, setex2)

    
    
