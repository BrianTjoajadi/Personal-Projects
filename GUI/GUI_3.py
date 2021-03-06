from tkinter import *

root = Tk()

one = Label(root, text = "One", bg = "red", fg = "white")
one.pack()
two = Label(root, text = "Two", bg = "blue", fg = "white")
two.pack(fill=X) #makes it grow in length based on the length of the window
three = Label(root, text = "Three", bg = "black", fg = "white")
three.pack(side = LEFT, fill = Y) #makes it grow in width based on the width of the window



root.mainloop()