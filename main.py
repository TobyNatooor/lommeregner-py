import tkinter as tk
from tkinter import *
from lommeregnerClass import Lommeregner
from makeGraph import Funktion_window

LR_window = lambda: Lommeregner().createWindow()

start = Tk()
start.title('Menu')
start.geometry("250x120+400+300")
start.resizable(0, 0)
tk.Button(start, text="Lommeregner", command=LR_window, padx=20, pady=15).pack()
tk.Button(start, text="Funktioner", command=Funktion_window, padx=28, pady=15).pack()
start.mainloop()
