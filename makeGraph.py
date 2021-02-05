import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

def Funktion_window():
    # window code
    window = Tk()
    window.title("Funktioner")
    window.geometry("320x324")
    window.resizable(0, 0)
    tk.Label(window, text="Indsæt a, b og c værdierne af din funktion",
             font=("Helvetica", 12)).pack()
    tk.Label(window, text="a", width=10, relief=RAISED).place(x=55, y=35)
    aInput = tk.Entry(window, width=12)
    aInput.place(x=55, y=60)
    tk.Label(window, text="b", width=10, relief=RAISED).place(x=135, y=35)
    bInput = tk.Entry(window, width=12)
    bInput.place(x=135, y=60)
    tk.Label(window, text="c", width=10, relief=RAISED).place(x=215, y=35)
    cInput = tk.Entry(window, width=12)
    cInput.place(x=215, y=60)

    # graph

    def makeGraph():
      # variabel

      limit = 10
      x = -10
      a = int(aInput.get())
      b = int(bInput.get())
      c = int(cInput.get())
      x_list = []
      y_list = []
      print(a, b, c)
      # udregning

      while x <= limit:
          y_list.append(eval("a*(x*x)+x*b+c"))
          x_list.append(x)
          x = x + 1
      print(x_list, y_list)
      plt.plot(x_list, y_list)
      plt.show()
    #style

    plt.grid(color='black', linestyle='-', linewidth=0.3)
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    plt.locator_params(axis='y', nbins=20)
    plt.locator_params(axis='x', nbins=20)

    tk.Button(window, text="Lav graf", command=makeGraph,
              padx=15).place(x=140, y=90)
    window.mainloop()
