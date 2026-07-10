def min_element(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp,a[i]) 
    return temp
def max_element(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp,a[i]) 
    return temp   
a = [12234,234567,54636,12235] 
size = len(a)
print("Minimum ",min_element(a,size))
print("Maximum ",max_element(a,size))