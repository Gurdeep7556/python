#replace any value of a key
# 1. direct method -> can change only value
# d = {"name":"abc", "age":23,"city":"chd"}
# d["age"]=24
# print(d)

# 2. update method 
# d.update ({"age":67,"city":"jaipur"}) #update can be used to change multiple values
# print(d)

# adding a new key value pair to existing dictionary
# 1.Direct method -> will change the value if it exist if not then it will add a new key value pair
# d["Blood group "]="A+"
# print(d)

# 2. Update method
# d.update({"Animal":"Rhino","zodiac sign":"scorpion"})
# print(d)

#how to delete key value pair
# 1. using pop function 
# d.pop("Animal")
# print(d)

# 2.using popitem function
# d.popitem()
#3.Delete function 
# del d
# print(d)
# 4.clear function 
# d.clear()
# print(d)


# for loop on dictionary 
d = {"name":"abhay","age":20,"city":"chd"}
for i in d:
    print(i,d[i])
    
#values
for i in d.values():
    print(i)
#keys
for i in d.keys():
    print(i)
    
#items
for k,v in d.items():
    print(k,v)