def linear(n):
    if n == 0:
        return
    print(n,end=" ")
    linear(n-1)
print("Level 1")
linear(5)
print()
def head(n):
    if n == 0:
        return
    head(n-1)
    print(n,end=" ")
print("Level 2")
head(5)
print()
def inc_dec(n):
    if n == 0:
        return
    print(n,end=" ")
    inc_dec(n-1)
    print(n,end=" ")
print("Level 3")
inc_dec(4)
print()
def tree(n):
    if n == 0:
        return
    print(n,end=" ")
    tree(n-1)
    tree(n-1)
print("Level 4")
tree(5)
print()