# st = input("Enter the string :")
# for i in range(len(st)):
#     print(i)
    
# for asscessing string also
# st = input("Enter the string :")
# for i in range(len(st)):
#     print(i,st[i])

#for replicating each character of string
#1
# st = input("Enter the string :")
# for i in range(len(st)):
#     print(st[i]*2,end = '')
    
 #2   
# st = input("Enter the string :")
# for i in st:
#     print(i*2,end = '')
    
#3  
# st = input("Enter the string :")
# x=''
# for i in st:
#     x=st+i*2
# print(st)


#printing even index value

#1
# st = input("Enter the string :")
# for i in range(len(st)):
#     if i%2==0:
#         print(st[i],end = ' ')

#2
st = input("Enter the string :")
x=' '
for i in range(len(st)):
    if i%2==0:
       x=st[i]
       print(x)


# input from user print last two characters thrice
# st = input("Enter the \"string\" :")
# print(st[-2:]*3,end =' ')

#write a python program to convert a string to all upper case if it contains atleast two uppercase character in the first four characters

# st = input("Enter the string :")
# up = 0
# for i in st[:4]:
#     if i.isupper():
#         up+=1
#     if up>=2:
#         print(st.upper())
#     else:
#         print(st)

#escape character(' \",\n,\t ')