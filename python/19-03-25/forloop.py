#for loop is the condition testing loop
#range Function used when we have to define our range 
# syntax: range(start, stop, step)
#1. start gives the sarting value kha se start hoga (by default the value is 0)
#2. stop gives when to stop the loop
#3. step gives the pattern like if we have to print 1,3,5 then the step is 2(by default the value is +1)
# for reverse counting we use -1 in step. -1 se counting reverse order mai start hoti hai.

#print in linear order
# for i in range(50,101):
#     print(i, end=" ")

#printing in reverse order
for i in range(100,50,-1):
    print(i)

#table printing
# for i in range(1,11):
#  print(17,"*", i,"=", 17*i)

#print even no. btw 1-50
# for i in range(1,51):
#  if(i%2==0):
#     print(i ," is even")
#  else:
#     print(i,"is odd")

#750 to 1250 all odd no.
# for i in range(750,1250):
#  if(i%2!=0):
#     print(i ," is odd")
    
#count even no. btw 1-100
# c=0
# for i in range (1,101):
#  if i%2==0:
#      c=c+1
# print(c)
    
    
#count all the odd no. frm 1900-2000
# c=0
# for i in range(1900,2001):
#  if i%2!=0:
#      c=c+1
# print(c)

#print all the sum btw the no. 50 -100
# c=0
# for i in range(50,101):
#  if i%2==0:
#      c=c+i
# print (c)

#take input from user and print the no. of time message is printed using for loop
# c=input("enter the message: ")
# n=int(input("number of time message is to be printed: "))
# for i in range(n):
#     print(c)

#check the prime number 
# n=int(input("enter a no: "))
# for i in range(2,n):
#  if n%i==0:
#      print("is not prime")
#      break
#  else:
#      print("is prime")

#break 
# for i in range(1,11):
#  print(i)
#  if i==3:
#   break

#continue
# for i in range(1,11):
#     print(i)
#     if i==3:
#      continue

#pattern printing
# n=1
# for i in range(1,51):
#     print(n,"+",i,"=",n+i)
#     n=n+i
    
    
#pattern printing While loop
# n=1
# i=1
# while i<=50:
#     print(n,"+",i,"=",n+i)
#     n=n+i
#     i=i+1

# for i in range(50,101,-1):
#     print(i)