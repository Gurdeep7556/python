# enter a number from user and display the sum of its digits

num = int(input("enter the number :"))#234
sum = 0
while num :
    sum = sum + num%10#4+0#3+4#7+2
    num = num//10#23#2#0
print("The sum of the digits is :",sum)