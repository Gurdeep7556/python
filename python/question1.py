# we need to provide discount according to sales. if the sales is more than or equal to 30000, then discount 18%. if sales is more than or equal to 20000, then discount is 15%. if sales is more than or equal to 10000 then discount is 10% rest will get a discount of 5%

sales = int(input("Enter the sales :"))

if sales >= 30000:
    print("You have been given 18% discount.")
    sales -= sales*18/100
    print("Amount after discount :",sales)
elif sales >= 20000:
    print("You have been given 15% discount.")
    sales -= sales*15/100
    print("Amount after discount :",sales)
elif sales >= 10000:
    sales -= sales*10/100
    print("You have been given 10% discount.")
    print("Amount after discount :",sales)
else:
    sales -= sales*5/100
    print("You have been given 5% discount.")
    print("Amount after discount :",sales)
    