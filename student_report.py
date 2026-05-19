name = str(input("enter student name:"))
a = float(input("enter maths mark:"))
b = float(input("enter science mark:"))
c = float(input("enter english mark:"))
d = float(input("enter second language mark:"))
e = float(input("enter social mark:"))
total = a + b + c + d + e 
avg = total / 5
print(" ------student report---------")
print("name of the student:" , name)
print("total marks:" , total)
print("average marks:" , avg)
if avg >= 35:
    print("congragulation you passed your exam")
else:
    print("sorry you failed your exam better luck next time")