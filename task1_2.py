a=input("Enter a string: ")
b=len(a)
i=0
for x in range(0,b):
    i=0
    if(a[x]>='a' and a[x]<='z'):
        i=1
    elif(a[x]>='A' and a[x]<='Z'):
        i=1
    if(i==0):
        print("Invalid character Inserted.")
        break
if(i==1):
    for x in range(0,b):
        if(a[x]>='a' and a[x]<='z'):
            print(a[x], end = '')
    for x in range(0,b):
        if(a[x]>='A' and a[x]<='Z'):
            print(a[x], end = '')
    
    

