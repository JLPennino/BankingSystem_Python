from admin import Admin
from customer_account import CustomerAccount
import json
import os
os.system('python gui.py')

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self): #Data storages
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self): #Loading customer data from json file
        
        # create customers
        print("Started Reading Previous Saved file")
        with open("CustomerData.json", "r") as read_file:
            print("Converting encoded data into readable output...")
            CustomerData = json.loads(''.join(read_file.readlines()))
            print("Decoded JSON Data From File")
            for CustomerObject in CustomerData['customerAccounts']:
                print(CustomerObject)
                self.accounts_list.append(CustomerAccount(
                    CustomerObject['fname'],
                    CustomerObject['lname'],
                    [CustomerObject["address[{}]".format(x)] for x in range(4)],
                    CustomerObject['current_account_no'],
                    CustomerObject['current_balance'],
                    CustomerObject['current_overdraft'],
                    CustomerObject['current_interest'],
                    CustomerObject['savings_account_no'],
                    CustomerObject['savings_balance'],
                    CustomerObject['savings_overdraft'],
                    CustomerObject['current_interest']
                ))
        
        print("Done reading json file")
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)


    def save_bank_data(self): #Saving customer data to json data file
        with open("CustomerData.json", "w") as writefile:
            writefile.write(self.__getAccountsFormatted())
            writefile.flush()
            writefile.close()

            print("{} accounts saved".format(len(self.accounts_list)))

    def __getAccountsFormatted(self): #Formats the loaded customer data 
        return json.dumps({ "customerAccounts": [self.accounts_list[i].data() for i in range(len(self.accounts_list))] }, indent = 4)


    def search_admins_by_name(self, admin_username):
        #Searching For Administrator
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
         print("\n The Admin %s does not exist! Try again...\n" %admin_username)
       
        return found_admin 
        
    def search_customers_by_name(self, customer_lname):
        #Searching For Customer
        found_customer = None
        for a in self.accounts_list:
            lname = a.get_last_name()
            if lname == customer_lname:
                found_customer = a
                break
        if found_customer == None:
         print("\n The customer %s does not exist! Try again...\n" %customer_lname)
                
        return found_customer 

    def main_menu(self):
        #Displaying bank system interface
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    


    def run_main_options(self):
        #Running admin login options
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount): #Transferring Money from one customer to the other
        sender = self.search_customers_by_name(sender_lname)
        if(sender != None):
            receiver = self.search_customers_by_name(receiver_lname)
            if(receiver != None):
                if(sender.get_balance_current_account() < amount):
                    print("The client %s %s doesn't have that much money" % (sender.get_first_name(), sender.get_last_name()))
                else:
                    sender.withdraw_current_account(amount)
                    receiver.deposit_current_account(amount)
                    print("Successfully transfered £%s from %s to %s" % (amount, sender.get_first_name(), receiver.get_first_name()))

                
    def admin_login(self, username, password):
		  #Login as Administrator
          found_admin = self.search_admins_by_name(username)
          msg = "\n Login failed"
          if found_admin != None:
              if found_admin.get_password() == password:
                  msg = "\n Login successful"
              else:
                found_admin = None
          return msg, found_admin
          

    def admin_menu(self, admin_obj):
        #The options you have within admin logged in menu
        print (" ")
        print ("Welcome Admin %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Transfer money")
        print ("2) Customer account operations & profile settings")
        print ("3) Admin account operations & profile settings")
        print ("4) Delete customer")
        print ("5) Print all customers detail")
        print ("6) Print all admins detail")
        print ("7) Management report")
        print ("8) Save bank data")
        print ("9) Sign out")
        print (" ")
        option = int(input ("Choose your option: "))
        return option


    def run_admin_options(self, admin_obj):  #Running admin options                              
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1: #Transferring Money
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)                    
            elif choice == 2: #Conducting account operations by last name
                customer_name = input("\n Please input customer surname : ")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                   customer_account.run_account_options()
            elif choice == 3: #Conducting admin account operations by username
                admin_username = input("\n Please input admin username : ")
                admin = self.search_admins_by_name(admin_username)
                if admin != None:
                   admin.run_admin_account_options()
            elif choice == 4: #Deleting Customer Data
                    if admin_obj.full_admin_rights == True:
                       customer_name = input("\n Please input customer surname you want to delete: ")
                       customer_account = self.search_customers_by_name(customer_name)
                       if customer_account != None:
                        self.accounts_list.remove(customer_account)
                        print("%s was deleted successfully!" %customer_name)
                    else: 
                        print("\n Admin %s %s does not have sufficient permissions"%(admin_obj.get_first_name(), admin_obj.get_last_name())) 
            
            elif choice == 5: #Display All customer details
                self.print_all_accounts_details()
                
            elif choice == 6: #Display All customer details
                self.print_all_admin_details()
            elif choice == 7: # Printing management report
                self.print_management_report()
            elif choice == 8: #Saves bank data and any changes back to the json file automatically 
                self.save_bank_data()
            elif choice == 9:
                loop = 0
        print ("\n Exit account operations") #Brings user back to main menu


    def print_all_accounts_details(self):
            # Prints all account details of the customers
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")
    
    def print_all_admin_details(self):
            # Prints all account details of the admins
            i = 0
            for a in self.admins_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                a.admin_print_details()
                print("------------------------")


    def print_management_report(self):
        def applyInterestRate(account): #Total interest rate to be applied across 12months
            return account.get_balance_current_account() * pow(1+account.get_current_interest(), 12)
        
        def applyInterestRateSaving(account):
            return account.get_balance_savings_account() * pow(1+account.get_savings_interest(), 12)
        
        def accountBalance(account): #Total balances to be applied across 12 months
            return max(0, account.get_balance_current_account())
        
        def accountSaving(account): #Total balances to be applied across 12 months
            return max(0, account.get_balance_savings_account())

        def accountOverdraftCurrent(account): #Total taken overdrafts across 12 months
            return min(0, account.get_balance_current_account())
            
        def accountOverdraftSavings(account): #Total taken overdrafts across 12 months
            return min(0, account.get_balance_savings_account())

        def accountOverDraft(account):
            return accountOverdraftCurrent(account) + accountOverdraftSavings(account)

        interest = sum(map(applyInterestRate, self.accounts_list)) #Variable calculations to work out total sums across year
        interestSaving = sum(map(applyInterestRateSaving, self.accounts_list))
        sumOfAccounts = sum(map(accountBalance, self.accounts_list))
        sumOfAccountsSaving = sum(map(accountSaving, self.accounts_list))

        # Total number of customers in the system
        print("%s customers registered" % len(self.accounts_list))
        # The sum of all money the customers currently have
        print("Sum of all money the customers currently have in current accounts: £%.2f" % sumOfAccounts)
        print("Sum of all money that customers currently have in savings accounts: £%.2f" % sumOfAccountsSaving)
        # Sum of interest rate payable to all accounts for one year
        print("The bank will need to pay £%.2f into current accounts" % interest)
        print(" Of that amount, £%.2f is the money that customers take into account" % sumOfAccounts)
        print(" And $%.2f interest rate" % (interest - sumOfAccounts))
        print("")
        print("The bank will need to pay £%.2f to saving accounts" % interestSaving)
        print(" Of that amount, £%.2f is the money that customers take into savings accounts" % sumOfAccountsSaving)
        print(" And £%.2f interest rate" % (interestSaving - sumOfAccountsSaving))
        #Total amount of overdrafts currently taken by all customers.
        print("Total amount of overdrafts currently taken by all customers: £%.2f" % sum(map(accountOverDraft, self.accounts_list)))


app = BankSystem()
app.run_main_options()