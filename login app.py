import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to handle login
def login():
    name = entry_name.get()
    device_number = entry_device_number.get()

    # Check if the CSV file exists
    file_exists = os.path.isfile('checkin_data.csv')

    # Open the CSV file in append mode
    with open('checkin_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Device Number', 'Name', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file doesn't exist
        if not file_exists:
            writer.writeheader()

        if name and device_number.isdigit():
            status = "CheckIN Successful"
            messagebox.showinfo("Nexus Check IN", status)
        else:
            status = "Device already CheckedIN"
            messagebox.showerror("Nexus Check IN", status)

        # Write the login attempt to the CSV file
        writer.writerow({'Device Number': device_number, 'Name': name, 'Status': status})

# Setting up the main window
app = tk.Tk()
app.title("Nexus CheckIN")
app.geometry("300x200")

# Device Number label and entry
label_device_number = tk.Label(app, text="Device Number")
label_device_number.pack(pady=5)
entry_device_number = tk.Entry(app)
entry_device_number.pack(pady=5)

# Name label and entry
label_name = tk.Label(app, text="Name")
label_name.pack(pady=5)
entry_name = tk.Entry(app)
entry_name.pack(pady=5)

# Submit button
button_login = tk.Button(app, text="Submit", command=login)
button_login.pack(pady=20)

# Running the app
app.mainloop()
