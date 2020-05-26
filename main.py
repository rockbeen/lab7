from numpy import array, arange, exp, sin, cos, sqrt
from scipy import integrate
import matplotlib.pyplot as plt

data = []
with open("sol.txt") as file:
    for line in file:
        data.append([float(line.split(',')[0]), float(line.split(',')[1]), float(line.split(',')[2])])

data = array(data)

x = data[:, 2]

y = exp(-x/2)*((11*7**0.5)/42 * sin(0.5*x*7**0.5) + 5/6 * cos(0.5*x*7**0.5)) + exp(-2*x)*(cos(x) - sin(x))/6
dy = exp(-x/2)*((-23*7**0.5)/42 * sin(0.5*x*7**0.5) + 1/2 * cos(0.5*x*7**0.5)) + exp(-2*x)*(-1/2*cos(x) + 1/6*sin(x))


def se_solve(Y, x):
    return [Y[1], cos(x)*exp(-2*x) - Y[1] - 2*Y[0]]

ys = integrate.odeint(se_solve, [1, 0], x)[:, 0]
dys = integrate.odeint(se_solve, [1, 0], x)[:, 1]

plt.figure(figsize=(16, 9))
plt.plot(x, data[:, 0], label="$y(x)$")
plt.plot(x, data[:, 1], label="$y'(x)$")
plt.legend(fontsize=14)
plt.minorticks_on()
plt.grid(which="both")
plt.show()

plt.figure(figsize=(16, 9))
plt.title("Фазовая траектория", fontsize=14)
plt.plot(data[:, 0], data[:, 1])
plt.xlabel("$y(x)$", fontsize=14)
plt.ylabel("$y'(x)$", fontsize=14)
plt.minorticks_on()
plt.grid(which="both")
plt.show()

plt.figure(figsize=(16, 9))
plt.title("Отклонение от точного решения", fontsize=14)
plt.plot(x, abs(y - data[:, 0]), label="$ \Delta y(x)$")
plt.plot(x, abs(dy - data[:, 1]), label="$ \Delta y'(x)$")
plt.legend(fontsize=14)
plt.minorticks_on()
plt.grid(which="both")
plt.show()

plt.figure(figsize=(16, 9))
plt.title("Отклонение от решения scipy.integrate", fontsize=14)
plt.plot(x, abs(ys - data[:, 0]), label="$ \Delta y(x)$")
plt.plot(x, abs(dys - data[:, 1]), label="$ \Delta y'(x)$")
plt.legend(fontsize=14)
plt.minorticks_on()
plt.grid(which="both")
plt.show()
