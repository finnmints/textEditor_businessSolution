from tkinter import *
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("NoteBook")

#Set size of window
root.geometry("300x150")

# Add in the page selector w scrollbar
pageLabel = Label(root, text="Pages")
pageList = Listbox(root, height=50, width=200)
pageList.insert(1, "page1")
pageList.insert(2, "page2")
pageList.insert(3, "page3")
pageList.insert(4, "page4")

scroll = Scrollbar(pageList)

pageList.pack()
scroll.pack()

# Start the GUI event loop
root.mainloop()