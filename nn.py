nnn = int(input("Enter the number"))
nodigits = len(str(nnn))
resultNumber = 0
temp = nnn
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** nodigits
    temp //=10
if nnn == resultNumber:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")     