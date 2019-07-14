from tkinter import *

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