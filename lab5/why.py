class Random:
    def __init__(self, input, input2):
        self._fname = input2
        self._name = input
    def setFname(self, inp):
        self._fname = inp
    def setName(self, inp):
        self._name = inp
    def getName(self):
        return self._name
    def getFname(self):
        return self._fname

    faccess = property(getFname, setFname)
    naccess = property(getName, setName)
