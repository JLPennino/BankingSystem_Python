class Admin:
    
    def __init__(self, fname, lname, address, user_name, password, full_rights): #Variables for storing Admin Info
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
    def update_first_name(self, fname): #Updating First Name
        self.fname = fname
    
    def update_last_name(self, lname): #Updating Last Name
        self.lname = lname
                
    def get_first_name(self): #Finding Admin First Name
        return self.fname
    
    def get_last_name(self): #Finding Admin Last Name
        return self.lname
        
    def update_address(self, addr): #Updating address
        self.address = addr
    
    def set_username(self, uname): #Giving username to admin
        self.user_name = uname
        
    def get_username(self): #Finding username of admin
        return self.user_name
        
    def get_address(self): #Finding address of admin
        return self.address      
    
    def update_password(self, password): #Updating passwords
        self.password = password
    
    def get_password(self): #Finding passwords
        return self.password
    
    def set_full_admin_right(self, admin_right): #Give admin perms
        self.full_admin_rights = admin_right

    def has_full_admin_right(self): #Looking at what perms admin has
        return self.full_admin_rights
    
    def admin_account_menu(self): #Running admin account menu interface
        print ("\n Your Administration Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Update admin name")
        print ("2) Update admin login details")
        print ("3) Update admin address")
        print ("4) Update admin rights")
        print ("5) Show admin details")
        print ("6) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def admin_print_details(self): #Printing admin details
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Username: %s" %self.user_name)
        print("Password: %s" %self.password)
        print("Has Full Rights: %s" %self.full_admin_rights)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        print(" ")
    
    def run_admin_account_options(self): #Running all account options
        loop = 1
        while loop == 1:
            choice = self.admin_account_menu()
            if choice == 1: #Updating Admin Names
                fname=input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\n Enter new customer last name: ")
                self.update_last_name(sname)
            elif choice == 2: #Updating Admin Logins
                uname=input("\n Enter new login username: ")
                self.set_username(uname)
                password = input("\n Enter new login password : ")
                self.update_password(password)
            elif choice == 3: #Updating Admin Address
                addr = []
                for i in range(0,4):
                    msg = input("Enter Address: ")
                    addr.append(msg)
                self.update_address(addr)
            elif choice == 4: #Updating Admin Permissions
                admin_right=input("\n Set Admin Permissions To True Or False: ")
                if (admin_right == 'True'):
                    self.set_full_admin_right(True)
                elif(admin_right == 'False'):
                    self.set_full_admin_right(False)
                else: 
                    print("Only use True or False")
            elif choice == 5: #Printing all admin information 
                self.admin_print_details()
            elif choice == 6: #Return to logged in as admin menu
                loop = 0
        print ("\n Exit account operations")

