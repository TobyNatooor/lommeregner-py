import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import numpy as np
import lommeregnerClass

def function_window():
    # window code
    window = Tk()
    window.title("Funktioner")
    window.geometry("312x324+600+300")
    window.resizable(0, 0)

    functionInput = tk.Entry(window)
    functionInput.pack()
    
    def makeGraph():
      theFunction = functionInput.get()
      print(theFunction)

      if "^" in theFunction:
        print("dette er en andengradsfunktion")
        theFunction.replace("^", "**")

        x = np.linspace(-5, 5, 100)
        y = theFunction
        fig = plt.figure()
        plt.plot(x, y, 'r')
        plt.show()

    tk.Button(window, text="Lav graf", command=makeGraph).pack()
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


LR_window = lambda: lommeregnerClass.Lommeregner().createWindow()

start = Tk()
start.title('Menu')
start.geometry("250x120+400+300")
start.resizable(0, 0)
tk.Button(start, text="Lommeregner", command=LR_window, padx=20, pady=15).pack()
tk.Button(start, text="Funktioner", command=function_window, padx=28, pady=15).pack()
start.mainloop()
