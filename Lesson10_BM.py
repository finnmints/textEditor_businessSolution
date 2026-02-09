from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime

root = Tk()

def Write_clicked():
	with open("demofile.txt", "w") as f:
		text = Textbox.get("1.0", END)
		f.write(text)
	print("You entered:")
	print(text)

def Read_clicked():
	with open("demofile.txt", "r") as f:
		content = f.read()
		print(content)
		Textbox.insert("1.0", content)

def Red_clicked():
	root.configure(background = 'indianRed')

def Green_clicked():
	root.configure(background = 'DarkSeaGreen1')

def Blue_clicked():
	root.configure(background = 'Aliceblue')

def Yellow_clicked():
	root.configure(background = 'lemonchiffon')

WriteButton = Button(root, text="Write To File", command = Write_clicked)
ReadButton = Button(root, text="Read From File", command = Read_clicked)

Textbox = Text(root)

with open('demofile.txt', 'w') as file:
    file.write('demofile.txt')
with open('demofile.txt', 'r') as file:
    content = file.read()

menubutton = Menubutton(root, text = "Background Color")   
  
menubutton.menu = Menu(menubutton)  
menubutton["menu"]= menubutton.menu  

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

menubutton.menu.add_checkbutton(label = "Green", variable = var1, command = Green_clicked)  
menubutton.menu.add_checkbutton(label = "Yellow", variable = var2, command = Yellow_clicked)
menubutton.menu.add_checkbutton(label = "Blue", variable = var3, command = Blue_clicked)
menubutton.menu.add_checkbutton(label = "Red", variable = var4, command = Red_clicked)

WriteButton.pack()
ReadButton.pack()
Textbox.pack()
menubutton.pack()

root.mainloop()