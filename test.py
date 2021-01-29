import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x**2+5
fig = plt.figure()
plt.plot(x, y, 'r')
plt.show()
