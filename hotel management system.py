def add_guest():
    name = input("enter guest name:")
    room = input("enter room number:")
    days = input("enter number of days:")
    with open("hotel.txt", "a", encoding = "utf-8") as file:
        file.write(name + "," + room +"," + days + "\n")
        print(name,"added successfully")
def view_guests():
    try:
        with open("hotel.txt", "r", encoding = "utf-8") as file:
            data = file.read()
            if data:
                print(data)
            else:
                print("no guests found")
    except FileNotFoundError:
        print("no guests records found")
def check_out():
    name = input("enter guest name to remove:")
    try:
        with open("hotel.txt" , "r", encoding = "utf-8") as file:
            guests = file.readlines()
            with open("hotel.txt" , "w", encoding = "utf-8") as file:
                found = False
                for guest in guests:
                    if guest.strip().split(",")[0].lower() != name.lower():
                        file.write(guest)
                    else:
                        found = True
                        if found:
                            print("guest checked out successfully")
                        else:
                            print("guest not found")
    except FileNotFoundError:
        print("no guests found")
def search_guest():
    name = input("enter name to search:")
    try:
        with open("hotel.txt" , "r", encoding = "utf-8") as file:
            found = False
            for guest in file:
                data = guest.strip().split(",")
                if data[0].lower() == name.lower():
                    print("\nname:" , data[0])
                    print("\nroom:" , data[1])
                    print("\ndays:" , data[2])
                    found = True
                    break
                if not found:
                    print("guests not found")
    except FileNotFoundError:
        print("no guest records found")
def update_guest():
    name = input("enter guest name to update:")
    try:
        with open("hotel.txt" , "r", encoding = "utf-8") as file:
            guests = file.readlines()
            found = False
            for i in range(len(guests)):
                data = guests[i].strip().split(",")
                if data[0].lower() == name.lower():
                    found = True
                    print("1. change name")
                    print("2. change room")
                    print("3. change days")
                    choice = input("enter your choice:")
                    if choice == "1":
                        data[0] = input("enter new name:")
                    elif choice == "2":
                        data[1] = input("enter new room number:")
                    elif choice == "3":
                        data[2] = input("enter new number of days:")
                        guests[i] = ",".join(data) + "\n"
                        break
                    with open("hotel.txt" , "w", encoding = "utf-8")as file:
                        file.writelines(guests)
                        if found:
                            print("guest updated successfully")
                        else:
                            print("guest not found")
    except FileNotFoundError:
        print("no guests record found")
def available_rooms():
    all_rooms = []
    for i in range(101,111):
        all_rooms.append(str(i))
        booked = []
        try:
            with open("hotel.txt" , "r", encoding = "utf-8") as file:
                for guest in file:
                    data = guest.strip().split(",")
                    booked.append(data[1])
        except FileNotFoundError:
            pass
        print("\navailable rooms:")
        for room in all_rooms:
            if room not in booked:
                print(room)
def generate_bill():
    name = input("enter guest name:")
    price = 1000
    try:
        with open("hotel.txt", "r", encoding = "utf-8") as file:
            found = False
            for guest in file:
                data = guest.strip().split(",")
                if data[0].lower() == name.lower():
                    days = int(data[2])
                    total = days * price
                    print("\n-----------BILL---------")
                    print("guest name:", data[0])
                    print("room number:", data[1])
                    print("days stayed:", days)
                    print("rate:" , price)
                    print("total bill:" , total)
                    found = True
                    break
                if not found:
                    print("guests not found")
    except FileNotFoundError:
        print("no guest records found")
while True:
    print("\n -----HOTEL MANAGEMENT SYSTEM-----")
    print("(1) add guests")
    print("(2) view guests")
    print("(3) search guests")
    print("(4) check out")
    print("(5) update guest")
    print("(6) view available rooms")
    print("(7) generate bill")
    print("(8) exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        add_guest()
    elif choice == 2:
        view_guests()
    elif choice == 3:
        search_guest()
    elif choice == 4:
        check_out()
    elif choice == 5:
        update_guest()
    elif choice == 6:
        available_rooms()
    elif choice == 7:
        generate_bill()
    elif choice == 8:
        print("goodbye")
        break
    else:
        print("invalid choice")