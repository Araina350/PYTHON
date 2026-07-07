n = int(input("Enter a number "))
temp = n
while temp > 0:
    print("last digit", temp % 10, "remaining numbers", temp // 10)
    temp = temp // 10
print()

def flip_number(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flip_number(num // 10)
    return last * pow(10,len(str(rest))) + rest
n2 = int(input("Enter a number"))
print(n2, "flipped ->",flip_number(n2))
print()

def flip_name(s):
    if len(s) == 1:
        return s
    return flip_name(s[1:]) + s[0]
name = input("Enter your name: ")
print(name, "Flipped ->",flip_name(name))
print()

def Pow4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return Pow4(n//4)
    return False
print(" 16 ->", Pow4(16), "12 ->",Pow4(12))
guess = int(input("Try ur own number"))
print(guess, "-> Power of 4? ", Pow4(guess))