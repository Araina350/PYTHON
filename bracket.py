def parens(s,l,r,p,n):
    if(p == 2*n):
        for ss in s:
            print(ss,end=" ") 
        print("\n")
        return
    if (l>r):
        s[p] = "}"
        parens(s,l,r+1,p+1,n)    
    if(l<n):
        s[p] = "{"   
        parens(s,l+1,r,p+1,n)  
n = int(input("Enter number of curly brackets"))
s = [" "] * 2 * n 
print("\n")
parens(s,0,0,0,n)       