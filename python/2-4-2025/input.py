# take input from the user and count teh occurence of each alphabet

s = input("Enter the string :")
d = {}
# for i in s:
#     d.update({i:s.count(i)})
# print(d)

for i in s :
    d[i] = s.count(i)
print(d)