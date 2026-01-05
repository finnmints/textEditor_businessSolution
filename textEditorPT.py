from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime

# Create the main window
root = Tk()
root.title("NoteBook")
root.configure(background = 'DarkSeaGreen1')

#New page button
button = tk.Button(root, text="New Page", command = button_clicked, background="DarkSeaGreen2", font = ("Courier New", 50))

#Set size of window
root.geometry("1000x800")

# Add in the page selector 
pageLabel = Label(root, text="Pages", background = "DarkSeaGreen1", font = ("Courier New", 80, "bold"))

pageList = Listbox(root, height=30, width=60)
pageList.insert(1, "page1")
pageList.insert(2, "page2")
pageList.insert(3, "page3")
pageList.insert(4, "page4")

pageList.grid(row = 1, column = 3, padx = 250)
pageLabel.grid(row = 0, column = 3, pady = 20)

#Creating the menu button
menubutton = Menubutton(root, text = "Background Color")   
  
menubutton.menu = Menu(menubutton)  
menubutton["menu"]= menubutton.menu  

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

menubutton.menu.add_checkbutton(label = "Green", variable = var1)  
menubutton.menu.add_checkbutton(label = "Yellow", variable = var2)
menubutton.menu.add_checkbutton(label = "Blue", variable = var3)
menubutton.menu.add_checkbutton(label = "Red", variable = var4)

menubutton.grid(row = 2, column = 3, padx = 350)


# Start the GUI event loop
root.mainloop()

