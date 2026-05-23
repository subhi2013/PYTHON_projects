contacts = {}
while True:
    print("(1)add contact\n(2)view contacts\n(3)search contact\n(4)delete contact\n(5)exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        name =input("enter the name:")
        number = input("enter the number:")
        contacts[name] = number
        file = open("contacts.txt" , "a")
        file.write(name + "-" + number + "\n")
        file.close()
        print("contact added")
    elif choice == 2:
        file = open("contacts.txt" , "r")
        print("\ncontacts:\n")
        for line in file:
            print(line)
        file.close()
    elif choice == 3:
        search = input("enter name to search:")
        if search in contacts:
            print("phone number:" , contacts[search])
        else:
            print("contacts not found")
    elif choice == 4:
        delete = input("enter name:")
        if delete in contacts:
                del contacts[delete]
                print("contact deleted")
        else:
                print("contacts not found")
    elif choice == 5:
            print("program closed")
            break
    else:
            print("invalid choice")