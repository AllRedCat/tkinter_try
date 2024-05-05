from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding="100 30")
frm.grid()

user_label = ttk.Label(frm, text="Username").grid(column=0, row=0)

username = StringVar()
name = ttk.Entry(frm, textvariable=username).grid(column=0, row=1)

pass_label = ttk.Label(frm, text="Password").grid(column=0, row=2)

password = StringVar()
passw = ttk.Entry(frm, textvariable=password, show="*").grid(column=0, row=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=99)

root.mainloop()

print(username.get())
print(password.get())