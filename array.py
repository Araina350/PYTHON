import array as arr
def Mean(arr, arrSize):
    total_sum = 0
    for i in range(0, arrSize):
        total_sum += arr[i]
    return(total_sum/arrSize)  
def Median(arr,arrSize):
    sorted(arr)
    if arrSize % 2 != 0:
        return float(arr[int(arrSize/2)]) 
    return float((arr[int((arrSize-1)/2)] + arr[int(arrSize/2)])/2.0)
arr = [12,67,34,400,500,29]
arrSize = len(arr)
print("Mean = ", Mean(arr,arrSize))
print("Median = ", Median(arr,arrSize))