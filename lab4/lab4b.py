#!/usr/bin/python3

import sys

class MyMath:
    def __init__(self, arg):
        self._number = arg

    def absolute(self):
        try:
            if int(self._number) >= 0:
                return self._number
            else:
                return int(self._number) * -1
        except:
            pass
        try:
            if float(self._number) >= 0.0:
                return self._number
            else:
                return float(self._number) * -1
        except:
            raise Exception("Please enter a number.")

    def sum(self, count):
        if len(self._number) > count + 1:
            try:
                return self.sum(count + 1) + float(self._number[count])
            except:
                raise Exception("One of the elements was not a number or float.")
        else:
            return float(self._number[count])
    
    def average(self):
        if (type(self._number) == list):
           return self.sum(0) / float(len(self._number))        
        else:
            raise Exception("Please enter a list of numbers or floats.")

if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        wmath = MyMath(sys.argv[1])
        
        print(f"The absolute value of {sys.argv[1]} is {wmath.absolute()}")

    elif len(sys.argv) > 2:
        sys.argv.pop(0)
        wmath = MyMath(sys.argv)
        
        print(f"The average of the list is is {wmath.average()}")


                
            

