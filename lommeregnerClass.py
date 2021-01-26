from tkinter import *
import tkinter as tk

class Lommeregner:
  def __init__(self):
    self.LRInput = ""
  
  def updateLabel(self):
    self.label.destroy()
    self.label = tk.Label(self.window, text=self.LRInput, relief=RAISED)
    self.label.pack()

  def insertLabel(self, insert):
    self.LRInput += str(insert)
    self.updateLabel()
    print(self.LRInput)

  def window(self):
    self.window = Tk()
    self.window.title("Lommeregner")
    self.window.geometry("312x324")
    self.window.resizable(0, 0)
    self.window.title('LommeregnerXXX')
    button1 = tk.Button(self.window, text="1", command=lambda: self.insertLabel(1))
    button1.pack()
    button2 = tk.Button(self.window, text="2", command=lambda: self.insertLabel(2))
    button2.pack()
    self.label = tk.Label(self.window, text="Tryk på knapperne", relief=RAISED)
    self.label.pack()


