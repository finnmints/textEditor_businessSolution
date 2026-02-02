from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime

root = Tk()

def Write_clicked():
	with open("demofile.txt", "w") as f:
		f.write("")
	text = Textbox.get("1.0", END)
	print("You entered:")
	print(text)

def Read_clicked():
	with open("demofile.txt", "r") as f:
		content = f.read()
		print(content)
		Textbox.insert("1.0", content)

WriteButton = Button(root, text="Write To File", command = Write_clicked)
ReadButton = Button(root, text="Read From File", command = Read_clicked)

Textbox = Text(root)

with open('demofile.txt', 'w') as file:
    file.write('Textbox')
with open('demofile.txt', 'r') as file:
    content = file.read()

WriteButton.pack()
ReadButton.pack()
Textbox.pack()

root.mainloop()