import tkinter as tk

def close_window():
    window.destroy()

window = tk.Tk()
window.title("First try tkinter")
window.geometry("400x300")
window.mainloop()