from tkinter import *
import tkinter as tk

class Lommeregner:
  def __init__(self):
    self.LRLabel = ""
    self.lastWasOperator = False
    self.numOfOperatorsInARow = 0
    self.startParenthesis = 0
    self.endParenthesis = 0
  
  def updateLabel(self):
    self.label.destroy()
    self.label = tk.Label(self.window, text=self.LRLabel, relief=RAISED, padx=20, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()
    print("Label: " + self.LRLabel)

  def insertNum(self, insert):
    self.LRLabel += str(insert)
    self.lastWasOperator = False
    self.numOfOperatorsInARow = 0
    self.updateLabel()

  def insertOperator(self, insert):
    if self.LRLabel != "":
      if self.lastWasOperator and insert != "-":
        for i in range(self.numOfOperatorsInARow):
          self.deleteLastInsert()
        self.numOfOperatorsInARow = 0
      self.LRLabel += str(insert)
      self.lastWasOperator = True
      self.numOfOperatorsInARow += 1
      self.updateLabel()

  def insertParenthesis(self, insert):
    if insert == "(" and self.lastWasOperator or self.LRLabel == "" or self.LRLabel[-1] == "(":
      self.startParenthesis += 1
      self.LRLabel += str(insert)
    elif insert == ")" and not self.lastWasOperator and not self.startParenthesis == self.endParenthesis:
      self.endParenthesis += 1
      self.LRLabel += str(insert)
    self.updateLabel()

  def deleteLastInsert(self):
    if self.LRLabel != "":
      self.LRLabel = self.LRLabel[:-1]
      self.updateLabel()

  def calculate(self):
    if self.lastWasOperator:
      print("Der mangler et tal til sidst")
    elif not self.startParenthesis == self.endParenthesis:
      print("En eller flere parenteser mangler at blive lukket")
    else:
      result = eval(self.LRLabel)
      result = round(result, 2)
      self.LRLabel = str(result)
      self.updateLabel()

  def clearLabel(self):
    self.LRLabel = ""
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
    tk.Button(self.window, text="Udregn", command=self.calculate, padx=20, pady=15).place(x=25, y=220)
    tk.Button(self.window, text="Delete", command=self.deleteLastInsert, padx=20, pady=15).place(x=115, y=220)
    tk.Button(self.window, text="Clear", command=self.clearLabel, padx=20, pady=15).place(x=205, y=220)
    self.label = tk.Label(self.window, text="", relief=RAISED, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()
