#!/usr/bin/python3.13
import sys

input = sys.argv[1]
control = True
fildata = [] 

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
        int(comp[2])
        nline = comp[2] + "|" + comp[1] 
        fildata.append(nline)
    except:
        continue

fildata.sort()
for i in fildata:
    nline = i.split("|")
    print(f"  {nline[1]}")

wfile.close()
