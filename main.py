import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
import lommeregnerClass

LR = lommeregnerClass.Lommeregner()


def Funktion_window():
    # window code
    window = Tk()
    window.title("Funktioner")
    window.geometry("312x324")
    window.resizable(0, 0)
    # main varibels
    x_list = []
    y_list = []
    ligning = ""
    # graf del.
    plt.plot(x_list, y_list)


start = Tk()
start.title('Lommeregner')
start.geometry("250x100")

Button1 = tk.Button(start, text="Funktioner", command=Funktion_window)
Button1.pack()
Button2 = tk.Button(start, text="Lommeregner", command=LR.window)
Button2.pack()

start.mainloop()
