import numpy as np

def Name_S01_Aufg2(a, xmin, xmax):

    xintervall = (xmax - xmin) * 100

    # Input prüfen
    a = np.asarray(a).squeeze()
    if a.ndim != 1 or a.size == 0:
        raise Exception("Fehler: a muss ein nicht-leerer 1D-Vektor sein.")
    if xmin >= xmax:
        raise Exception("Fehler: xmin < xmax erforderlich.")
    
    # x-Werte
    x = np.linspace(xmin, xmax, xintervall)

    # Funktionswerte p(x)
    p = sum(a[i] * x**i for i in range(a.size))

    # Ableitung: [1*a1, 2*a2, ..., n*an]
    dp_coeffs = np.arange(1, a.size) * a[1:]
    dp = sum(dp_coeffs[i] * x**i for i in range(dp_coeffs.size))

    # Stammfunktion: [0, a0/1, a1/2, ..., an/(n+1)]
    pint_coeffs = np.zeros(a.size+1)
    pint_coeffs[1:] = a / np.arange(1, a.size+1)
    pint = sum(pint_coeffs[i] * x**i for i in range(pint_coeffs.size))

    return x, p, dp, pint
