import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from lommeregnerClass import Lommeregner

def function_window():
    # window code
    window = Tk()
    window.title("Funktioner")
    window.geometry("340x180+600+300")
    window.resizable(0, 0)

    tk.Label(window, text="Indsæt a, b og c værdierne af din funktion", font=("Helvetica", 12)).pack()
    tk.Label(window, text="a", width=10, relief=RAISED).place(x=55, y=35)
    aInput = tk.Entry(window, width=12)
    aInput.place(x=55, y=60)
    tk.Label(window, text="b", width=10, relief=RAISED).place(x=135, y=35)
    bInput = tk.Entry(window, width=12)
    bInput.place(x=135, y=60)
    tk.Label(window, text="c", width=10, relief=RAISED).place(x=215, y=35)
    cInput = tk.Entry(window, width=12)
    cInput.place(x=215, y=60)
    
    def makeGraph():
      a = aInput.get()
      b = bInput.get()
      c = cInput.get()
      print(f"a: {a}  b: {b}  c: {c}")

    tk.Button(window, text="Lav graf", command=makeGraph, padx=15).place(x=140, y=90)
    window.mainloop()

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



LR_window = lambda: Lommeregner().createWindow()

start = Tk()
start.title('Menu')
start.geometry("250x120+400+300")
start.resizable(0, 0)
tk.Button(start, text="Lommeregner", command=LR_window, padx=20, pady=15).pack()
tk.Button(start, text="Funktioner", command=function_window, padx=28, pady=15).pack()
start.mainloop()
