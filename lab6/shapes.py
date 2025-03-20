class Point:
    _symbol = "*"
    
    def __init__(self, symbol="."):
        self._symbol = symbol

    def setSymbol(self, new):
        self._symbol = new

    def draw(self):
        print(self._symbol)

class Rectangle(Point):

    def __init__(self, symbol="#", Lsize=3, Wsize=3):
        super().__init__(symbol)
        self._Lsize = Lsize
        self._Wsize = Wsize

    def draw(self):
        for h in range(self._Lsize):
            for w in range(self._Wsize):
                print(self._symbol, end="")
            print("")

class Triangle(Point):

    def __init__(self, symbol="#", base=3):
        super().__init__(symbol)
        self._base = base

    def draw(self):
        self._count = 1
        for h in range(self._base):
            for w in range(self._count):
                print(self._symbol, end="")
            self._count = self._count + 1
            print("")

class Diamond(Point):

    def __init__(self, symbol="#", width=10):
        super().__init__(symbol)
        self._width = width

    def draw(self):
        for h in range(1, (self._width + 1) // 2 + 1):
            for w in range((self._width + 1) // 2 - h):
                print(" ", end="")
            for w2 in range((h * 2) - 1):
                print(self._symbol, end="")
            print()
        for h in range((self._width + 1)//2 + 1, self._width + 1):
            for w3 in range(h - (self._width + 1)//2):
                print(" ", end ="")
            for w4 in range((self._width + 1 - h)*2 - 1):
                print(self._symbol, end="")
            print()

                
class Square(Rectangle):
    def __init__(self, symbol="#", size=3):
        super().__init__(symbol)
        self._size = size

    def draw(self):
        for h in range(self._size):
            for w in range(self._size):
                print(self._symbol, end="")
            print("")

    
