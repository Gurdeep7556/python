#Anything within "" & '' are considered as string in python.

# to print a string in for loop 
# x='hello'
# for i in x :
#     print(i)

# operators in string
# (+) used for concatenation
# (*) used for replication

#CONCATENATION 
# we cannot concat the different datatype variable
# x='hello'
# y='world'
# # for i in x,y:
# print(x+' '+y)


#concatenation with + sign
# x='my house no is'
# y='67'
# print(x+' '+y)


#concatenation without + sign (using FORMAT)
#syntax---> varname.fromat(diffn dt).....
#example: 
# x='my house no is {}'
# y=67
# print(x.format(y))

#2 
# x='my house no is {}'
# y=67
# c=x.format(y)
# print(c)

#3
# x=f'my house no is {y}'
# y=67
# print(x)


# REPLICATE used to replicate any variables data but we cannot give spaces in this
# x='abc'
# print(x*5)

#MEMBERSHIP operator
#1. IN 
#2. NOT IN
# x='helllo'
# print("e" in x)
# print("G" not in x)

# x="a"
# y='A'
# print(x>y)
#ASCII values
#ORD gives the ASCII value of any Digit or Character
# print(ord("A"))
#CHR gives the digit or character of any ASCII value
# print(chr(65))

# ---> Make a product bar code that give the product name, 
# Take input from the user of 1 character and assign that character to a particular product<---

#METHODS

#1.UPPER
# x="abhay"
# print(x.upper())
#2.lower
# x="ABHAY"
# print(x.lower())
#3.Title(only char is in upper case bakki lower case of every word)
# x="theta academy"
# print(x.title())
#4.Capitalize(only char is in upper case bakki lower case of starting word)
# x="theta academy"
# print(x.capitalize())
#5.isAlpha(checks wether the string has only aplhabet or not gives o/p as true or false )
# x='hel5lo'
# print(x.isalpha())
#6. isDigit(checks wether the string has only digit or not)
# x='1235'
# print(x.isdigit())
#7. isalnum(check wether the string has alphabet and number or not as well as checks for special char)
# x="456abh"
# print(x.isalnum())
#8.islower(checks if string is not in lower case or not)
# x="hello"
# print(x.islower())
#9.isupper(checks for upper case)
# x="HELLO"
# print(x.isupper())
#10. isspace(check for spaces)
# x="HELLO"
# print(x.isspace())
#11.startswith(checks if the string is starting with the given char or not)
# x="HELLO"
# print(x.startswith("H"))
#12.endswith(checks if the string is ending with the given char or not)
# x="HELLO"
# print(x.endswith("O"))
#13.replace(replace the given string with any other string)
# x="HELLO World HELLO"
# print(x.replace("HELLO","OIEE",1))


#count
# x='hello'
# print(x.count('l'))

#index: we can specify the start and end btw any range, follows +ve indexing to find occuring element. returns ValueError when substring is not present in the string.
# x='university'
# print(x.index('i')) #returns 2
# print(x.index('i',3,8)) #returns 7

#find : works like index, returns -1 when substring is not present in the string.
# x='university'
# print(x.find('i')) #returns 2
# print(x.find('p') ) #returns -1

#rindex: starts from right and return the 1 occuring index value gives +ve indexing
# x='university'
# print(x.rindex('i'))

#rfind: starts from right and return the 1 occuring index value gives +ve indexing
# x='university'
# print(x.rfind('i'))


#quesntion
# word=input("Enter any Word: ")
# a=word[0]
# print(a)
# b=word.replace(word[0],'$')
# print(b)
# print(a+b[1:])

#partition
# x="Hi im abhay singh"
# print(x.partition('abhay'))

# Center
# x='abhay'
# y='singh'
# print((x+" "+y).center(25))

#rjust
# x='abhay'
# y='singh'
# print((x+" "+y).rjust(25,'+'))

#ljust
# x='abhay'
# y='singh'
# print((x+" "+y).ljust(25))

#length :gives the length of the string
# x='hello'
# print(len(x))

#strip
# x=input("enter the messg: ")
# print(x.strip())
#lstrip
# print(x.lstrip())
#rstrip
# print(x.rstrip())


#split -->string ko list mai convert kar sakte hai
#joins-->list ko string mai covert kar sakte hai


#take a input from user and find length if it is divisible by 4 then print in reverse order
# x=input("Enter a word: ")
# a=len(x)
# if a%4==0:
#     print(x[-1::-1])
# else:
#     print(x)

#enter a word from a user and detect ing is there or not if it is there print ly with word
# x=input("Enter a word: ")
# if x.endswith("ing"):
#     print(x,"ly")
# else:
#     print(x+"ing")

# write a code to convert a string to all uppercase if it contains atleast 2 upper case character
