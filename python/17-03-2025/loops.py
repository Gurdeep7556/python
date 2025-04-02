# while loop

#(20) table printing 
# i=1
# n=20
# while i<=10:
#     print(n,"*", i,"=", n*i, end=" ")
#     i=i+1


#print all the even number btw 1-20
# i=1
# while i<=20:
#         if i%2==0:
#             print(i,end=" ")
#         i=i+1        
    
# i=20
# while i<=1 :
#     print(i)
#     i=i-1

#print all the odd number btw 50-60
# i=50
# while i<=60:
#     if i%2!=0:
#         print(i,end=" ")
#     i=i+1

# c=0
# i=1
# while i<=20:
#     if i%2==0:
#         c=c+1
#     i=i+1
# print(c)

# c=0
# i=750 
# while i<=1250:
#     if  (i%2)!=0:
#         c=c+1
#     i=i+1
# print(c)

# #sum of 1-50
# c=0
# i=1
# while i<=50:
#     if i%2 ==0:
#         c=c+i
#     i=i+1
# print(c)

#take i/p from user and the no. of times the message is getting print
# i=input("Enter message: ")
# c=int(input("Enter the time: "))
# z=1
# while z <= c:
#      print(i)
#      z=z+1

#build a pattern like
# 1 + 1 = 2
# 2 + 2 = 4
# 4 + 3 = 7
# n=1
# i=1
# while i<=50:
#      print(n,"+", i,"=", n+i, end=" ")
#      n=n+i
#      i=i+1

a = 1
b = 1
i = 1
while i <= 10:
    print(a,'+',b,'=',a+b)
    a += b
    b+=1
    i+=1
