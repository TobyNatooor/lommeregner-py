# vi har valgt at lave vores projekt med et UI biblotek 
from tkinter import *
from lommeregnerClass import Lommeregner
from makeGraph import Funktion_window

# Laver start vinduet
window = Tk()
window.title('Menu')
window.geometry("250x120+400+300")
window.resizable(0, 0)
Button(window, text="Lommeregner", command=Lommeregner().createWindow, padx=20, pady=15).pack()
Button(window, text="Funktioner", command=Funktion_window, padx=28, pady=15).pack()
window.mainloop()
