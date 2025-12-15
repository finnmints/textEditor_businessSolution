from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime

# Create the main window
root = Tk()
root.title("NoteBook")

#Set size of window
root.geometry("500x300")

# Add in the page selector 
pageLabel = Label(root, text="Pages")
pageList = Listbox(root, height=10, width=20)
pageList.insert(1, "page1")
pageList.insert(2, "page2")
pageList.insert(3, "page3")
pageList.insert(4, "page4")

pageList.pack()
pageLabel.pack()

# Creating Menubar
menubar = Menu(root)

# Adding color Menu
color = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Color', menu = color)
color.add_command(label ='Green', command = None)
color.add_separator()
color.add_command(label ='Yellow', command = None)
color.add_separator()
color.add_command(label ='Blue', command = None)
color.add_separator()
color.add_command(label ='Red', command = None)

# display Menu
root.config(menu = menubar)
mainloop()

# Start the GUI event loop
root.mainloop()