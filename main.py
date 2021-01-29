import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
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
    # udregning af funktion
    x = 0
    # while x <= 10:
    # y_list.append(eval(ligning))
    # x_list.appendlist

    # graf del.
    #plt.plot(x_list, y_list)


start = Tk()
start.title('Lommeregner')
start.geometry("250x100")
Button1 = tk.Button(start, text="Funktioner", command=Funktion_window).pack()
Button2 = tk.Button(start, text="Lommeregner", command=LR.window).pack()
start.mainloop()
