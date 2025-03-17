#!/usr/bin/python3
import sys

def palindrome(clist, rlist, index):
    
    if (index < len(clist)) and (clist[index] == rlist[index]):
        
        index = index + 1
        return palindrome(clist, rlist, index)
    
    elif (index < len(clist)) and (clist[index] != rlist[index]):
        return False
    
    else:
        return True


if __name__ == '__main__':
    arg = sys.argv[1]

    try:
        if(palindrome(list(arg), list(reversed(arg)), 0)):
            print("Palindrome")
        else:
            print("Not Palindrome")
    except TypeError:
        print(TypeError)
        
            
            

