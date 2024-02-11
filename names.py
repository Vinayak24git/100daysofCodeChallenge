names = [] #list to gather my data

with open("names.txt") as file:  #reading eachline, striping off the new line 
    for line in file:
        names.append(line.rstrip()) #& adding the names to the list
        
        
for name in sorted(names): #sort all the names alphabetically
    print(f"hello, {name}")#print the names