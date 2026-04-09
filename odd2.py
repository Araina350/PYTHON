def Twoodd(arr, size):
    xorof = arr[0]
    x = 0
    y = 0 
    setbit = 0
    for i in range(1, size):
        xorof = xorof ^ arr[1]
    setbit = xorof & ~(xorof - 1)
