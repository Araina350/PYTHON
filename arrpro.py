stock = [100,180,400,590,625,980]
profit = 0
for i in range(1,len()):
    if stock[i]>stock [i-1]:
        profit += stock[i] - stock[i-1]
print("Stock Prices",stock )  
print("Maximum profit", profit) 
heights = [0,1,0,2,1,0,1,3,2,1,2]
n = len(heights)  
left_tallest = [0] * n
left_tallest[0] = heights[0] 
for i in range(1,n):
    left_tallest[i] = max(left_tallest[i - 1],heights[i])
print("heights", heights)   
print("left_tallest",left_tallest)
right_tallest = [0] * n
right_tallest[n-1] = heights[n-1]
for i in range(n-2,-1,-1):
        right_tallest[i] = max(right_tallest[i + 1],heights[i])
print("heights", heights)   
print("right_tallest",right_tallest)
water = 0
for i in range(n):
    water += min(left_tallest[i],right_tallest[i]) - heights[i]
print("Total water trapped",water)    