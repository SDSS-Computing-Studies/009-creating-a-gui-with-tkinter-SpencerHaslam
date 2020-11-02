#!python3
import tkinter as tk 
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

window = tk.Tk()

entry1 = tk.Entry(window, width=10)
entry2 = tk.Entry(window, width=10)
entry3 = tk.Entry(window, width=10)
label1 = tk.Label(window,text="x")
label2 = tk.Label(window,text="=")



entry1.grid(row = 1, column = 1)
label1.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
label2.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)
window.mainloop()