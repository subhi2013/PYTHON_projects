students = {}
while True:
    print("\n-----student management system ------")
    print("1. ADD STUDENTS")
    print("2. SHOW STUDENTS")
    print("3. SEARCH STUDENTS")
    print("4. UPDATE MARKS")
    print("5. DELETE STUDENTS")
    print("6. HIGHEST MARKS")
    print("7. LOWEST MARKS")
    print("8. TOTAL MARKS")
    print("9. EXIT")
    choice = int(input("enter your choice:"))
    #add students
    if choice == 1:
        name = input("enter student name:")
        mark = int(input("enter student mark:"))
        students[name] = mark
        print("student added")
    #show students
    elif choice == 2:
        if len(students) == 0:
            print("no students found")
        else:
            for name in students:
                print(name , ":" , students[name])
    #search student
    elif choice == 3:
        name = input("enter student name to search:")
        if name in students:
            print("mark:" , students[name])
        else:
            print("student not found")
    #update mark
    elif choice == 4:
        name = input("enter student name:")
        if name in students:
            new_mark = int(input("enter new marks:"))
            students[name] = new_mark
            print("mark updated")
        else:
            print("student not found")
    #delete students
    elif choice == 5:
        name = input("enter student name:")
        if name in students:
            del students[name]
            print("student deleted")
            
        else:
            print("student not found")
    #highest mark
    elif choice == 6:
        if len(students) == 0:
            print("no students found")
        else:
            highest = max(students, key=students.get)
            print("top student is:", highest)
            print("mark:" , students[highest])
    #lowest mark
    elif choice == 7:
        if len(students) == 0:
            print("no students found")
        else:
            lowest = min(students , key =students.get)
            print("lowest student:" , lowest)
            print("mark:" , students[lowest])
    #total marks
    elif choice == 8:
        total = 0
        for mark in students.values():
            total = total + mark
            print("total mark is:" ,total)
    #exit
    elif choice == 9:
        print("program ended")
        break
    else:
        print("invalid choice")
        
        
    