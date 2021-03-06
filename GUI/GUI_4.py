from tkinter import *

root = Tk()

label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 0, sticky = E) # E is to place it on the right. Sticky take the arguments (N,E,S,W)
label_2.grid(row = 1, sticky = E)

entry_1.grid(row = 0, column = 1) #places it in rows and columns starting from 0
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text = "Keep me logged in")
c.grid(columnspan = 2)

root.mainloop()