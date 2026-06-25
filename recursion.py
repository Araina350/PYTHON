print("Dream recursion")
print("Two rules of recursion: ")
print("1.Call yourself with a smaller function ")
print("Have a BASE CASE that stops the calls")
print()
def count_up(n):
    if n > 10:
        return
    print(n, end=" ")
    count_up(n+1)
print("Numbers till ten")
count_up(1)
print()
print()    
def countdown(n):
    if n == 0:
        return
    print(n, end=" ")
    countdown(n-1)
print("Countdown time!!!!!!!!!! ")    
countdown(5)
print()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print("Factorials:")
print("factorial(5)=", factorial(5))   
print("factorial(4)=", factorial(4))   
print("factorial(1)=", factorial(1))   
print("factorial(0)=", factorial(0))  


import sys
print("Recursion limit",sys.getrecursionlimit())
def no_base_case(n):
    print("Call",n,end=" ")
    no_base_case(n + 1)
sys.setrecursionlimit(30)
try:
    no_base_case(1)
except RecursionError:
    print()
    print("fvffdlifjeljf")
sys.setrecursionlimit(1000)
print("Important rule: Include a Base Case in a recursive function")