import random

class current_account:
    def __init__ (self, customer, balance, accnum, address, overdraft):
        self.customer = customer
        self.balance = balance
        self.accnum = accnum
        self.address = address
        self.aoverdraft = overdraft

class savings_account:
    def __init__ (self, customer, balance, accnum, address, interestrate):
        self.customer
        self.balance
        self.accnum
        self.address
        self.interestrate

class fixed_term_acc:
    def __init__ (self, customer, balance, accnum, address, transfee):
        self.customer
        self.balance
        self.accnum
        self.address
        self.transfee

def output(acc):
    print(acc.customer)
    print(acc.address)
    print(acc.accnum)
    print(f"Balance = (customer.balance)")
    print(f"overdraft allowance = (customer.overdraft)")

while True:
    print("press 1 to view account details")
    print("press 2 to create a new account")

    choice = input()

    if choice == "2":
        print("What account would you like to create")
        print("Press 1 for a current account")
        print("Press 2 for a savings account")
        print("Press 3 for a fixed term account")

        choice2 = input()

    if choice2 == "1":
        customer = input("Please enter your name ")
        ccnum = random.randint(100000, 999999)
        address = input("Please enter your address ")
        returning = input("Have you banked with us before ")
        if returning == "Y":
            overdraft = 1000
        else:
            overdraft = 500

            acc = current_account(customer, 0, accnum, address, overdraft)
            
        elif choice2 == "2":
            customer = input("Please enter your name ")
            accnum = random.randint(100000, 999999)
            address = input("Please enter your address ")
            interestrate = input()

            sacc = savings_account(customer, 0, accnum, address, interestrate)
            
        elif choice2 == "3":
            customer = input("Please enter your name ")
            accnum = random.randint(100000, 999999)
            address = input("Please enter your address ")
            transfee = input()

            ftacc = fixed_term_acc(customer, 0, accnum, address, transfee)
            


    elif choice == "1":
        while True:
            try:
                search = input("Enter your name ")
                output(search)
            except AttributeError:
                print("No accounts currently under that name. Try again.")
                continue
            else:
                break
           
                



















