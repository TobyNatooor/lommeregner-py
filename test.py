import matplotlib.pyplot as plt
import numpy as np


class opdelFunktionen():
  num1, num2, num3 = "", "", ""
  op1, op2, op3 = "", "", ""
  
  def __init__(self, theFunction):
    led = 0
    if not theFunction[0] == "-" or theFunction[0] == "+":
      theFunction = "+" + theFunction

    for i in theFunction:
        if i == "+" or i == "-":
          led += 1
          if led == 1: self.op1 = i
          if led == 2: self.op2 = i
          if led == 3: self.op3 = i
        else:
          if led == 1: self.num1 += i
          if led == 2: self.num2 += i
          if led == 3: self.num3 += i

    print("num1: " + self.num1 + "    num2: " + self.num2 + "     num3: " + self.num3)
    print("op1: " + self.op1 + "    op2: " + self.op2 + "     op3: " + self.op3)

    if "*x" in self.num2:
      self.num2 = self.num2.replace("*x", "")
    else:
      self.num3 = self.num2
      self.num2 = ""
      self.op3 = self.op2
      self.op2 = ""

    if "x^" in self.num1: 
      self.num1 = self.num1.replace("x^", "")
    else:
      self.num2 = self.num1
      self.num1 = ""
      self.op2 = self.op1
      self.op1 = ""

    print("num1: " + self.num1 + "    num2: " + self.num2 + "     num3: " + self.num3)
    print("op1: " + self.op1 + "      op2: " + self.op2 + "       op3: " + self.op3)

    self.num1 = int(self.num1)
    self.num2 = int(self.num2)
    self.num3 = int(self.num3)
    #self.op1, self.op2, self.op3 = "", "", ""


    
test = opdelFunktionen("-x^2+5*x-667")
print(test.op3)

x = np.linspace(-5, 5, 100)
if test.op1 == '-':
  x = -(x)
y = pow(x, test.num1) + test.num2*x + test.num3
fig = plt.figure()
plt.plot(x, y, 'r')
plt.show()



