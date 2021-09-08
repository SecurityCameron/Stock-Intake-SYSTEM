import tkinter as tk
from tkinter import messagebox
from db import Database
import datetime
# -------------------------------What This Program Does: ----------------------------------------
# 
# This is the stock intake program, it allows the inputting of new products with
# information about them and then subsequently stores them in a database. This
# program is what will be displayed after a successful login from 'login.py'
#
# -----------------------------------------------------------------------------------------------


# -------------------F1.ii & F1.iii: updating a category and a product: -------------------------

# Administrators can edit/delete a *category* and edit/delete a *product*
# through the same update feature button. Both can be done through the
# same button, thus, I have included functionality for both

# -----------------------------------------------------------------------------------------------



# -------------------------Database Filename ---------------------------
# The entire DB store would be reset each day/stocktake if saved as the
# current datetime, but to do this you would simply change "store.db"
# below to 'filename'.

# I can and have implemented this feature but as I dont want the
# products to disappear with each new stock intake I've kept it as
# "store.db" ----------------------------------------------------

today = datetime.datetime.now()

# parameters for datetime d/m/y
filename = today.strftime("%d,%b,%Y") 

# Initiate database object
db = Database("store.db") # change to filename.



# Main Application/GUI class

class Application(tk.Frame):
    
    """
    This program and class allows an admin to enter new stock into the
    
    stock intake system once authenticated through the login box program
    
    This allows updating the database with new stock in the warehouse
    
    """
    
    
    
    def __str__(self):
        return "str(today)"
    
    
    def __init__(self, master):
        
        #Init to initialise all root window settings and widgets.
        
        super().__init__(master)
        self.master = master
        master.title('Admin Panel Stock System')
        master.geometry("750x350")
    
        self.create_widgets()
        self.selected_item = 0
        self.populate_list()


    # Below is making the creation of user input
    # boxes and labels and positioning them in the UI
    
    def create_widgets(self):
        # input box and label made
        self.item_text = tk.StringVar()
        self.item_label = tk.Label(
            self.master, text='Product Name', font=('bold', 15), pady=22)
        self.item_label.grid(row=0, column=0, sticky=tk.W)
        self.item_entry = tk.Entry(self.master, textvariable=self.item_text)
        self.item_entry.grid(row=0, column=1)
        
        
        # Product ID and label made
        self.product_text = tk.StringVar()
        self.product_label = tk.Label(
            self.master, text='Product ID', font=('bold', 15))
        self.product_label.grid(row=0, column=2, sticky=tk.W)
        self.product_entry = tk.Entry(
            self.master, textvariable=self.product_text)
        self.product_entry.grid(row=0, column=3)
        
        # Description input box and label made
        self.desc_text = tk.StringVar()
        self.desc_label = tk.Label(
            self.master, text='Description', font=('bold', 15))
        self.desc_label.grid(row=1, column=0, sticky=tk.W)
        self.desc_entry = tk.Entry(
            self.master, textvariable=self.desc_text)
        self.desc_entry.grid(row=1, column=1)
        
        # Price input box and label made
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Price', font=('bold', 15))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)
        
        # Quantity input box and label made
        self.quantity_text = tk.StringVar()
        self.quantity_label = tk.Label(
            self.master, text='Quantity', font=('bold', 15))
        self.quantity_label.grid(row=1, column=4, sticky=tk.W)
        self.quantity_entry = tk.Entry(self.master, textvariable=self.quantity_text)
        self.quantity_entry.grid(row=1, column=5)
        
        # Category input bot and label made
        self.category_text = tk.StringVar()
        self.category_label = tk.Label(
            self.master, text='Category', font=('bold', 15))
        self.category_label.grid(row=0, column=4, sticky=tk.W)
        self.category_entry = tk.Entry(self.master, textvariable=self.category_text)
        self.category_entry.grid(row=0, column=5)
        
        

        # items list (listbox) - this is the box showing the DB items/products 
        self.items_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.items_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=22, padx=22)
        
        # Create scrollbar - if many items in DB you can scroll
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        
        # Set scrollbar to items and configuring it
        self.items_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.items_list.yview)

        # Allows items to be selected and deselected
        self.items_list.bind('<<ListboxSelect>>', self.select_item)

        # The Buttons for actions against the DB.
        self.add_btn = tk.Button(
            self.master, text="Add Item", width=13, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=22)

        self.remove_btn = tk.Button(
            self.master, text="Remove Item", width=13, command=self.remove_item)
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(
            self.master, text="Update Item", width=13, command=self.update_item)
        self.update_btn.grid(row=2, column=2)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", width=13, command=self.clear_text)
        self.exit_btn.grid(row=2, column=3)

    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting items
        self.items_list.delete(0, tk.END)
        
        # Loop through records
        for row in db.fetch():
            # Insert into database and list
            self.items_list.insert(tk.END, row)

    # Add new item with all fields present
    def add_item(self):
        if self.item_text.get() == '' or self.product_text.get() == '' or self.desc_text.get() == '' or self.price_text.get() == '' or self.quantity_text.get() == '' or self.category_text.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return
        print(self.item_text.get())
        
        # Insert into the Database the values inputted
        db.insert(self.item_text.get(), self.product_text.get(),
                  self.desc_text.get(), self.price_text.get(), self.category_text.get(), self.quantity_text.get())
        
        # Clear the list of items
        self.items_list.delete(0, tk.END)
        
        # Insert into list
        self.items_list.insert(tk.END, (self.item_text.get(), self.product_text.get(
        ), self.desc_text.get(), self.price_text.get(), self.category_text.get(), self.quantity_text.get()))
        self.clear_text()
        self.populate_list()

    # Runs when item is selected.
    def select_item(self, event):
        index = self.items_list.curselection()[0]
        # Find the item in question.
        self.selected_item = self.items_list.get(index)

        # Add text to entries once selected.
        self.item_entry.delete(0, tk.END)
        self.item_entry.insert(tk.END, self.selected_item[1])
        self.product_entry.delete(0, tk.END)
        self.product_entry.insert(tk.END, self.selected_item[2])
        self.desc_entry.delete(0, tk.END)
        self.desc_entry.insert(tk.END, self.selected_item[3])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(tk.END, self.selected_item[4])
        self.category_entry.delete(0,tk.END)
        self.category_entry.insert(tk.END, self.selected_item[5])
        self.quantity_entry.delete(0,tk.END)
        self.quantity_entry.insert(tk.END, self.selected_item[6])
        
        # Checks stock level of item selected in list then outputs the name as a warning box.
        if int(self.quantity_entry.get()) < 20:
            tk.messagebox.showwarning(title="Low Stock", message="The chosen item: '" + self.item_entry.get()+"' has low stock (under 20).")
            
        
        
            
        
    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(self.selected_item[0], self.item_text.get(
        ), self.product_text.get(), self.desc_text.get(), self.price_text.get(), self.category_text.get(), self.quantity_text.get())
        
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        self.item_entry.delete(0, tk.END)
        self.product_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        

#Init methods and to keep the program running in a mainloop so it doesnt close
root = tk.Tk()
app = Application(master=root)
app.mainloop()
