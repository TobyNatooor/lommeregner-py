# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-5, 5, 100)
# y = x**2+5
# fig = plt.figure()
# plt.plot(x, y, 'r')
# plt.show()

num1, num2, num3 = "", "", ""
op1, op2, op3 = "", "", ""
isntLinear = False
test = 0

theFunction = "x^2+10*x+5"

if theFunction[0] == "x":
  theFunction = "+" + theFunction
  print(theFunction)

for i in theFunction:
  if i == "+" or i == "-":
    test += 1
    if test == 1: op1 = i
    if test == 2: op2 = i
    if test == 3: op3 = i
  else:
    if test == 1: num1 += i
    if test == 2: num2 += i
    if test == 3: num3 += i


print("num1: " + num1 + "    num2: " + num2 + "     num3: " + num3)
print("op1: " + op1 + "    op2: " + op2 + "     op3: " + op3)
