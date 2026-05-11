from tkinter import *
from tkinter import messagebox
import math

# Create window
root = Tk()
root.title("Interest Calculator")
root.geometry("400x350")
root.configure(bg="lightblue")

# Heading
title = Label(
    root,
    text="Simple & Compound Interest Calculator",
    font=("Arial", 14, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=10)

# Principal Amount
Label(root, text="Principal Amount:", bg="lightblue", font=("Arial", 11)).pack()
principal_entry = Entry(root, font=("Arial", 11))
principal_entry.pack(pady=5)

# Rate of Interest
Label(root, text="Rate of Interest (%):", bg="lightblue", font=("Arial", 11)).pack()
rate_entry = Entry(root, font=("Arial", 11))
rate_entry.pack(pady=5)

# Time Period
Label(root, text="Time Period (Years):", bg="lightblue", font=("Arial", 11)).pack()
time_entry = Entry(root, font=("Arial", 11))
time_entry.pack(pady=5)

# Result Labels
simple_result = Label(root, text="", bg="lightblue", font=("Arial", 11, "bold"))
simple_result.pack(pady=10)

compound_result = Label(root, text="", bg="lightblue", font=("Arial", 11, "bold"))
compound_result.pack(pady=5)

# Function to calculate interest
def calculate_interest():
    try:
        P = float(principal_entry.get())
        R = float(rate_entry.get())
        T = float(time_entry.get())

        # Simple Interest
        SI = (P * R * T) / 100

        # Compound Interest
        Amount = P * (1 + R / 100) ** T
        CI = Amount - P

        # Display Results
        simple_result.config(
            text=f"Simple Interest = {SI:.2f}",
            fg="green"
        )

        compound_result.config(
            text=f"Compound Interest = {CI:.2f}",
            fg="purple"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Button
calc_button = Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="darkblue",
    fg="white",
    command=calculate_interest
)
calc_button.pack(pady=15)

# Run app
root.mainloop()