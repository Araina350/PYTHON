def Power4(number):
    count = 0
    if (number &(~(number &(number - 1)))):
        while (number > 1):
            number >>= 1
            count += 1
        if(count % 2 ==0):
            return True
        else:
            return False
    return False    
number = int(input("Enter the number"))
if (Power4(number)):
    print("\nThe number is power of 4")
else:
    print("\nThe number is not power of 4")            