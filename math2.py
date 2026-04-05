from math import sqrt
math22 = int(input("Enter a number: "))
if math22 > 1:
    for i in range(2, int(sqrt(math22))+1):
        if math22 % i == 0:
            print(math22, " is a composite number")
            break
    else:
        print(math22, " is a prime number")
else:
    print("It is not a prime number")      