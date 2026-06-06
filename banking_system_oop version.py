class bankaccount:
    def __init__(self, name, balance, pin, acc_no, acc_type):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.history = []
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"deposited {amount}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"withdrawn {amount}")
        else:
            print("insufficient balance")
    def show_balance(self):
        print("balance:" , self.balance)
    def mini_statement(self):
        for transaction in self.history:
            print(transaction)
    def check_pin(self,entered_pin):
        if entered_pin == self.pin:
            print("pin corrected")
        else:
            print("wrong pin")
    def transfer(self,other_account,amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            self.history.append(f"transferred {amount}")
            other_account.history.append(f"received {amount}")
        else:
            print("insufficient balance")
    def change_pin(self , old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("pin changed successfully")
        else:
            print("wrong pin")
    def show_account(self):
        print("account number:" , self.acc_no)
        print("name:" , self.name)
        print("balance:" , self.balance)
        print("account type:" , self.acc_type)
    def add_interest(self,rate):
        interest = self.balance * rate / 100
        self.balance += interest
        self.history.append(f"interest added {interest}")
    def fixed_deposit(self, years, rate):
        maturity = self.balance * (1 + rate/100) ** years
        print("maturity amount:" , maturity)
    def loan_emi(self, loan_amount, months):
        emi = loan_amount / months
        print("monthly emi:" , emi)
    def __str__(self):
        return f"{self.name} - {self.balance}"
account1 = bankaccount(
    "tharun",
    6000,
    "1234",
    1001,
    "savings"
    )
account2 = bankaccount(
    "subhi",
    3000,
    "3264",
    1002,
    "current"
    )
all_accounts = [account1 , account2]
total = 0
for acc in all_accounts:
    total += acc.balance
    print("total money:", total)
richest = all_accounts[0]
for acc in all_accounts:
    if acc.balance > richest.balance:
        richest = acc
print("richest customer:" , richest.name)
print("balance:" , richest.balance)
poorest = all_accounts[0]
for acc in all_accounts:
    if acc.balance < poorest.balance:
        poorest = acc
print("poorest customer:", poorest.name)
print("balance:" , poorest.balance)
total = 0
for acc in all_accounts:
    total += acc.balance
average = total / len(all_accounts)
print("average balance:" , average)
print(len(all_accounts))
print(account1)
print(account2)
print(account1.name)
print(account1.balance)
print(account1.pin)
print(account1.acc_no)
print(account1.history)
account1.deposit(1000)
print(account1.balance)
account1.withdraw(500)
print(account1.balance)
print(account1.history)
print(account1.history)
account1.show_balance()
account1.mini_statement()
account1.check_pin("1234")
account1.check_pin("2013")
account1.transfer(account2,1000)
print(account1.balance)
print(account2.balance)
account1.change_pin("1234" , "9999")
print(account1.pin)
account1.show_account()
account1.add_interest(10)
print(account1.balance)
print(account1.history)
account1.add_interest(10)
print(account1.balance)
account1.fixed_deposit(2, 10)
account1.loan_emi(12000 , 12)