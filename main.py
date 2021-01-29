import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import lommeregnerClass

LR = lommeregnerClass.Lommeregner()


def funktion_window():
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
start.title('Menu')
start.geometry("250x120")
Button1 = tk.Button(start, text="Funktioner", command=funktion_window, padx=28, pady=15).pack()
Button2 = tk.Button(start, text="Lommeregner", command=LR.createWindow, padx=20, pady=15).pack()
start.mainloop()
