li = [45,23,89,67,12]
# #max_number 
# max = 0
# for i in li:
#     if max<i:
#         max=i
# print(max)

# in built functions :
# print(max(li))
# print(sum(li))
# print(min(li))


#min number 
# min = li[0]
# for i in li:
#     if min>i:
#         min=i
# print(min)

#weather a is present or not 
# li = ["apple","kiwi","cherry","orange","mango"]
# li2=[]
# for i in range(len(li)):
#     if 'a' in li[i]:
#         li2.append(li[i])
# print(li2)


#same same but different 
# li = ["apple","kiwi","cherry","orange","mango"]
# li2=[]
# for i in li:
#     if 'a' in i:
#         li2.append(i)
# print(li2)


#printing the indices of 2 
# li=[4,22,6,2,8,2,1,9,2]
# li2 = []
# v=2
# for i in range(len(li)) :
#     if li[i]==v:
#         li2.append(i)
# print(li2)

#list comprehension -> shorter syntax
# expression loop condition 
# eg :
# li = ["apple","kiwi","cherry","orange","mango"]
# li2=[i for i in li if 'a' in i]
# print(li2)

#printing all odd numbers 
# li = [22,55,88,33,66,99]
# li2 = [i for i in li if i%2 != 0]
# print(li2)

#print a list of square of 1 - 15
# li=[]
# for i in range(1,16):
#     li.append(i**2)
# print(li)

# li = [i**2 for i in range(1,16)]
# print(li)

# using list comprehension print numbers divisible by 8 between 1 and 100 
# li = [i for i in range(1,101) if i%8 == 0]
# print(li)

# using list comprehension 
# li = [33,55,99,11,66,22]
# li2 = [li[i],'even' if i%2==0 else 'odd' for i in li ]
# print(li2)

#create 

# li=[4,22,6,2,8,2,1,9,2]
# li2 = []
# v=2
# for i in range(len(li)) :
#     if li[i]==v:
#         li2.append(i)
# print(li2)

# li = [i for i in range(len(li)) if li[i] == 2]
# print(li)

