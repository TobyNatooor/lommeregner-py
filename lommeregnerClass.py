from tkinter import *
import tkinter as tk

class Lommeregner:
  def __init__(self):
    self.LRInput = ""
    self.lastWasOperator = False
  
  def updateLabel(self):
    self.label.destroy()
    self.label = tk.Label(self.window, text=self.LRInput, relief=RAISED, padx=20, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()

  def insertNum(self, insert):
    self.LRInput += str(insert)
    self.lastWasOperator = False
    self.updateLabel()

  def insertOperator(self, insert):
    if 0 < len(self.LRInput):
      if self.lastWasOperator:
        self.delete()
      self.LRInput += str(insert)
      self.lastWasOperator = True
      self.updateLabel()

  def delete(self):
    if self.LRInput != "":
      self.LRInput = self.LRInput[:-1]
      self.updateLabel()

  def calculate(self):
    result = eval(self.LRInput)
    result = round(result, 2)
    self.LRInput = str(result)
    self.updateLabel()
    print(result)

  def createWindow(self):
    self.window = Tk()
    self.window.title("Lommeregner")
    self.window.geometry("305x280")
    self.window.resizable(0, 0)

    tk.Button(self.window, text="1", command=lambda: self.insertNum("1"), padx=20, pady=15).place(x=5, y=40)
    tk.Button(self.window, text="2", command=lambda: self.insertNum("2"), padx=20, pady=15).place(x=65, y=40)
    tk.Button(self.window, text="3", command=lambda: self.insertNum("3"), padx=20, pady=15).place(x=125, y=40)
    tk.Button(self.window, text="4", command=lambda: self.insertNum("4"), padx=20, pady=15).place(x=5, y=100)
    tk.Button(self.window, text="5", command=lambda: self.insertNum("5"), padx=20, pady=15).place(x=65, y=100)
    tk.Button(self.window, text="6", command=lambda: self.insertNum("6"), padx=20, pady=15).place(x=125, y=100)
    tk.Button(self.window, text="7", command=lambda: self.insertNum("7"), padx=20, pady=15).place(x=5, y=160)
    tk.Button(self.window, text="8", command=lambda: self.insertNum("8"), padx=20, pady=15).place(x=65, y=160)
    tk.Button(self.window, text="9", command=lambda: self.insertNum("9"), padx=20, pady=15).place(x=125, y=160)
    tk.Button(self.window, text="0", command=lambda: self.insertNum("0"), padx=20, pady=15).place(x=185, y=40)
    tk.Button(self.window, text="+", command=lambda: self.insertOperator("+"), padx=20, pady=15).place(x=245, y=100)
    tk.Button(self.window, text="-", command=lambda: self.insertOperator("-"), padx=20, pady=15).place(x=245, y=160)
    tk.Button(self.window, text="*", command=lambda: self.insertOperator("*"), padx=20, pady=15).place(x=185, y=100)
    tk.Button(self.window, text="/", command=lambda: self.insertOperator("/"), padx=20, pady=15).place(x=185, y=160)
    tk.Button(self.window, text="Udregn", command=self.calculate, padx=20, pady=15).place(x=65, y=220)
    tk.Button(self.window, text="Delete", command=self.delete, padx=20, pady=15).place(x=185, y=220)

    self.label = tk.Label(self.window, text="", relief=RAISED, padx=20, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()

