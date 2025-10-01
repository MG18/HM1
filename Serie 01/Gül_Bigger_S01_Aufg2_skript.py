import matplotlib.pyplot as plt

from Gül_Bigger_S01_Aufg2 import Name_S01_Aufg2

# Polynom aus Aufgabe 1
a = [-0, 1, 2]  # a0 ... an
x, p, dp, pint = Name_S01_Aufg2(a, -10, 10)

fig, ax = plt.subplots(figsize=(7,4))
ax.plot(x, p,    label="f(x)")
ax.plot(x, dp,   label="f'(x)")
ax.plot(x, pint, label="F(x) mit C=0")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Aufgabe 2: allgemeines Polynom")
ax.grid(True)
ax.legend()

ax.set_xlim(-6, 8)
ax.set_ylim(-20, 20)

plt.show()
