List1 = [1,2,3,4,5,6,7]
List2 = []
for num in List1:
    if num % 2 == 0:
        List1.remove(num)
        List2.append(num)
        
        
print("List1: ",List1)
print("List1: ",List2)