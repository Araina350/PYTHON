def sum_n(n):
    return n*(n+1)//2
print("Sum of first n numbers(n=5):",sum_n(5))


def array_sum(a):
    total=0
    for i in a:
        total += i
    return total
a=[12, 3, 4, 67]    
print ("Array sum:",array_sum(a))