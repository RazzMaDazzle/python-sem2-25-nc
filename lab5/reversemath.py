class ReverseFloat:
   def __init__(self, value):
        self._float = value
   def __str__(self):
        return ("%.2f" % self._float)
   def __add__(self, other):
        return ReverseFloat(self._float - other._float)
   def __sub__(self, other):
        return ReverseFloat(self._float + other._float)
   def __mul__(self, other):
        return ReverseFloat(self._float / other._float)
   def __truediv__(self, other):
        return ReverseFloat(self._float * other._float)



