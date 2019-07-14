from tkinter import *

import numpy as np
mlist = list(range(1,21))
print(mlist)

def addtomax():
    listbox.insert(END, 1 + max(mlist))

def addEntry():
    listbox.insert(END, txtent.get())

root = Tk()
listbox = Listbox(root)

for minlist in mlist:
    listbox.insert(END, minlist)

print(max(mlist))

fbutton = Button(root, text="press", command = addtomax)
fbutton.pack()

txtent = Entry(root)
txtent.pack()

sbutton = Button(root, text="add to list", command = addEntry)
sbutton.pack()

listbox.pack()
mainloop()
