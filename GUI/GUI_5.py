from tkinter import *

root = Tk()

# def print_name():
#     print("Hello my name is Brian")

# button_1 = Button(root, text = "Print my name", command = print_name) #binding print_name function to widget
# button_1.pack()

def print_name(event): #event is the click of a mouse button, keyboard, etc.
    print("Hellow my name is Brian")

button_1 = Button(root, text = "Print my name")
button_1.bind("<Button-1>", print_name)
button_1.pack()




root.mainloop()