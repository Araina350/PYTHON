def NumberOfBits(n):
    zeroes = 0
    ones = 0
    while n:
        if(n&1 == 1):
            ones+=1
        else:
            zeroes+=1
        n>>= 1       
    print("\n\nOnes = ",ones,"\nzeroes ",zeroes) 
number = int(input("Enter your number"))
NumberOfBits(number)