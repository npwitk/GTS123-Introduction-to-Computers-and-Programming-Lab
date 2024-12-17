import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.arange(-3*m.pi, 3*m.pi, 0.1)

y1 = np.sin(x)
y2 = np.sin(x+0.5)
y3 = np.sin(x+1)
y4 = np.sin(x+1.5)

plt.plot(x, y1, color="blue", linewidth=2, linestyle= "dotted")
plt.plot(x, y2, color="green", linewidth=2, linestyle= "dashed")
plt.plot(x, y3, color="orange", linewidth=2, linestyle= "dashdot")
plt.plot(x, y4, color="pink", linewidth=2, linestyle= "solid")
plt.xlim(-10, 10)
plt.show()