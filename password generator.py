import random
characters = [
    "a" , "b" , "c" ,"d" ,
    "1" , "2" , "3" , "4" ,
    "@" , "#" , "$" , "%"
    ]
length = int(input("enter passwword length:"))
password = " "
for i in range(length):
    password = password + random.choice(characters)
print("your final password is:" , password)