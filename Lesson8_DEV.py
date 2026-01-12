from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime
import random

root= Tk()

def button1_clicked():
	Label1.config(text="Updated 1!")
def button2_clicked():
	Label2.config(text="Updated 2!")
	Label3.config(text="Updated 3!")
def randomize():
	textList = random.randint(1, 6)
	if textList==6:
		Label3.config(text="RANDOMLY PICKED!")
	if textList==5:
		Label2.config(text="RANDOMLY PICKED!")
	if textList==4:
		Label1.config(text="RANDOMLY PICKED!")
	if textList==3:
		button3.config(text="RANDOMLY PICKED!")
	if textList==2:
		button2.config(text="RANDOMLY PICKED!")
	if textList==1:
		button1.config(text="RANDOMLY PICKED!")
	

root.geometry("300x150")

button1 = Button(root, text="Button 1!", command = button1_clicked)
button2 = Button(root, text="Button 2!", command = button2_clicked)
button3 = Button(root, text="Button 3!", command = button3_clicked)
randButt = Button(root, text="Random Button!", command = randomize)

Label1 = Label(root, text= "Label 1")
Label2 = Label(root, text= "Label 2")
Label3 = Label(root, text= "Label 3")

button1.pack()
button2.pack()
button3.pack()
randButt.pack()
Label1.pack()
Label2.pack()
Label3.pack()

root.mainloop()