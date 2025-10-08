import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.99, 2.01, 501)

fig, ax = plt.subplots(figsize=(5,2.7), layout='constrained')

ax.plot(x, x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128, label="f1(x)")
ax.plot(x, (x-2)**7, label="f2(x)")
ax.legend()
#plt.ylim(-100,100)
plt.grid(True)

plt.show()


#Obwohl f1 und f2 analytisch identisch sind, führt die ausmultiplizierte Form f1 in Double-Precision nahe x=2 zu katastrophaler Auslöschung (große, fast gleiche Terme heben sich auf).
# Dadurch werden Rundungsfehler stark verstärkt. Die faktorisierte Form f2=(x−2)**7 bleibt numerisch stabil, weil sie direkt mit der kleinen Größe (x−2) arbeitet.


# mit schrittweite 10**(-17) hat man 2001 punkte zwischen dem intervall, man muss ganzzahl als parameter mitgeben
x2 = np.linspace(-10**(-14), 10**(-14), 2001)

fig2, ax2 = plt.subplots(figsize=(5,2.7), layout='constrained')

ax2.plot(x2, x2/(np.sin(1+x2) - np.sin(1)), label="g(x)")
ax2.plot(x2, x2/(2*np.cos((2+x2)/2)*np.sin(x2/2)), label="g2(x)")
#ax.plot(x, (x-2)**7, label="f2(x)")
ax2.legend()
#plt.ylim(-100,100)
plt.grid(True)

plt.show()

#Nein es ist nicht stabil mit der variante von aufgabe b)
#Ja es wird stabil mit der variante von auf a)
