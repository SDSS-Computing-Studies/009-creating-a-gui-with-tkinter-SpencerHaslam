#!python3
import tkinter as tk 
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

window = tk.Tk()

dogphoto = PhotoImage(file="dog.png")
doggo = tk.Label(window, image=dogphoto)
name = tk.Label(window,text="Name")
nameen = tk.Entry(window, width=10)
buttonname = tk.Button(window,text="< Previous")
tipe = tk.Label(window,text="Type")
tipeen = tk.Entry(window, width=10)
Cdata = tk.Label(window,text="Client database")
breed = tk.Label(window,text="Breed")
breeden = tk.Entry(window, width=10)
search = tk.Button(window,text="Search by Name")
owner = tk.Label(window,text="Owner")
owneren = tk.Entry(window, width=10)
searchen = tk.Entry(window, width=10)
birth = tk.Label(window,text="Birthdate")
birthen = tk.Entry(window, width=10)
Neext = tk.Button(window,text="Next >")
button2 = tk.Button(window,text="Save Entry")

doggo.grid(row = 1, column = 1)
name.grid(row = 2, column = 1)
nameen.grid(row = 3,column = 1)
buttonname.grid(row = 4, column = 1)
tipe.grid(row = 2, column = 2)
tipeen.grid(row = 3,column = s2)
Cdata.grid(row = 1, column = 3)
breed.grid(row = 2, column = 3)
breeden.grid(row = 3,column = 3)
button2.grid(row = 4, column = 3)
search.grid(row=1,column=4,sticky=N)
owner.grid(row = 2, column = 4)
owneren.grid(row = 3,column = 4)
searchen.grid(row=1,column=5,sticky=N)
birth.grid(row = 2, column = 5)
birthen.grid(row = 3,column = 5)
Neext.grid(row = 4, column = 5)

window.mainloop()
