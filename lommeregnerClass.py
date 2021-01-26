from tkinter import *
import tkinter as tk

class Lommeregner:
  def __init__(self):
    self.LRInput = ""
  
  def updateLabel(self):
    self.label.destroy()
    self.label = tk.Label(self.window, text=self.LRInput, relief=RAISED, padx=20, pady=5)
    self.label.pack()

  def insertLabel(self, insert):
    self.LRInput += str(insert)
    self.updateLabel()
    print(self.LRInput)

  def delete(self):
    if self.LRInput != "":
      self.LRInput = self.LRInput[:-1]
    self.updateLabel()

  def window(self):
    self.window = Tk()
    self.window.title("Lommeregner")
    self.window.geometry("340x320")
    self.window.resizable(0, 0)
    self.window.title('LommeregnerXXX')
    button1 = tk.Button(self.window, text="1", command=lambda: self.insertLabel(1), padx=20, pady=15)
    button1.place(x=5, y=40)
    button2 = tk.Button(self.window, text="2", command=lambda: self.insertLabel(2), padx=20, pady=15)
    button2.place(x=65, y=40)
    button3 = tk.Button(self.window, text="3", command=lambda: self.insertLabel(3), padx=20, pady=15)
    button3.place(x=125, y=40)
    button4 = tk.Button(self.window, text="4", command=lambda: self.insertLabel(4), padx=20, pady=15)
    button4.place(x=5, y=100)
    button5 = tk.Button(self.window, text="5", command=lambda: self.insertLabel(5), padx=20, pady=15)
    button5.place(x=65, y=100)
    button6 = tk.Button(self.window, text="6", command=lambda: self.insertLabel(6), padx=20, pady=15)
    button6.place(x=125, y=100)
    button7 = tk.Button(self.window, text="7", command=lambda: self.insertLabel(7), padx=20, pady=15)
    button7.place(x=5, y=160)
    button8 = tk.Button(self.window, text="8", command=lambda: self.insertLabel(8), padx=20, pady=15)
    button8.place(x=65, y=160)
    button9 = tk.Button(self.window, text="9", command=lambda: self.insertLabel(9), padx=20, pady=15)
    button9.place(x=125, y=160)
    button0 = tk.Button(self.window, text="0", command=lambda: self.insertLabel(0), padx=20, pady=15)
    button0.place(x=185, y=40)
    buttonDelete = tk.Button(self.window, text="Delete", command=self.delete, padx=20, pady=15)
    buttonDelete.place(x=245, y=40)
    self.label = tk.Label(self.window, text="---", relief=RAISED, padx=20, pady=5)
    self.label.pack()


