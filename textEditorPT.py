from tkinter import *
from tkmacosx import Button

# Add in the page selector w scrollbar
pageList = Listbox()
pageList.insert(1, "page1")
pageList.insert(2, "page2")
pageList.insert(3, "page3")
pageList.insert(4, "page4")

scroll = Scrollbar(pageList)

pageList.pack()
scroll.pack()