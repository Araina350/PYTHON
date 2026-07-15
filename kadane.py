nums = [1,-2,5,10,8,-17,5,6,-8,24]
print("Full array: ",nums)
print("Subarrays and their sums")
print("[0:3] = ",nums[0:3],"Sum = ", sum(nums[0:3]))
print("[3:6] = ",nums[3:6],"Sum = ", sum(nums[3:6]))
print("[6:11] = ",nums[6:11],"Sum = ", sum(nums[6:11]))
print()
print("Running sum trace")
running = 0
for num in nums:
    running += num
    if running < 0:
        print(f"{num} -> sum = {running} <-- Negative! reset to 0")
        running = 0
    else:
       print(f"{num} -> sum = {running}")     

running = 0
best = 0
for num in nums:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print("Array",nums)
print("Max array sum",best)   
print() 