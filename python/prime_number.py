# # check weather a number is prime number or not 
num = int(input("Enter a number :"))
i=1
f = 0
while i <= num:
    if num%i == 0:
        f = f+1
        # if f > 2:
        #     print("The number is not prime.")
        #     break
        # else:
        #     print("The number is prime.")
        #     break
    i += 1
print(f)

#input krana hai 3 values jisme min max and middle values find karni hai