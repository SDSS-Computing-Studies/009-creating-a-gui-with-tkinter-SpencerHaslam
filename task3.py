#!python3
import tkinter as tk 
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

window = tk.Tk()

dogphoto = PhotoImage(file="dog.png")
doggo = tk.Label(window, image=dogphoto)
label1 = tk.Label(window,text="A cuddly little puppy! This is from the same creators who wrought you Keropi and Kero Kero.", bg="#93FCF7",wraplength = 150)



doggo.grid(row = 1, column = 1)
label1.grid(row=2, column= 1)



window.mainloop()