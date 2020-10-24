import numpy as np
import matplotlib.pyplot as plt
import random

n = int(input("Enter the number of steps you wish to generate"))
x = np.zeros(n)
y = np.zeros(n)

for i in range(1,n):
    val = random.choice(['N', 'S', 'E', 'W'])
    if val == 'E':
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 'W':
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 'N':
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
plt.plot(x,y)
plt.title("Random walk for " + str(n) + " particles")
plt.grid()
plt.show()

