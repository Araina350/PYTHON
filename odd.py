def OddOcurrence(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res
arr = []
n = int(input("Enter your array size"))
while(n):
    num = int(input("Enter one of your numbers")) 
    arr.append(num)
    n-=1
print("\n\nOdd occuring number = ",OddOcurrence(arr))       