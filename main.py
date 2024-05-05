from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding="100 30")
frm.grid()

username = StringVar()
name = ttk.Entry(frm, textvariable=username)
name.grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

root.mainloop()

print(username.get())