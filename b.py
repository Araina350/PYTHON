def SetorNot(number, n):
    if number &(1 << (n - 1)):
        print("\nSet")
    else:
        print("\nNot Set")
number = int(input("Enter your number"))  
n = int(input("Enter the bit")) 
SetorNot(number,n)
