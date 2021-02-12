import matplotlib.pyplot as plt
from tkinter import *


def Funktion_window():
    # graph
    def makeGraph():
      # variabel
      limit = 40
      x = -40
      a = float(aInput.get())
      b = float(bInput.get())
      c = float(cInput.get())
      x_list = []
      y_list = []
      print(a, b, c)

      # udregning graph
      while x <= limit:
          y_list.append(eval("a*(x*x)+x*b+c"))
          x_list.append(x)
          x = x + 0.25
      plt.plot(x_list, y_list)

      #udregning af tal (d, toppunkt og x skæringspunkter)
      d = round(((b*b) - (4*a*c)), 3)
      ls1 = round(((-b + (d**0.5).real) / (2 * a)), 3)
      ls2 = round(((-b - (d**0.5).real) / (2 * a)) ,3)
      topx = round((-b / (2*a)), 3)
      topy = round((-d / (4*a)), 3)

      displayTalString = f"diskriminant: {d}\n  x1: {ls1}    x2: {ls2}\n toppunkt: ({topx},{topy})"
      Label(window, text=displayTalString, relief=RAISED, padx=130, font=("Helvetica", 12)).pack(side=BOTTOM)
      
      #style
      plt.grid(color='black', linestyle='-', linewidth=0.3) 
      plt.axhline(y=0, color="black")
      plt.axvline(x=0, color="black")
      plt.locator_params(axis='y', nbins=20)
      plt.locator_params(axis='x', nbins=20)
      plt.show()

    #Laver vinduet og UI
    window = Tk()
    window.title("Funktioner")
    window.geometry("340x200")
    window.resizable(0, 0)
    Label(window, text="Indsæt a, b og c værdierne af din funktion", font=("Helvetica", 12)).pack()
    Label(window, text="a", width=10, relief=RAISED).place(x=55, y=35)
    aInput = Entry(window, width=12)
    aInput.place(x=55, y=60)
    Label(window, text="b", width=10, relief=RAISED).place(x=135, y=35)
    bInput = Entry(window, width=12)
    bInput.place(x=135, y=60)
    Label(window, text="c", width=10, relief=RAISED).place(x=215, y=35)
    cInput = Entry(window, width=12)
    cInput.place(x=215, y=60)
    Button(window, text="Lav graf", command=makeGraph, padx=15).place(x=140, y=90)
    window.mainloop()
    