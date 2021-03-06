from tkinter import *

root = Tk()

top_frame = Frame(root) #create an invisible container
top_frame.pack() #everything has to be packed

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

button1 = Button(top_frame, text = "Press me", fg = "red")
button2 = Button(top_frame, text = "Press me", fg = "blue")
button3 = Button(top_frame, text = "Press me", fg = "green")
button4 = Button(bottom_frame, text = "Press me", fg = "purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)


root.mainloop()