from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")
root.geometry("400x400")

# Databases

# Create a database or create one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE adressES(
    first_name text,
    last_name text,
    city text,
    state text,
    zipcode text
)""")

# Commit changes
conn.commit()

# Close connection
conn.close()

mainloop()
