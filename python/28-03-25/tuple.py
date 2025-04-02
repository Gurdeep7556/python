#tuple is immutable (cannot be changed afterwards)
#tuple can store multiple values of different data types (hetrogenous in manner)
#tuple is ordered 

# creating a tuple

# t = ("a","b","c",5,9,2)
# print(t)
# print(len(t))
# print(type(t))

#ordered 
# print(t[0])

# for i in t:
#     print(i,end = ' ')
    
# for i in range(len(t)):
#     print(i,t[i],end =' ')


#different methods which can be performed on tuples
# print(t.index("c"))

# print(t.count("c"))

#conevrsion of tuples into a list

# 1. type casting 
# syntax --> list(tuple_name)
# l = list(t)

# l.insert(3,'k')# insert is an operation performed on list to insert between two values syntax-> list_name.insert(pos,value)
# syntax --> tuple(list_name)

# t = tuple(l)
# print(t)

# UNPACKING of Tuples 

f = ('apple','mango','grapes','guava','kiwi')
# (red,yellow,green) = f
# print(red)
# print(yellow)
# print(green)

(red,*yellow,green) = f