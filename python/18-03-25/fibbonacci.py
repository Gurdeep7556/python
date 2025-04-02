# Enter the number of terms you want 
num=int(input("Enter no. of time: "))
a=0
b=1
c=0
print(a,b)
for i in num:
   a=b
   b=c
   c=a+b
   print(c,end=',')
   i+=1