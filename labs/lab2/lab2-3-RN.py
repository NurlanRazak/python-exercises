from tkinter import *

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
