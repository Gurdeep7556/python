d = {"name":"abc", "age":23,"city":"chd"}
x=23
for i in d.keys():
    if d[i] == 23:
        print(i)
    
for i in d:
    if d[i] == 23:
        print(i)
        
for k,v in d.items():
    if v == 23:
        print(k)        
