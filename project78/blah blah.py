from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")

# Display screen
entry = Entry(root, width=20, font=("Arial", 24), bd=5, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to add numbers to screen
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

# Clear screen
def clear():
    entry.delete(0, END)

# Calculate product (only multiplication)
def multiply():
    try:
        expression = entry.get()
        result = eval(expression)  # simple way for now
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button style
btn_style = {"font": ("Arial", 14), "width": 5, "height": 2, "bg": "gray", "fg": "white"}

# Number buttons
Button(root, text="7", command=lambda: click(7), **btn_style).grid(row=1, column=0)
Button(root, text="8", command=lambda: click(8), **btn_style).grid(row=1, column=1)
Button(root, text="9", command=lambda: click(9), **btn_style).grid(row=1, column=2)

Button(root, text="4", command=lambda: click(4), **btn_style).grid(row=2, column=0)
Button(root, text="5", command=lambda: click(5), **btn_style).grid(row=2, column=1)
Button(root, text="6", command=lambda: click(6), **btn_style).grid(row=2, column=2)

Button(root, text="1", command=lambda: click(1), **btn_style).grid(row=3, column=0)
Button(root, text="2", command=lambda: click(2), **btn_style).grid(row=3, column=1)
Button(root, text="3", command=lambda: click(3), **btn_style).grid(row=3, column=2)

Button(root, text="0", command=lambda: click(0), **btn_style).grid(row=4, column=1)

# Multiply button
Button(root, text="×", command=lambda: click("*"), bg="orange", fg="white",
       font=("Arial", 14), width=5, height=2).grid(row=1, column=3)

# Equals button
Button(root, text="=", command=multiply, bg="green", fg="white",
       font=("Arial", 14), width=5, height=2).grid(row=4, column=2)

# Clear button
Button(root, text="C", command=clear, bg="red", fg="white",
       font=("Arial", 14), width=5, height=2).grid(row=4, column=0)

# Run app
root.mainloop()