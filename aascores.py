scores = [310,490,500,190,246]
print("Part1 : HEAD-TAIL")
print("Full. leaderboard:",scores)
print("HEAD:",scores[0])
print("TAIL:",scores[1:])
print("HEAD OF TAIL:",scores[1:][0])
print("TAIL OF TAIL:",scores[1:][1:])
def dilation(a,depth=0):
    indent = " " * depth
    print(f"{indent}List: {a} -> length= {len(a)}")
    if len(a) == 1:
        print("{indent}Base case reached!!")
        return
    dilation(a[1:], depth+1)
print("Part2: Base Case")
dilation([490,500,190,246])    
