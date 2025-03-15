#!/usr/bin/python3.13
import sys

input = sys.argv[1]
control = True
fildata = []
total = {}

wfile = open(input, "r")

while (control):
    line = wfile.readline()
    if not line:
        control = False
        continue
    elif (line[0] == 'f'):
        continue
    elif (line[0].isspace()):
        continue

    comp = line.split("|")
    try:
        float(comp[4])    
        nline = comp[3]
        
        #Total salary dictionary
        if comp[3] not in total:
            total.update({comp[3]: float(comp[4])})
        else:
            total[comp[3]] = total[comp[3]] + float(comp[4])
        
        #To populate frequency dictionary
        fildata.append(nline)
    except:
     continue

fildata.sort()

#I could probably combine this into one dictionary if I really wanted to but I'm not taking the time right now to make that work
count = {i:fildata.count(i) for i in fildata}

for i in count:
    print(f"   The average {i} gets payed {total[i] / count[i]:.2f} dollars an hour.")
    
wfile.close()
