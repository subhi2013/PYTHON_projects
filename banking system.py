accounts = {}
history = []
pins = {}
account_numbers = {}
next_account_number = 1001
account_types = {}
def create_account():
    global next_account_number
    name = input("enter account name:")
    balance = int(input("enter opening balance:"))
    pin = input("create pin:")
    accounts[name] = balance
    pins[name] = pin
    account_numbers[name] = next_account_number
    print("account number:" , next_account_number)
    next_account_number += 1
    account_type = input("enter account type(savings/current):")
    account_types[name] = account_type
    print("account created")
def show_accounts():
    if len(accounts) == 0:
        print("no accounts found")
    else:
        for name in accounts:
            print(account_numbers[name],"-" , name,":", accounts[name],"-",
                  account_types[name])
def deposit_money():
    name = input("enter account name")
    if name in accounts:
        pin = input("enter pin:")
        if pin == pins[name]:
            amount = int(input("enter account name:"))
            accounts[name] = accounts[name] + amount
            print("money deposited")
        else:
            print("account not found")
    else:
        print("wrong pin")
def withdraw_money():
    name = input("enter account name:")
    if name in accounts:
        pin = input("enter pin:")
        if pin == pins[name]:
            amount = int(input("enter amount:"))
            if amount <= accounts[name]:
                accounts[name] = accounts[name] - amount
                print("money withdrawn")
                history.append(name + "withdrew" +
                               str(amount))
            else:
                print("insufficient balance")
        else:
            print("account not found")
    else:
        print("wrong pin")
def check_balance():
    name = input("enter account name:")
    if name in accounts:
        pin = input("enter pin:")
        if pin == pins[name]:
            print("balance:" , accounts[name])
        else:
            print("wrong pin")
    else:
        print("account not found")
def delete_account():
    name = input("enter account name:")
    if name in accounts:
        pin = input("enter pin:")
        if pin == pins[name]:
            del accounts[name]
            del pins[name]
            print("accounts deleted")
        else:
            print("wrong pin")
def save_accounts():
    file = open("accounts.txt" , "w", encoding="utf-8")
    for name in accounts:
        file.write(name + "," + str(accounts[name]) + "\n")
    file.close()
    print("accounts saved")
def load_accounts():
    try:
        file = open("accounts.txt" , "r", encoding="utf-8")
        for line in file:
            line = line.strip()
            name , balance = line.split(",")
            accounts[name] = int(balance)
        file.close()
        print("accounts loaded")
    except FileNotFoundError:
        print("no saved file found")
def transfer_money():
    from_account = input("from account:")
    to_account = input("to account:")
    if from_account in accounts and to_account in accounts:
        amount = int(input("enter amount:"))
        if amount <= accounts[from_account]:
            accounts[from_account] -= amount
            print("transfered successfully")
            history.append(from_account + "transferred" +
            str(amount) + "to" + to_account)
        else:
            print("insufficient balance")
    else:
        print("account not found")
def richest_customer():
    if len(accounts) == 0:
        print("no accounts found")
    else:
        richest = max(accounts, key=lambda k: accounts[k])
        print("richest customer:" , richest)
        print("balance:" , accounts[richest])
def poorest_customer():
    if len(accounts) == 0:
        print("no accounts found")
    else:
        poorest = min(accounts , key=lambda k: accounts[k])
        print("poorest customer:" , poorest)
        print("balance:" , accounts[poorest])
def total_money():
    total = 0
    for balance in accounts.values():
        total = total + balance
        print("total money is:" , total)
def average_balance():
    if len(accounts) == 0:
        print("accouns not found")
    else:
        total = 0
        for balance in accounts.values():
            total = total + balance
            average = total / len(accounts)
            print("average balance is:" , average)
def show_history():
    if len(history) == 0:
        print("no transaction found")
    else:
        print("transaction history")
        for item in history:
            print(item)
def change_pin():
    name = input("enter account name:")
    if name in pins:
        old_pin = input("enter old pin:")
        if old_pin == pins[name]:
            new_pin = input("enter new pin:")
            pins[name] = new_pin
            print("pin changed successfully")
        else:
            print("wrong old pin")
    else:
        print("account not found")
