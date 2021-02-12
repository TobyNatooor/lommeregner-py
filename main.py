
# vi har valgt at lave vores projekt med et UI biblotek kaldet tkinter
from tkinter import *
from lommeregnerClass import Lommeregner
from makeGraph import Funktion_window

# Laver start vinduet 
window = Tk()
window.title('Menu')
window.geometry("250x120+400+300")
window.resizable(0, 0)
# Knapper til at starte lommeregner og funktionsudregerne/graf
Button(window, text="Lommeregner", command=Lommeregner().createWindow, padx=20, pady=15).pack()
Button(window, text="Funktioner", command=Funktion_window, padx=28, pady=15).pack()
# for window til at starte.  
window.mainloop()
