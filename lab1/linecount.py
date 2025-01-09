#Control and file variables
count = 0
condition = True
fname = input(f"Please enter a file name to count: ")

#Input handling 
while(condition):
    try:
        f = open(fname, "r")
        condition = False
    except Exception:
        fname = input(f"The name caused an error, {Exception}, please try again: ")

#Line iteration
for i in f:
    count += 1

print(f"The number of lines in the file is {count}")

f.close()
