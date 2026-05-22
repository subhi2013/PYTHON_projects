tasks = []
print("hello , welcome you can write your to do list here")
while True:
    print("select your options\n(1)add task\n(2)view task\n(3)remove task\n(4)exit/")
    choice = int(input("enter your choice:"))
    if choice == 1:
        task = (input("enter the tasks:"))
        tasks.append(task)
        file = open("tasks.txt" , "a")
        file.write(task + "\n")
        file.close()
        print("task added")
    elif choice == 2:
        file = open("tasks.txt" , "r")
        print("\nyour tasks:\n")
        for line in file:
            print(line)
        file.close()
    elif choice == 3:
        a = str(input("tasks you want to remove:"))
        if a in tasks:
          tasks.remove(a)
          print("tasks removed")
    elif choice == 4:
       print("program closed")
       break
    else:
        print("invalid choice")
            
