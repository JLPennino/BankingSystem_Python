class CustomerAccount:
    def __init__(self, fname, lname, address, current_account_no, current_account_balance, current_overdraft, current_interest, savings_account_no, savings_account_balance, savings_overdraft, savings_interest):
        self.fname = fname #Assigns all attributes to a value
        self.lname = lname
        self.address = address
        self.current_account_no = current_account_no
        self.savings_account_no = savings_account_no
        self.current_account_balance = float(current_account_balance)
        self.savings_account_balance = float(savings_account_balance)
        self.current_overdraft = current_overdraft
        self.current_interest = current_interest
        self.savings_overdraft = savings_overdraft
        self.savings_interest = savings_interest
    
    def data(self): #Converts data to json when data saved
        return {
            "fname": self.fname,
            "lname": self.lname,
            "address[0]": self.address[0],
            "address[1]": self.address[1],
            "address[2]": self.address[2],
            "address[3]": self.address[3],
            "current_account_no": self.current_account_no,
            "current_balance": self.current_account_balance,
            "current_overdraft": self.current_overdraft,
            "current_interest": self.current_interest,
            "savings_account_no": self.savings_account_no,
            "savings_balance": self.savings_account_balance,
            "savings_overdraft": self.savings_overdraft,
            "savings_interest": self.savings_interest
        }
    
    def update_first_name(self, fname): #Updating first name of customer
        self.fname = fname
    
    def update_last_name(self, lname): #Updating last name of customer
        self.lname = lname
                
    def get_first_name(self): #Finding first name of customer
        return self.fname
    
    def get_last_name(self): #Finding last name of customer
        return self.lname
        
    def update_address(self, addr): #Updating customer address
        self.address = addr
        
    def get_address(self): #Finding customer address
        return self.address
    
    def deposit_current_account(self, amount): #Deposit Balance
        self.current_account_balance+=amount
        
    def withdraw_current_account(self, amount): #Withdraw Balance
        self.current_account_balance-=amount
        
    def deposit_savings_account(self, amount): #Deposit Balance
        self.savings_account_balance+=amount
        
    def withdraw_savings_account(self, amount): #Withdraw Balance
        self.savings_account_balance-=amount
        
    def print_balance_current_account(self): #Display current account balance
        print("\n The current account balance is £%.2f" %self.current_account_balance)
        
    def print_balance_savings_account(self): #Display current account balance
        print("\n The savings account balance is £%.2f" %self.savings_account_balance)
        
    def get_balance_current_account(self): #Finding current balance
        return self.current_account_balance
    
    def get_balance_savings_account(self): #Finding savings balance
        return self.savings_account_balance
    
    def get_current_account_no(self): #Finding current account number
        return self.current_account_no
    
    def get_savings_account_no(self): #Finding savings account number
        return self.savings_account_no
    
    def print_current_overdraft(self): #Finding overdraft amount
        print("\n The current overdraft amount is £%.2f" %self.current_overdraft)
        
    def print_savings_overdraft(self): #Finding overdraft amount
        print("\n The savings overdraft amount is £%.2f" %self.savings_overdraft)
        
    def print_current_interest(self): #Finding overdraft amount
        print("\n The current account interest rate is %.2f" %self.current_interest)

    def get_current_interest(self):
        return self.current_interest
        
    def print_savings_interest(self): #Finding overdraft amount
        print("\n The savings account interest rate is %.2f" %self.savings_interest)

    def get_savings_interest(self):
        return self.savings_interest
    
    def get_current_overdraft(self): #Finding current overdraft amount
        return self.current_overdraft
    
    def get_savings_overdraft(self): #Finding savings overdraft amount
        return self.savings_overdraft
    
    def account_menu(self): #Running account menu interface
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money to current account")
        print ("2) Deposit money to savings account")
        print ("3) Withdraw money from current account")
        print ("4) Withdraw money from savings account")
        print ("5) Check account balances")
        print ("6) Check eligible account overdraft amounts")
        print ("7) Check current account interest rates")
        print ("8) Update customer name")
        print ("9) Update customer address")
        print ("10) Show customer details")
        print ("11) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self): #Printing customer details
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Current Account No: %s" %self.current_account_no)
        print("Current Account Balance: £%s" %self.current_account_balance)
        print("Savings Account No: %s" %self.savings_account_no)
        print("Savings Account Balance: £%s" %self.savings_account_balance)
        print("Eligible Current Account Overdraft Amount: £%s" %self.current_overdraft)
        print("Eligible Savings Overdraft Amount: £%s" %self.savings_overdraft)
        print("Current Account Interest Rate: %s" %self.current_interest)
        print("Savings Account Interest Rate: %s" %self.savings_interest)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        print(" ")
   
    def run_account_options(self): #Running all account options
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1: #Depositing money into current account
                amount=float(input("\n Please enter amount to deposit into current account: "))
                self.deposit_current_account(amount)
                self.print_balance_current_account()
            elif choice == 2: #Depositing money into savings account
                amount=float(input("\n Please enter amount to deposit into savings account: "))
                self.deposit_savings_account(amount)
                self.print_balance_savings_account()
            elif choice == 3: #Withdrawing money from current account 
                amount=float(input("\n Please enter amount to withdraw from current account: "))
                if(self.current_account_balance == 0):
                    if(amount > self.current_overdraft):
                        print("Not enough balance or overdraft to do this")
                    else:
                        self.current_overdraft -= amount
                        print("Not enough balance, so the balance has been debited from the available overdraft")
                        self.print_current_overdraft()
                elif(amount > self.current_account_balance + self.current_overdraft):
                    print("Not enough balance or overdraft to do this")
                elif(amount > self.current_account_balance):
                    clientBal = self.current_account_balance
                    amount -= clientBal
                    self.current_account_balance = -amount
                    self.current_overdraft -= amount
                    print("Removed £%s from client account + £%s from overdraft" % (clientBal, amount))
                    self.print_current_overdraft()
                    self.print_balance_current_account()
                else:
                    self.withdraw_current_account(amount)
                    self.print_balance_current_account()
            elif choice == 4: #Withdrawing money from savings account
                amount=float(input("\n Please enter amount to withdraw from savings account: "))
                if(self.savings_account_balance == 0):
                    if(amount > self.savings_overdraft):
                        print("Not enough balance or overdraft to do this")
                    else:
                        self.savings_overdraft -= amount
                        print("Not enough balance, so the balance has been debited from the available overdraft")
                        self.print_savings_overdraft()
                elif(amount > self.savings_account_balance + self.savings_overdraft):
                    print("Not enough balance or overdraft to do this")
                elif(amount > self.savings_account_balance):
                    clientBal = self.savings_account_balance
                    amount -= clientBal
                    self.savings_account_balance = -amount
                    self.savings_overdraft -= amount
                    print("Removed £%s from client account + £%s from overdraft" % (clientBal, amount))
                    self.print_savings_overdraft()
                    self.print_balance_savings_account()
                else:
                    self.withdraw_savings_account(amount)
                    self.print_balance_savings_account()  
            elif choice == 5: #Printing account balances
                self.print_balance_current_account()
                self.print_balance_savings_account()
            elif choice == 6: #Printing account overdrafts
                self.print_current_overdraft()
                self.print_savings_overdraft() 
            elif choice == 7: #Printing accounts interest rates
                self.print_current_interest()
                self.print_savings_interest()
            elif choice == 8: #Updating Customer Names
                fname=input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\n Enter new customer last name: ")
                self.update_last_name(sname)
            elif choice == 9: #Updating Address
                addr = []
                for i in range(0,4):
                    msg = input("Enter Address: ")
                    addr.append(msg)
                self.update_address(addr)
            elif choice == 10: #Printing all customer information 
                self.print_details()
            elif choice == 11:
                loop = 0
        print ("\n Exit account operations")
