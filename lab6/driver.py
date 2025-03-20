#!/usr/bin/python3.13
from shapes import *
import sys

if __name__ == "__main__":
    try:
        file = open(sys.argv[1])
    except:
        raise Exception("That is not a file, please provide a file.")

    for i in file:
        
        i.strip('\n')
        shape = i.strip("\n")
        shape = shape.split(" ")
        
        try:
            
            if (shape[0] == "P"):
                exe = Point(shape[1])
                exe.draw()
            elif (shape[0] == "D"):
                exe = Diamond(shape[1], int(shape[2]))
                exe.draw()
            elif (shape[0] == "R"):
                exe = Rectangle(shape[1], int(shape[2]), int(shape[3]))
                exe.draw()
            elif (shape[0] == "S"):
                exe = Square(shape[1], int(shape[2]))
                exe.draw()
            elif (shape[0] == "T"):
                exe = Triangle(shape[1], int(shape[2]))
                exe.draw()
            else:
                print(f"Couldn't find a matching shape.")
                print(f"Valid shapes are, (P)oint, (D)iamond, (R)ectangle, (S)quare, and (T)riangle.")
                print(f"The given input was {shape[0]}")
        
        except:
            raise Exception(f"The shape {shape}, was formated incorrectly.")
        
    file.close()
