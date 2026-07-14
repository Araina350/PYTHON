binary = [1,1,0,0,1,0,1,0,1,1,1,1]
streak = 0
for num in binary:
    if num == 0 :
        streak = 0
    else :
        streak = streak + 1
    print(num," -> ",streak)        

streak = 0
best = 0
for num in binary:
    if num == 0 :
        streak = 0
    else :
        streak = streak + 1
    if best < streak:
        best = streak
print("Binary array: ",binary) 
print("Max consecutive 1s",best)
print()

nums = [1,0,3,6,0,0,0,2,235,0,72]
print("Before",nums)
zero = 0
for nonzero in range(len(nums)):
    if nums[nonzero] != 0:
        nums[nonzero],nums[zero] = nums[zero], nums[nonzero]
        zero += 1
print("After: ", nums)    

print("Write pointer stopped at",zero)
print("Non-Zeros at front"        , zero)
print("Zeros at end: ",len(nums)- zero)