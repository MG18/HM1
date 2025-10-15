import numpy as np
import matplotlib.pyplot as plt


#Aufgabe 4
#Auslöschung = Subtraktion fast gleicher großer Zahlen → Verlust signifikanter Stellen.
# Folge: Die Funktion ist ist numerisch heikel in der Umgebung von 1.1

# Definition von t(x)
def t(x):
    return 100*x**2 - 200*x + 99

# x-Werte rund um 1.1
xs = np.linspace(1.095, 1.105, 400)
ys = t(xs)

# Plot
plt.figure(figsize=(6,4))
plt.plot(xs, ys, label="t(x) = 100x² - 200x + 99")
plt.axhline(0, color="black", linestyle="--")
plt.axvline(1.1, color="red", linestyle=":", label="x = 1.1")
plt.title("t(x) ist nahe x=1.1 sehr klein → anfällig für Auslöschung")
plt.xlabel("x")
plt.ylabel("t(x)")
plt.legend()
plt.grid(True)
plt.show()



# Kondition definieren
def K(x):
    return np.abs(100*x*(x-1) / (100*x**2 - 200*x + 99))

# Wertebereich mit Delta x = 1e-7
xs = np.arange(1.1, 1.3+1e-7, 1e-7)
Ks = K(xs)

# Plot: halblogarithmisch (y-Achse log)
plt.figure(figsize=(7,4))
plt.semilogy(xs, Ks, label="Kondition von h(x)")
plt.xlabel("x")
plt.ylabel("K(x) (log-Skala)")
plt.title("Halblogarithmischer Plot der Kondition von h(x)")
plt.grid(True, which="both")
plt.legend()
plt.show()


# Hinweis:
# Die Auslöschung bei h(x) nahe x=1.1 kann nicht durch algebraische Umformung vermieden werden.
# Grund: Die Kondition K(x) geht dort gegen ∞, d.h. das Problem ist schlecht konditioniert.
# Kleine Eingabefehler in x führen unvermeidlich zu großen relativen Fehlern im Resultat.
