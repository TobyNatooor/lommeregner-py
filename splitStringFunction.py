class SplitStringFunction():
  def __init__(self, theFunction):
    self.op1, self.op2, self.op3 = "", "", ""
    self.num1, self.num2, self.num3 = "", "", ""
    self.power = ""
    self.part = 0
    
    if not theFunction[0] == "-":
      theFunction = "+" + theFunction

    for i in theFunction:
        if i == "+" or i == "-":
          self.part += 1
          if self.part == 1:
            self.op1 = i
          if self.part == 2:
            self.op2 = i
          if self.part == 3:
            self.op3 = i
        else:
          if self.part == 1:
            self.num1 += i
          if self.part == 2:
            self.num2 += i
          if self.part == 3:
            self.num3 += i

    if "*x" in self.num2:
      self.num2 = self.num2.replace("*x", "")
    else:
      self.num3 = self.num2
      self.num2 = ""
      self.op3 = self.op2
      self.op2 = ""

    if "x^" in self.num1:
      if self.num1[0] == "x":
        self.num1 = "1" + self.num1
      self.num1 = self.num1.split("x^")
      self.power = self.num1[1]
      self.num1 = self.num1[0]
      if self.num1 == "":
        self.num1 = "1"
    else:
      self.num2 = self.num1
      self.num1 = ""
      self.op2 = self.op1
      self.op1 = ""
      self.num2 = self.num2.replace("*x", "")

    self.num1 = 0 if not self.num1.isdigit() else int(self.op1 + self.num1)
    self.num2 = 0 if not self.num2.isdigit() else int(self.op2 + self.num2)
    self.num3 = 0 if not self.num3.isdigit() else int(self.op3 + self.num3)
    self.power = 0 if not self.power.isdigit() else int(self.power)

