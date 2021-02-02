from tkinter import *
import tkinter as tk

class Lommeregner:
  def __init__(self):
    self.LRString = ""
    self.lastWasOperator = False
    self.numOfOperatorsInARow = 0
  
  def updateLabel(self):
    self.label.destroy()
    self.label = tk.Label(self.window, text=self.LRString, relief=RAISED, padx=20, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()
    print("Label: " + self.LRString)

  def insertNum(self, insert):
    self.LRString += str(insert)
    self.lastWasOperator = False
    self.numOfOperatorsInARow = 0
    self.updateLabel()

  def insertOperator(self, insert):
    if self.LRString != "":
      if self.lastWasOperator and insert != "-":
        for i in range(self.numOfOperatorsInARow):
          self.deleteLastInsert()
        self.numOfOperatorsInARow = 0
      self.LRString += str(insert)
      self.lastWasOperator = True
      self.numOfOperatorsInARow += 1
      self.updateLabel()

  def insertParenthesis(self, insert):
    if self.LRString != "":
      if insert == "(" and self.lastWasOperator:
        self.LRString += str(insert)
      if insert == ")" and not self.lastWasOperator:
        self.LRString += str(insert)
      self.updateLabel()

  def deleteLastInsert(self):
    if self.LRString != "":
      self.LRString = self.LRString[:-1]
      self.updateLabel()

  def calculate(self):
    if self.lastWasOperator:
      print("Der mangler et tal til sidst")
    else:
      result = eval(self.LRString)
      result = round(result, 2)
      self.LRString = str(result)
      self.updateLabel()

  def createWindow(self):
    self.window = Tk()
    self.window.title("Lommeregner")
    self.window.geometry("305x280+900+300")
    self.window.resizable(0, 0)

    tk.Button(self.window, text="1", command=lambda: self.insertNum("1"), width=6, height=3).place(x=5, y=40)
    tk.Button(self.window, text="2", command=lambda: self.insertNum("2"), width=6, height=3).place(x=65, y=40)
    tk.Button(self.window, text="3", command=lambda: self.insertNum("3"), width=6, height=3).place(x=125, y=40)
    tk.Button(self.window, text="4", command=lambda: self.insertNum("4"), width=6, height=3).place(x=5, y=100)
    tk.Button(self.window, text="5", command=lambda: self.insertNum("5"), width=6, height=3).place(x=65, y=100)
    tk.Button(self.window, text="6", command=lambda: self.insertNum("6"), width=6, height=3).place(x=125, y=100)
    tk.Button(self.window, text="7", command=lambda: self.insertNum("7"), width=6, height=3).place(x=5, y=160)
    tk.Button(self.window, text="8", command=lambda: self.insertNum("8"), width=6, height=3).place(x=65, y=160)
    tk.Button(self.window, text="9", command=lambda: self.insertNum("9"), width=6, height=3).place(x=125, y=160)
    tk.Button(self.window, text="0", command=lambda: self.insertNum("0"), width=6, height=3).place(x=185, y=40)
    tk.Button(self.window, text="+", command=lambda: self.insertOperator("+"), width=6, height=3).place(x=245, y=100)
    tk.Button(self.window, text="-", command=lambda: self.insertOperator("-"), width=6, height=3).place(x=245, y=160)
    tk.Button(self.window, text="*", command=lambda: self.insertOperator("*"), width=6, height=3).place(x=185, y=100)
    tk.Button(self.window, text="/", command=lambda: self.insertOperator("/"), width=6, height=3).place(x=185, y=160)
    tk.Button(self.window, text="(", command=lambda: self.insertParenthesis("("), width=2, height=3).place(x=245, y=40)
    tk.Button(self.window, text=")", command=lambda: self.insertParenthesis(")"), width=2, height=3).place(x=275, y=40)
    tk.Button(self.window, text="Udregn", command=self.calculate, padx=20, pady=15).place(x=65, y=220)
    tk.Button(self.window, text="Delete", command=self.deleteLastInsert, padx=20, pady=15).place(x=185, y=220)

    self.label = tk.Label(self.window, text="", relief=RAISED, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()
