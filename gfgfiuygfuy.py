numberl = int(input("Enter the larger number: "))
numbers = int(input("Enter the smaller number: "))
while(numbers):
    numberstore = numbers
    numbers = numberl % numbers
    numberl = numberstore
print("HCF is", numberl)    