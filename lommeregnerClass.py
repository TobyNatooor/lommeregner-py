
from tkinter import *

#Vi har valgt at lave lommeregneren med en class
class Lommeregner:
  def __init__(self):
    self.display = "" # Variablet der viser udreginingen
    self.lastWasOperator = False
    self.numOfOpsInARow = 0 
    self.startParenthesis = 0 # varibel til at tjekke om der er både start og slut parenthesis.
    self.endParenthesis = 0 # varibel til at tjekke om der er både start og slut parenthesis.

  #Funktionen updatere stringen display  
  def updateLabel(self):
    self.label.destroy()
    self.label = Label(self.window, text=self.display, relief=RAISED, padx=20, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()
    print(self.display)

  #Insætter tal til display
  def insertNum(self, insert):
    self.display += str(insert)
    self.lastWasOperator = False
    self.numOfOpsInARow = 0
    self.updateLabel()

  #Insætter +, -, * eller / til display
  def insertOperator(self, insert):
    if self.display != "":
      if self.lastWasOperator and insert != "-":
        for i in range(self.numOfOpsInARow):
          self.deleteLastInsert()
        self.numOfOpsInARow = 0
      self.display += str(insert)
      self.lastWasOperator = True
      self.numOfOpsInARow += 1
      self.updateLabel()

  #Insætter parenteser til display
  def insertParenthesis(self, insert):
    if insert == "(" and self.lastWasOperator or self.display == "" or self.display[-1] == "(":
      self.startParenthesis += 1
      self.display += str(insert)
    elif insert == ")" and not self.lastWasOperator and not self.startParenthesis == self.endParenthesis:
      self.endParenthesis += 1
      self.display += str(insert)
    self.updateLabel()

  #Sletter det sidste tegn på string display
  def deleteLastInsert(self):
    if self.display != "":
      self.display = self.display[:-1]
      self.updateLabel()

  #Regner display ud og ændrer sig selv til den udregning
  def calculate(self):
    if self.lastWasOperator:
      print("Der mangler et tal til sidst")
    elif not self.startParenthesis == self.endParenthesis:
      print("En eller flere parenteser mangler at blive lukket")
    else:
      result = eval(self.display)
      result = round(result, 2)
      self.display = str(result)
      self.updateLabel()

  #Sletter alt i display
  def clearLabel(self):
    self.display = ""
    self.updateLabel()

  #Funktionen laver lommeregner vinduet og UI
  def createWindow(self):
    self.window = Tk()
    self.window.title("Lommeregner")
    self.window.geometry("305x280+900+300")
    self.window.resizable(0, 0)
    
    #Label der viser string display
    self.label = Label(self.window, text=self.display, relief=RAISED, pady=5, width=350, font=("Helvetica", 16))
    self.label.pack()
    #Knapperne
    Button(self.window, text="1", command=lambda: self.insertNum("1"), width=6, height=3).place(x=5, y=40)
    Button(self.window, text="2", command=lambda: self.insertNum("2"), width=6, height=3).place(x=65, y=40)
    Button(self.window, text="3", command=lambda: self.insertNum("3"), width=6, height=3).place(x=125, y=40)
    Button(self.window, text="4", command=lambda: self.insertNum("4"), width=6, height=3).place(x=5, y=100)
    Button(self.window, text="5", command=lambda: self.insertNum("5"), width=6, height=3).place(x=65, y=100)
    Button(self.window, text="6", command=lambda: self.insertNum("6"), width=6, height=3).place(x=125, y=100)
    Button(self.window, text="7", command=lambda: self.insertNum("7"), width=6, height=3).place(x=5, y=160)
    Button(self.window, text="8", command=lambda: self.insertNum("8"), width=6, height=3).place(x=65, y=160)
    Button(self.window, text="9", command=lambda: self.insertNum("9"), width=6, height=3).place(x=125, y=160)
    Button(self.window, text="0", command=lambda: self.insertNum("0"), width=6, height=3).place(x=185, y=40)
    Button(self.window, text="+", command=lambda: self.insertOperator("+"), width=6, height=3).place(x=245, y=100)
    Button(self.window, text="-", command=lambda: self.insertOperator("-"), width=6, height=3).place(x=245, y=160)
    Button(self.window, text="*", command=lambda: self.insertOperator("*"), width=6, height=3).place(x=185, y=100)
    Button(self.window, text="/", command=lambda: self.insertOperator("/"), width=6, height=3).place(x=185, y=160)
    Button(self.window, text="(", command=lambda: self.insertParenthesis("("), width=2, height=3).place(x=245, y=40)
    Button(self.window, text=")", command=lambda: self.insertParenthesis(")"), width=2, height=3).place(x=275, y=40)
    Button(self.window, text="Udregn", command=self.calculate, padx=20, pady=15).place(x=25, y=220)
    Button(self.window, text="Delete", command=self.deleteLastInsert, padx=20, pady=15).place(x=115, y=220)
    Button(self.window, text="Clear", command=self.clearLabel, padx=20, pady=15).place(x=205, y=220)
