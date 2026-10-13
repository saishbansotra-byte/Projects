import tkinter as tk

# Functions

def add():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1 + num2
    answer.config(text=result)


def subtract():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1 - num2
    answer.config(text=result)


def multiply():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1 * num2
    answer.config(text=result)


def divide():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result = num1 / num2
    answer.config(text=result)


# Create window
window = tk.Tk()

window.title("My Calculator")
window.geometry("300x350")


# First number
tk.Label(window, text="Enter first number").pack()

number1 = tk.Entry(window)
number1.pack()



tk.Label(window, text="Enter second number").pack()

number2 = tk.Entry(window)
number2.pack()


# Buttons
tk.Button(window, text="ADD", command=add).pack(pady=5)

tk.Button(window, text="SUBTRACT", command=subtract).pack(pady=5)

tk.Button(window, text="MULTIPLY", command=multiply).pack(pady=5)

tk.Button(window, text="DIVIDE", command=divide).pack(pady=5)


# Result
tk.Label(window, text="Answer:").pack(pady=10)

answer = tk.Label(window, text="0", font=("Arial", 20))
answer.pack()


# Run the window
window.mainloop()
