number = int(input("Enter your number: "))
ognumber = number
reversenum = 0
while number > 0:
    digit = number % 10
    reversenum = reversenum * 10 + digit
    number //= 10
if ognumber == reversenum:
    print("It is a palindrome")
else:
    print("It is not a palindrome")        