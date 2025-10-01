import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10)
var = np.poly1d([1,-5,-30,110,29,-105])
der = var.deriv()
stem = var.integ()


y1 = var(x)
y2 = der(x)
y3 = stem(x)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, y1, label="f(x)")
ax.plot(x, y2, label="f'(x)")
ax.plot(x, y3, label="F(x)")
ax.legend()
plt.ylim(-1500,1500)
plt.grid(True)
plt.title("Aufgabe 1")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

plt.show()
