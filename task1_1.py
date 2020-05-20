def outer(a,b):
    def inner(x,y):
        return x+y
    return(inner(a,b)+5)

q=int(input("Enter a number for a : "))
w=int(input("Enter a number for b : "))
print(outer(q,w))
