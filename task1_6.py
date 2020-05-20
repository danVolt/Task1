print("Operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
z = input("Select the operation:")
if z in ('1', '2', '3', '4'):
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if z == '1':
        print(x, "+", y, "=", x+y)

    elif z == '2':
        print(x, "-", y, "=", x-y)

    elif z == '3':
        print(x, "*", y, "=", x*y)

    elif z == '4':
        print(x, "/", y, "=", x/y)
    else:
        print("Invalid Input")
