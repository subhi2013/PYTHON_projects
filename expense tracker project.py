expenses = {}
def add_expense():
    category = input("enter category name:")
    amount = int(input("enter amount:"))
    expenses[category] = amount
    print("expense added")
def show_expenses():
    if len(expenses) == 0:
        print("no expenses found")
    else:
        for category in expenses:
            print(category , ":" , expenses[category])
def search_expense():
    category = input("enter category to search:")
    if category in expenses:
        print(category , ":" , expenses[category])
    else:
        print("category not found")
def delete_expense():
    category = input("enter category to delete:")
    if category in expenses:
        del expenses[category]
        print("expense deleted")
    else:
        print("category not found")
def total_expense():
    total = 0
    for category in expenses:
        total = total + expenses[category]
        print("total expense is:" , total)
def average_expense():
    if len(expenses) == 0:
        print("expense not found")
    else:
        total = 0
        for category in expenses:
            total = total + expenses[category]
            average = total / len(expenses)
            print("average expense:" , average)
def highest_expense():
    if len(expenses) == 0:
        print("no expenses found")
    else:
        highest_category = ""
        highest_amount = 0
        for category in expenses:
            if expenses[category] > highest_amount:
                highest_amount = expenses[category]
                highest_category = category
                print("highest expense:")
                print(highest_category, ":" , highest_amount)
def save_expenses():
    file = open("expenses.txt" , "w")
    for category in expenses:
        file.write(category + "," + str(expenses[category]) + "\n")
    file.close()
    print("expenses saved")
def load_expenses():
    try:
        file = open("expenses.txt" , "r")
        for line in file:
            line = line.strip()
            category, amount = line.split(",")
            expenses[category] = int(amount)
            file.close()
            print("expenses loaded")
    except FileNotFoundError:
        print("no saved file found")
while True:
    print("\n-------EXPENSE TRACKER-------\n")
    print("1. add expenses")
    print("2. show expenses")
    print("3. search expenses")
    print("4. delete expenses")
    print("5. total expenses")
    print("6. average expenses")
    print("7. highest expenses")
    print("8. save expenses")
    print("9. load expenses")
    print("10. exit")
    choice = input("enter your choice:")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        total_expense()
    elif choice == "6":
        average_expense()
    elif choice == "7":
        highest_expense()
    elif choice == "8":
        save_expenses()
    elif choice == "9":
        load_expenses()
    elif choice == "10":
        print("program ended")
        break
    else:
        print("choice not found")
    