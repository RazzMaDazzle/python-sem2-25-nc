#!/usr/bin/python3

from why import Random

if __name__ == "__main__":
    ran1 = Random("help", "me")
    ran2 = Random("it's", "cold")

    print(f"The first two attributes are {ran1.naccess} and {ran1.faccess}")
    print(f"The first two attributes for the second instance are {ran2.naccess} and {ran2.faccess}")
    
    ran1.naccess = input("Enter a value for the first attribute: ")
    ran1.faccess = input("Enter a value for the second attribute: ")

    print(f"The first two attributes are now {ran1.naccess} and {ran1.faccess}")
    print(f"The first two attributes for the second instance are still {ran2.naccess} and {ran2.faccess}")

    ran2.naccess = input("Enter a value for the first attribute in the second instance: ")
    ran2.faccess = input("Enter a value for the second attribute in the second instance: ")

    
    print(f"The first two attributes are still {ran1.naccess} and {ran1.faccess}")
    print(f"While the first two attributes for the second instance have changed to {ran2.naccess} and {ran2.faccess}")



