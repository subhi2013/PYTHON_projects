a = str(input("enter student name:"))
b  = int(input("enter your age:"))
c = str(input("enter school name:"))
d = float(input("enter your marks:"))
datas = {
    "name" : a,
    "age" : b,
    "school" : c,
    "marks" : d}
print("-----STUDENT DETAILS------")
print("name:", datas["name"])
print("age:" , datas["age"])
print("school:" , datas["school"])
print("mark:" , datas["marks"])