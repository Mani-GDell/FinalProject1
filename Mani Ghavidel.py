#Mani Ghavidel
# Importing the required libraries
import tkinter as tk
import sqlite3
# Creating the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Student Registration System")
# Creating the database
conn = sqlite3.connect('student.db')
c = conn.cursor()
# Creating the table
c.execute('''CREATE TABLE IF NOT EXISTS students
 (name TEXT, email TEXT, password TEXT, unit TEXT)''')
# Function to add the student details to the database
def add_student():
 name = name_entry.get()
 email = email_entry.get()
 password = password_entry.get()
 unit = unit_entry.get()
 c.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (name, email, password, unit))
 conn.commit()
# Function to display the selected units
def show_units():
 c.execute("SELECT unit FROM students WHERE email=?", (email_entry.get(),))
 units = c.fetchall()
 print("Selected Units:")
 for unit in units:
  print(unit[0])
# Function to log in the student
def login():
 c.execute("SELECT * FROM students WHERE email=? AND password=?", (email_entry.get(),
password_entry.get()))
 if c.fetchone() is not None:
  show_units()
 else:
  print("Invalid email or password")
# Creating the labels
name_label = tk.Label(root, text="Name")
email_label = tk.Label(root, text="Email")
password_label = tk.Label(root, text="Password")
unit_label = tk.Label(root, text="Unit")
# Creating the entry fields
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
unit_entry = tk.Entry(root)
# Creating the buttons
register_button = tk.Button(root, text="Register", command=add_student)
login_button = tk.Button(root, text="Login", command=login)
# Placing the widgets on the window
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
unit_label.grid(row=3, column=0)
unit_entry.grid(row=3, column=1)
register_button.grid(row=4, column=0)
login_button.grid(row=4, column=1)
# Running the main loop
root.mainloop()