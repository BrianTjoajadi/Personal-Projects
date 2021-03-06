from tkinter import *


class BrianButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text = "Print Message", command = self.print_message)
        self.print_button.pack(side = LEFT)

        self.quit_button = Button(frame, text = "Quit", command = frame.quit)
        self.quit_button.pack(side = LEFT)
    
    def print_message(self):
        print("Wow, this actually worked!")


root = Tk()
b = BrianButtons(root)
root.mainloop()