from tkinter import *
from functools import partial
import time

#F1 Login done by CAMERON NOAKES

#I am coding in self contained programs and importing them as libraries,
# allows it to be more organised and smaller program increments.

#This Program is the login feature of F1i. allowing users to login
# who have valid credentials.

#makes the window
root = Tk()  
root.geometry('250x100')  
root.title('AllAboutToys Login')

#Main Class for the login program

class Login():
    
    """
    The use of this class should allow successful login attempts
    
    If a login is invalid it will fail and an error message will occur
    
    This program is to only allow authenticated users to access the stock intake system
    """
    
    
    def validate_login(UserID, password):
        print("UserID entered:", UserID.get())
        print("password entered:", password.get())
    
    
        f = open("creds.txt","r")
    
        f_read = f.readline()
        f_read2 = f_read.strip('\n')
    
        entry = f_read2.split(",")
        
        #debugging purposes
        
        #print(entry[0])
        #print (entry[1])


        if entry[0] == UserID.get() and entry[1] == password.get():
            
            #changes the background to show a successful login
            root.configure(bg="Green")
            valid_creds = Label(root,text="Valid Credensials").grid(row=2, column=1)
        
            #Destroys the previous window as it wasn comflicting with input fields in 2nd library.
            root.destroy()
        
            #Calling for next library after successful login.
            import Stock_Taking_OOP
        

        else:
            # Executed if invalid login 
             print ("Wrong Credensials.")
             wrong_creds = Label(root,text="Wrong Credensials/ Bad Match!").grid(row=2, column=1) 



    #username label and username entry box
    UserID_Label = Label(root, text="UserID").grid(row=0, column=0)
    UserID = StringVar()
    UserID_Entry = Entry(root, textvariable=UserID).grid(row=0, column=1)  

    #password label and password entry box
    password_Label = Label(root,text="Password").grid(row=1, column=0)  
    password = StringVar()
    password_Entry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)  

    validate_login = partial(validate_login, UserID, password)

    #login button when pressed
    login_Button = Button(root, text="Login", command=validate_login).grid(row=4, column=0)


# Continious program loop
root.mainloop()







