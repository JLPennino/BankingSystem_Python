from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main window 
master.geometry("200x200") 
master.title("Bank System")
  
  
# Login Page
def openLoginPage(): 
      
    # Toplevel object which will be treated as a new window 
    LoginPage = Toplevel(master) 
  
    
    LoginPage.title("Bank System") 
  
     
    LoginPage.geometry("200x200") 
  
 
    Label(LoginPage,  
          text ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").pack()
    Label(LoginPage,  
          text ="Login Screen").pack() 
    Label(LoginPage,  
          text ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").pack()
    Label(LoginPage, text='Admin Username:').pack()
    e1 = Entry(LoginPage).pack() 
    Label(LoginPage, text='Admin Password:').pack() 
    e2 = Entry(LoginPage).pack() 
    btnlogin = Button(LoginPage,
             text ="Login",  
             command = openAdminMenu) 
    btnlogin.pack()
    
def openAdminMenu(): #Admin Menu
      
     
    AdminMenu = Toplevel(master) 
  
    
    AdminMenu.title("Bank System") 
  
    
    
  
    # Admin menu gui
    Label(AdminMenu,  
          text ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").pack()
    Label(AdminMenu,  
          text ="Admin Menu").pack() 
    Label(AdminMenu,  
          text ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").pack()
    
    btntransfer = Button(AdminMenu,
             text ="Transfer Money",  
             command = openLoginPage) 
    btntransfer.pack(side = TOP)
    btncustomer = Button(AdminMenu,
             text ="Customer Account Settings",  
             command = openLoginPage) 
    btncustomer.pack(side = TOP)
    btnadmin = Button(AdminMenu,
             text ="Admin Account Settings",  
             command = openLoginPage) 
    btnadmin.pack(side = TOP)
    btndelete = Button(AdminMenu,
             text ="Delete Customer",  
             command = openLoginPage) 
    btndelete.pack(side = TOP) 
    btnallcustomer = Button(AdminMenu,
             text ="Customer Details",  
             command = openLoginPage) 
    btnallcustomer.pack(side = TOP) 
    btnalladmin = Button(AdminMenu,
             text ="Admin Details",  
             command = openLoginPage) 
    btnalladmin.pack(side = TOP) 
    btnmanagement = Button(AdminMenu,
             text ="Management Report",  
             command = openLoginPage) 
    btnmanagement.pack(side = TOP) 
    btnsave = Button(AdminMenu,
             text ="Save Data",  
             command = openLoginPage) 
    btnsave.pack(side = TOP) 
    btnout = Button(AdminMenu, #Signs out of Admin Login
             text ="Sign Out",  
             command = lambda:[openAdminMenu, AdminMenu.destroy])
    btnout.pack(side = BOTTOM)   
# Main Menu Of Bank System
label1 = Label(master,  
              text ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
  
label1.pack(pady = 10)
  
label = Label(master,  
              text ="Welcome To Python Bank System") 
  
label.pack(pady = 10) 

label2 = Label(master,  
              text ="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

label2.pack(pady = 10)
  
# A button which will open a new window on button click 
btn = Button(master,
             text ="Admin Login",  
             command = openLoginPage) 
btn.pack() 
# A button which will exit out of the gui
btn = Button(master, 
             text ="Quit Python Bank System",  
             command = master.destroy) 
btn.pack() 
  
 
mainloop() 