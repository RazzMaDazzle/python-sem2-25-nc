#!/usr/bin/python3

import sys
from example import Example

if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    
    example1 = Example(int(arg1), int(arg2))
    example2 = Example(int(arg1), int(arg2))
    
    print(f"The sum of ex1 and ex2 in example1: {example1.ex3}")
    print(f"The product of ex1 and ex2 in example2: {example2.ex4}")
    print()
    
    example1.ex3 = int(input("Please enter new a new value for ex1 by setting ex3: "))
    example1.ex4 = int(input("Please enter new a new value for ex2 by setting ex4: "))

    print()
    print(f"The sum of ex1 and ex2 in example1 is now: {example1.ex3}")
    print(f"The product of ex1 and ex2 in example2 is still: {example2.ex4}")