def add_interest():
    name = input("enter account name:")
    if name in accounts:
        rate = float(input("enter interest rate(%):"))
        interest = int(accounts[name] * rate / 100)
        accounts[name] = accounts[name] + interest
        history.append(name + "received interest of" +
                       str(interest))
        print("interst added")
        print("new balance:" , accounts[name])
    else:
        print("account not found")
def search_account_number():
    name = input("enter account name:")
    if name in account_numbers:
        print("account number:", account_numbers[name])
    else:
        print("account not found")
def top_3_customer():
    sorted_customers = sorted(accounts,
                       key=lambda name:accounts[name],
                       reverse=True)
    print("top 3 richest customers")
    for name in sorted_customers[:3]:
        print(name, ":", accounts[name])
def mini_statement():
    print("last 5 transactions")
    for item in history[-5:]:
        print(item)
def admin_dashboard():
    print("\n=======ADMIN DASHBOARD=======\n")
    print("total customers:" , len(accounts))
    total = sum(accounts.values())
    print("total money:" , total)
    average = total/len(accounts)
    print("average balance:" , average)
    richest = max(accounts,key=lambda k:accounts[k])
    print("richst customer:" , richest)
    print("balance:",accounts[richest])
    poorest = min(accounts,key=lambda k:accounts[k])
    print("poorest customer:",poorest)
    print("balance:",accounts[poorest])
def search_customer():
    name = input("enter customer name:")
    if name in accounts:
        print("name:", name)
        print("balance:", accounts[name])
        print("account number:", account_numbers[name])
        print("account type:",account_types[name])
    else:
        print("customer not found")
def fixed_deposit():
    amount = float(input("enter amount:"))
    rate = float(input("enter interest rate:"))
    years = int(input("enter years:"))
    maturity = amount * ((1 + rate / 100) ** years)
    print("maturity amount:" , round(maturity, 2))
def loan_emi():
    loan = float(input("enter loan amount:"))
    rate = float(input("enter annual interest rate(%):"))
    months = int(input("enter loan period(months):"))
    monthly_rate = rate / (12 *100)
    emi = (loan * monthly_rate *
    ((1 + monthly_rate) ** months)
    ) / (
        ((1 + monthly_rate) ** months) -1)
    print("monthly emi:" , round(emi, 2))
while True:
    print("\n------BANKING SYSTEM-----\n")
    print("1. create account")
    print("2. show account")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. check balance")
    print("6. delete account")
    print("7. save accounts")
    print("8. load accounts")
    print("9. transfer money")
    print("10. richest customer")
    print("11. poorest customer")
    print("12. total money")
    print("13. average balance")
    print("14. transaction history")
    print("15. change pin")
    print("16. add interest")
    print("17. search account number")
    print("18. top 3 richest customers")
    print("19. mini statement")
    print("20. admin dashboard")
    print("21. search customer")
    print("22. fixed deposit calculator")
    print("23. loan emi calculator")
    print("24. exit")
    choice = int(input("enter your choice"))
    if choice == 1:
        create_account()
    elif choice == 2:
        show_accounts()
    elif choice == 3:
        deposit_money()
    elif choice == 4:
        withdraw_money()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        delete_account()
    elif choice == 7:
        save_accounts()
    elif choice == 8:
        load_accounts()
    elif choice == 9:
        transfer_money()
    elif choice == 10:
        richest_customer()
    elif choice == 11:
        poorest_customer()
    elif choice == 12:
        total_money()
    elif choice == 13:
        average_balance()
    elif choice == 14:
        show_history()
    elif choice == 15:
        change_pin()
    elif choice == 16:
        add_interest()
    elif choice == 17:
        search_account_number()
    elif choice == 18:
        top_3_customer()
    elif choice == 19:
        mini_statement()
    elif choice == 20:
        admin_dashboard()
    elif choice == 21:
        search_customer()
    elif choice == 22:
        fixed_deposit()
    elif choice == 23:
        loan_emi()
    elif choice == 24:
        print("program ended")
        break
    else:
        print("invalid choice")
            

        
        
    