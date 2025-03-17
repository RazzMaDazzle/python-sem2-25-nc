#!/usr/bin/python3
import sys

def factorial1(inp):
    prod = 1
    for i in range(1, inp + 1):
        prod = prod * i
    return prod

def factorial2(inp):
    if (inp == 1): return 1 
    return inp * factorial2(inp -1)

def control(arg, arg1):
    ans = 0
    if arg == 'iterative':
        ans = factorial1(arg1)
    elif arg == 'recursive':
        ans = factorial2(arg1)
    else:
        raise Exception("Invalid approach, please enter a valid approach.")
    print(ans)


if __name__ == '__main__':
    arg = sys.argv[1]
    arg1 = sys.argv[2]

    try:
        control(arg, int(arg1))
    except:
       print("Please enter a number.")
    
            
            

