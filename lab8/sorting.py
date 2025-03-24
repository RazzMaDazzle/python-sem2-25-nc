#!/usr/bin/python3.13
import sys


if __name__ == "__main__":
    
    data = {}
    ids = []

    try:
        file = open(sys.argv[1], "r")
    except:
        raise Exception("That's not a file, please try again.")

    for i in file:

        line = i.strip('\n')
        comp = line.split('|')
        if (line[0] == '#'): continue

        dicti = {}
        
        try:
            dicti["id"] = int(comp[0])
            dicti["name"] = comp[1]
            dicti["country"] = comp[2]
            dicti["species"] = comp[3]
            dicti["class"] = comp[4]
            dicti["level"] = int(comp[5])
        
        except:
            raise Exception("Invalid format.")
        
        data[int(comp[0])] = dicti
        ids.append(int(comp[0]))

    file.close()

    orglist = []
    
    for id in ids:
        age = data[id]["level"]
        temp = (age, id)
        orglist.append(temp)

    orglist.sort()

    print("Here are the people in this list, presented in ascending order by level")
    for tup in orglist:
        print(f"Name: {data[tup[1]]["name"]}, Country: {data[tup[1]]["country"]}, Species: {data[tup[1]]["species"]}, Class: {data[tup[1]]["class"]}, and Level: {data[tup[1]]["level"]}.")





