import numpy as np
import matplotlib.pyplot as plt

# Startwerte
n = 6
s_naiv = 1.0
s_stab = 1.0

N = [n]
U_naiv = [n * s_naiv]
U_stab = [n * s_stab]

# Anzahl Verdopplungen
for _ in range(40):
    # naiv: s_{2n} = sqrt(2 - 2*sqrt(1 - s_n^2/4))
    c = np.sqrt(1.0 - (s_naiv*s_naiv)/4.0)
    s_naiv = np.sqrt(2.0 - 2.0*c)

    # stabil: s_{2n} = s_n / sqrt(2*(1 + sqrt(1 - s_n^2/4)))
    c = np.sqrt(1.0 - (s_stab*s_stab)/4.0)
    s_stab = s_stab / np.sqrt(2.0*(1.0 + c))

    n *= 2
    N.append(n)
    U_naiv.append(n * s_naiv)
    U_stab.append(n * s_stab)

# Plot
plt.plot(N, U_naiv, label="naiv")
plt.plot(N, U_stab, "--", label="stabil")
plt.axhline(2*np.pi, linewidth=1, label="2π (Referenz)")
plt.xscale("log")
plt.xlabel("Anzahl Ecken n (log)")
plt.ylabel("Umfang U_n = n · s_n")
plt.title("Archimedes: Naive vs. stabile Rekursion")
plt.grid(True)
plt.legend()
plt.show()

