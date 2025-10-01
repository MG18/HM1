import matplotlib as plt
import numpy as np
import timeit
def fact_rec(n):

    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)
    

def fact_for(n):
    x = 1
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    
    for i in range(1,n+1):
        x = x*i

    return x


t1= timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
t2= timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)
# Die Version mit dem For-Loop ist um den Faktor 10 schneller, denn beim for Loop werden nur Zahlen miteinander multipliziert, wobei bei der rekursiven variante n mal eine funktion aufegrufen wird
print(fact_rec(200))
# Integer (int): keine obere Grenze außer Speicher und Zeit → auch 200! ist kein Problem.

print(float(fact_for(171)))
#Der maximale darstellbare Wert liegt etwa bei 1.8 * 10**308 Da fakultäten asymptotisch sehr schnell wachsen, ist bei 171 die grenze erreicht und es führt zum Overflow
print(t1)
print(t2)