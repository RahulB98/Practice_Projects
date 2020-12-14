import math
import matplotlib.pyplot as plt 

def Y(x):
    return 0.5*(math.exp(x) - math.exp(-x))

for x in range(0,2):
    plt.plot(x, Y(x),"-")
plt.show()
'''import matplotlib.pyplot as plt
def func(x,y):
    return(x-y)

def RK2(x0, y0, x ,h):
    n = round( (x - x0) / h)
    print(n)
    y = y0

    plot_x= []
    plot_y = []

    for i in range(1, n+1):
        k1 = h * func(x0, y);  
        k2 = h * func(x0 + 0.5 * h, y + 0.5 * k1)
        y = y + (1/6) * (k1 + 2 * k2)
        plot_x.append(x0)
        plot_y.append(y)
        x0 = x0 + h
        

    return y, plot_x, plot_y

y0 = 2
x0 = 1
for h in [0.1,0.05,0.025]:
    Y_dash, X, Y = RK2(x0, y0, 1.4, h)
    print("for h = " +str(h)+" dy/dyx using RK2 method is: " + str(Y_dash))
    plt.plot(X,Y, "-o", label = "h = " + str(h))
    plt.legend()
plt.xlabel("Vlaues of X")
plt.ylabel("Calcuklated values of dy/dx")
plt.title("Runge-Kutta 2 Method")
plt.grid()
plt.show()'''