def Same(num1, num2):
    if((num1 ^ num2)!= 0):
        print("Both are not equal")
    else:
        print("Both are equal")
num1 = int(input("Enter the first number"))        
num2 = int(input("Enter the second number")) 
Same(num1, num2)