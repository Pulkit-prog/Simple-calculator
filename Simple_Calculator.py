from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluate the expression in the screen
            value = eval(screen.get())
            scvalue.set(value)
        except Exception as e:
            # Handle any error and display 'Error' message
            scvalue.set("Error")
        screen.update()
                
    elif text == "C":
        # Clear the screen
        scvalue.set("")
        screen.update()
    
    else:
        # Append the button text to the screen value
        if scvalue.get() == "Error":
            scvalue.set("")  # Reset the screen if "Error" is present
        scvalue.set(scvalue.get() + text)
        screen.update()

# Create the main application window
root = Tk()
root.geometry("400x600")  # Adjusted size for better layout
root.title("Calculator")

# Screen for displaying the result
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold", justify=RIGHT, bd=8, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Function to create buttons dynamically
def create_button(frame, text, padx, pady):
    b = Button(frame, text=text, padx=padx, pady=pady, font="lucida 20 bold", relief=RAISED)
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-1>", click)
    return b

# Create button rows
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
        if text:  # Add only if text is not empty
            create_button(f, text, 20, 20)
    f.pack()

root.mainloop()
