import sqlite3

#--------------------- This Database Program Usage ------------------------

# This python program I coded makes an sqlite3 database and allows the
# items added and updated in the stock intake system to be added stored
# accordinally in this database by storing them in the appropriate columns

# -------------------------------------------------------------------------

class Database:
    
    """
    This class handles how the interactions will be done and how new items will be added
    as well as updating original items already in the database, it also subsequently deals
    with deletion from the database of specific items. Clearing inputs aren't here as
    that is a feature specifically for the stock intake system and doesn't need to
    interact with the DB.

    """
    
    def __init__(self, db):
        #Connect to the database and make the cursor
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        #creates the table withing the database with specific attributes needed
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, item text, customer text, retailer text, price text, category text, quantity text)")
        self.conn.commit()
        
        
        #Below was used once allow 2 new columns
#         addColumn1 = "ALTER TABLE item ADD COLUMN category varchar(32)"
#         self.cur.execute(addColumn1)

#         addColumn2 = "ALTER TABLE item ADD COLUMN quantity varchar(10)"
#         self.cur.execute(addColumn2)



    def fetch(self):
        #fetches all the items from the database 
        self.cur.execute("SELECT * FROM item")
        rows = self.cur.fetchall()
        return rows

    def insert(self, item, customer, retailer, price, category, quantity):
        #inserts values into the item section of the database
        self.cur.execute("INSERT INTO item VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (item, customer, retailer, price, category, quantity))
       
        
        
        self.conn.commit()

    def remove(self, id):
        #allows deletion of specific items
        self.cur.execute("DELETE FROM item WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, item, customer, retailer, price, category, quantity):
        #allows updates of item for quantity and sales - '?' are placeholders for the parameters of the actual values
        self.cur.execute("UPDATE item SET item = ?, customer = ?, retailer = ?, price = ?, category = ?, quantity = ? WHERE id = ?",
                         (item, customer, retailer, price, category, quantity, id))
        self.conn.commit()

    def __del__(self):
        #closes the connection to the database
        self.conn.close()


