from tkinter import *

def do_nothing():
    print("Ok ok I won't")

root = Tk()

menu_1 = Menu(root)
root.config(menu = menu_1)

sub_menu = Menu(menu_1)
menu_1.add_cascade(label = "File", menu = sub_menu) #cascade is used to add drop down menu
sub_menu.add_command(label = "New Project...", command = do_nothing)
sub_menu.add_command(label = "New...", command = do_nothing)
sub_menu.add_separator() #used to separate items in the drop down menu
sub_menu.add_command(label = "Exit", command = do_nothing)

edit_menu = Menu(menu_1)
menu_1.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Redo", command = do_nothing)

# ***** The Toolbar *****

toolbar = Frame(root, bg = "blue")
insert_button = Button(toolbar, text = "Insert Image", command = do_nothing)
insert_button.pack(side = LEFT, padx = 2, pady = 2)
print_button = Button(toolbar, text = "Print", command = do_nothing)
print_button.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X) #fill = x to grow sideways as the window expands

root.mainloop()