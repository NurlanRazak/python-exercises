from tkinter import *
# #1

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


# # 2

def firfunc():
    # print("Button1 was pressed")
    feedback_text.set("Button 1 has been pressed")

def secfunc():
    # print("Button2 was pressed")
    feedback_text.set("Button 2 has been pressed")

root = Tk()

feedback_text = StringVar() 
feedback_text.set("No button pressed")
label1 = Label(root, textvariable=feedback_text)

firstbutton = Button(root, text="Button1", command = firfunc)
secondbutton = Button(root, text="Button2", command = secfunc)

label1.pack()
firstbutton.pack()
secondbutton.pack()

mainloop()

# # 3

def make_circle(event):
    can.create_oval(event.x, event.y, event.x+20, event.y+20)

def delcircle():
    can.delete(ALL)    

def quitreal():
    root.destroy()
root = Tk()

menubar = Menu(root)

can = Canvas(root, width = 400, height = 400)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "Clear", command = delcircle)
filemenu.add_command(label = "Exit", command = quitreal)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


can.pack()

can.bind("<Button-1>", make_circle)
mainloop()

# #4
root = Tk()
can = Canvas(root, bg = "white")
can.grid(row=0, column=4, columnspan=2, rowspan=2)

def make_circle(event):
    can.create_oval(event.x, event.y, event.x+20, event.y+20)
def make_square(event):
    can.create_rectangle(event.x, event.y, event.x+20, event.y+20)
def make_line(event):
    can.create_line(event.x, event.y, event.x+20, event.y+20)

def bindcircle():
    can.bind("<Button-1>", make_circle)
    print("after binding")

def bindsquare():
    can.bind("<Button-1>", make_square)
    print("after binding")

def bindline():
    can.bind("<Button-1>", make_line)
    print("after binding")

but1 = Button(root, text="Circle", command = bindcircle)
but2 = Button(root, text="Square", command = bindsquare)
but3 = Button(root, text="Line", command = bindline)
but4 = Button(root, text="Canvas")

but1.grid(row=0, column=0)
but2.grid(row=1, column=0)
but3.grid(row=2, column=0)
but4.grid(row=3, column=0)


mainloop()

# 5 
root = Tk()
can = Canvas(root, bg = "white")
can.grid(row=0, column=4, columnspan=2, rowspan=2)

def make_circle(event):
    can.create_oval(event.x, event.y, event.x+20, event.y+20)
def make_square(event):
    can.create_rectangle(event.x, event.y, event.x+20, event.y+20)
def make_line(event):
    can.create_line(event.x, event.y, event.x+20, event.y+20)

def bindcircle():
    can.bind("<Button-1>", make_circle)
    print("after binding")

def bindsquare():
    can.bind("<Button-1>", make_square)
    print("after binding")

def bindline():
    can.bind("<Button-1>", make_line)
    print("after binding")



def delcircle():
    if(messagebox.askokcancel("Del?", "Are you sure?")):
        print("user said yes")
        can.delete(ALL)      
    else:
        print("cancel")  
    #can.delete(ALL)    

def quitreal():
    if(messagebox.askokcancel("Exit?", "Are you sure?")):
        print("user said yes")
        root.destroy()    
    else:
        print("cancel")
    # root.destroy()

menubar = Menu(root)
from tkinter import messagebox

filemenu = Menu(menubar, tearoff=0)


filemenu.add_command(label = "Clear", command = delcircle)
filemenu.add_command(label = "Exit", command = quitreal)

menubar.add_cascade(label="File", menu=filemenu)


but1 = Button(root, text="Circle", command = bindcircle)
but2 = Button(root, text="Square", command = bindsquare)
but3 = Button(root, text="Line", command = bindline)
but4 = Button(root, text="Canvas")

but1.grid(row=0, column=0)
but2.grid(row=1, column=0)
but3.grid(row=2, column=0)
but4.grid(row=3, column=0)

root.config(menu=menubar)
mainloop()