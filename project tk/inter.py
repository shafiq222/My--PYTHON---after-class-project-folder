from tkinter import *

# Create window
root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x250")
root.config(bg="lightblue")

# Function to convert inches to centimeters
def convert():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(
        text=f"{inches} inches = {centimeters:.2f} cm"
    )

# Title label
title = Label(
    root,
    text="Length Converter",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=10)

# Input label
input_label = Label(
    root,
    text="Enter length in inches:",
    font=("Arial", 12),
    bg="lightblue"
)
input_label.pack()

# Entry box
entry = Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
entry.pack(pady=10)

# Convert button
convert_button = Button(
    root,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="darkblue",
    fg="white",
    command=convert
)
convert_button.pack(pady=10)

# Result label
result_label = Label(
    root,
    text="",
    font=("Arial", 14),
    bg="lightblue",
    fg="green"
)
result_label.pack(pady=20)

# Run application
root.mainloop()