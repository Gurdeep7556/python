#list in python ...
# $ list is able to store multiple characters of multilple data types in a single variable.
# * square brackets are used to represent list.
# Characterstics of lists
# 1. list is a hetrogenous data type
# 2. list can store duplicate data
# 3. list is ordered (we have all positive indexing and negative indexing)
# 4. list is mutable(can change its values).


# eg :
# li = ['a',12,'world',4.66]
# print(li)

#how to access elements in a list
# li=['a','b','c',1,6,9]
# print(li[1]) 
# print(li[1:4])
# print(li[-1::-1])
# print(li[-2])

#Membership Operator
#1. IN
#2. NOT IN 
#li=['a','b','c',1,6,9]
# print('a' in li)
# print('a' not in li)

#For loop
# li=['a','b','c',1,6,9]
# for i in li:
#     print(li,end=' ')

#loop thrugh index number
# li=['a','b','c',1,6,9]
# for i in range(len(li)):
#     print(i,li[i])

#how to replace a element in a list
# li=['a','b','c',1,6,9]
# li[1]='y'
# print(li)

#how to add anew element in a list
# li=['a','b','c',1,6,9]
#insert
# li.insert(3,8)
# print(li)

#append: in this we are not required to enter the position of the new value, it give the element last position
# li=['a','b','c',1,6,9]
# li.append(7887)
# print(li)


#deleting elements of a list:
#1. remove method: in this we can mention the element which we want to remove
# li=['a','b','c',1,6,9]
# li.remove('b')
# print(li)

#2. pop mthd. : in this we can remove the element by giving its index no.
# li=['a','b','c',1,6,9]
# li.pop(1)
# print(li)


#3. del method
# li=['a','b','c',1,6,9]
# del li
# print(li)

#4. clear
# li=['a','b','c',1,6,9]
# li.clear()
# print(li)

#index method
# li=['a','b','c',1,6,9, 'b']
# print(li.index('b'))

#count method
# li=['a','b','c',1,6,9, 'b']
# print(li.count('b'))

#reverse method
# li=['a','b','c',1,6,9, 'b']
# li.reverse()
# print(li)


#for sorting
# li=[5,1,6,9]
# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)
# print(sorted(li))
# print(sorted(li, reverse=True))


#calculate the sum of a list
li=[99,11,16,24,59]

# a=0
# for i in li:
#     a=a+i
#     print(a)

# a=1
# for i in li:
#     a=a*i
#     print(a)

# for i in li:
#     if i%2==0:
#         print(i)

# for i in li:
#     if i%2!=0:
#         print(i)

#Palandromic means ki ulta padhe tod same mtlb aaye
#print the palandromic number from this list
li=['abca','abba','aba','acba']
var = input("Enter the value to be inserted in the list :")
li.append(var)
for i in li:
    if i==i[-1::-1]:
       print(i)
    
