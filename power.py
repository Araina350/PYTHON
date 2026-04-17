import math
def powerSet(set, SetSize):
    powerSetSize = (int) (math.pow(2,SetSize))
    inner = 0 
    outer = 0
    for outer in range(0,powerSetSize):
        for inner in range(0,SetSize):
            if((outer &(1 << inner)) > 0):
                print(set[inner], end = " ")
        print("")        
size = int(input("Enter your array size "))
set = []
for i in range(0, size):
    n = int(input("Enter your values"))
    set.append(n)
print(powerSet(set,len(set)))    

