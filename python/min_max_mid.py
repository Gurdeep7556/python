a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))

if a>b and a>c:
    print(a," is the greatest.")
    if b>c:
        print(b,"is the mid value.")
        print(c,"is the min value.")
    else:
        print(c," is the mid value.")
        print(b," is the min value.")
elif b>a and b>c:
    print(b," is the greatest.")
    if a>c:
        print(a,"is the mid value.")
        print(c,"is the min value.")
    else:
        print(c," is the mid value.")
        print(a," is the min value.")
else :
    print(c," is the greatest.")
    if a>b:
        print(a,"is the mid value.")
        print(b,"is the min value.")
    else:
        print(b," is the mid value.")
        print(a," is the min value.")