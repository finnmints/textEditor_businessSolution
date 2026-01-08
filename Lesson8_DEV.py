from tkinter import *
from tkmacosx import Button
from tkinter.ttk import * 
from time import strftime

button1 = tk.Button(root, text="Button 1!", command = button1_clicked)
button2 = tk.Button(root, text="Button 2!", command = button2_clicked)
button3 = tk.Button(root, text="Button 3!", command = button3_clicked)

Label1 = Label(root, text= T1)
Label2 = Label(root, text= T2)
Label3 = Label(root, text= T3)
T1 = Text(root)
T2 = Text(root)
T3 = Text(root)

def button1_clicked():
	root.title(T.get("Updated 1!", END))