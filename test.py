import matplotlib.pyplot as plt
import numpy as np
from splitStringFunction import SplitStringFunction

fcn = SplitStringFunction("3x^2+15*x")

x = np.linspace(-20, 20, 100)
y = fcn.num1*x**fcn.power + fcn.num2*x + fcn.num3
plt.plot(x, y, 'r')
plt.show()


