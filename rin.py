def romantoint(romanInput):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    resultInt = 0
    for i in range(0,len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInt -= roman[romanInput[i]]
        else:
            resultInt += roman[romanInput[i]]    
    return  resultInt + roman[romanInput[-1]]  
roman = input("Enter roman numeral")
print("Integer equivalent: ",romantoint(roman))