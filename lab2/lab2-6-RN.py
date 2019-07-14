from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk()

buttonl = [
"7", "8", "9", "+", "*", 
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", ".",
"0", "C", "(", ")", ]

myrow = 1
mycolumn = 0
for q in buttonl:
    rel = ""
    cmd=lambda i=q: solve(i)
    ttk.Button(root, text=q, command = cmd, width = 20).grid(row = myrow, column = mycolumn)
    mycolumn += 1
    if mycolumn > 4:
        mycolumn = 0
        myrow += 1

enternum = Entry(root, width = 40)
enternum.grid(row=0, column = 0, columnspan = 5)

def solve(key):
    global memory
    if key == "=":
        ren = "0123456789.)-/*+("
        if enternum.get()[0] not in ren:
            enternum.insert(END, "enter num")
            messagebox.showerror("error, enter num")
        try:
            result = eval(enternum.get())
            enternum.insert(END, "=" + str(result))
        except:
            enternum.insert(END, "error")
            messagebox.showerror("error", "some error")
    elif key == "C":
        enternum.delete(0, END)
    elif key == "+-":
        if "=" in enternum.get():
            enternum.delete(0,END)
        try:
            if enternum.get()[0] == "-":
                enternum.delete(0)
            else:
                enternum.insert(0, "-")
        except IndexError:
            pass
    elif key == "(":
            enternum.insert(END, "(")
    elif key == ")":
            enternum.insert(END, ")")
    else:
        if "=" in enternum.get():
            enternum.delete(0, END)
        enternum.insert(END, key)

root.mainloop()    