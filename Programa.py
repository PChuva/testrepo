from tkinter import *

root = Tk ()

def myclick():
    text_on = Label (root, text = "Look it's working!!!")
    return text_on.grid()
Mylabel = Label (root, text = "Pedro APP", fg = "Red")
Mylabel.grid(row = 0, column =0)
Mybotton = Button(root, text = "Nome", padx = 50, pady = 50, fg = "Red", bg ="Brown", command = myclick)
Mybotton.grid(row = 2, column = 0)
mybutton2 = Button(root, text = "Age")
mybutton2.grid(row = 7, column =0)
canvas = Canvas(root, height = 680, width = 1500)
canvas.grid(row = 100, column = 100)
root.mainloop()
