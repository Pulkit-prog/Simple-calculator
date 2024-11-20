# Simple-calculator

This Python code creates a simple calculator using the Tkinter library for the graphical user interface (GUI). Below is a detailed explanation of each part of the code:

1. Importing the Required Library
python
Copy code
from tkinter import *
Tkinter is a standard Python library used to create GUIs.
2. Defining the click Function
python
Copy code
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        if scvalue.get() == "Error":
            scvalue.set("")
        scvalue.set(scvalue.get() + text)
        screen.update()
Purpose: Handles button click events.
event.widget.cget("text"): Retrieves the text from the button clicked.
if text == "=":: Evaluates the expression shown on the screen using eval() and displays the result. If an error occurs during evaluation, "Error" is shown.
elif text == "C":: Clears the screen when "C" is clicked.
else:: Appends the clicked button's text to the screen. If "Error" is present, the screen is reset before appending.
3. Creating the Main Application Window
python
Copy code
root = Tk()
root.geometry("400x600")
root.title("Calculator")
root = Tk(): Initializes the main application window.
root.geometry("400x600"): Sets the size of the window.
root.title("Calculator"): Sets the window title to "Calculator".
4. Setting Up the Display Screen
python
Copy code
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold", justify=RIGHT, bd=8, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
StringVar(): A Tkinter variable class that holds string data for the entry widget.
Entry: A widget for single-line text input.
font, justify, bd, relief: Customizes the appearance of the entry widget.
5. Creating a Function to Generate Buttons
python
Copy code
def create_button(frame, text, padx, pady):
    b = Button(frame, text=text, padx=padx, pady=pady, font="lucida 20 bold", relief=RAISED)
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-1>", click)
    return b
Button: Creates a button widget.
b.bind("<Button-1>", click): Binds a left mouse click event to the click function.
6. Creating and Packing Button Rows
python
Copy code
button_texts = [
    ["9", "8", "7", "C"],
    ["6", "5", "4", "/"],
    ["3", "2", "1", "*"],
    ["0", ".", "00", "-"],
    ["%", "=", "+", ""]
]

for row in button_texts:
    f = Frame(root, bg="grey")
    for text in row:
        if text:
            create_button(f, text, 20, 20)
    f.pack()
Button Layout: The button_texts list defines the button labels for each row.
Frame: Groups the buttons in rows.
f.pack(): Adds the frame to the window.
7. Main Loop
python
Copy code
root.mainloop()
root.mainloop(): Starts the Tkinter event loop, keeping the window open until the user closes it.
