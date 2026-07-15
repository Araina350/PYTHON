stock = [10,20,156,12345,6565,7676]
profit = 0
for i in range(len(stock)):
    if stock[i]>stock[i-1]:
       profit += stock
print("Stock prices = ",stock)
