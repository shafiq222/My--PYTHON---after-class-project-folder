from tkinter import *

# Create the main window
root = Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="lightblue")

# Function to check password strength
def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password!", fg="red")

    elif length < 5:
        result_label.config(text="Weak Password", fg="red")

    elif length < 8:
        result_label.config(text="Medium Password", fg="orange")

    else:
        result_label.config(text="Strong Password", fg="green")

# Title Label
title_label = Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title_label.pack(pady=15)

# Password Label
password_label = Label(
    root,
    text="Enter Password:",
    font=("Arial", 12),
    bg="lightblue"
)
password_label.pack()

# Password Entry
password_entry = Entry(
    root,
    show="*",
    width=30,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

# Check Button
check_button = Button(
    root,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="darkblue",
    fg="white",
    command=check_strength
)
check_button.pack(pady=10)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="lightblue"
)
result_label.pack(pady=10)

# Run the application
root.mainloop()