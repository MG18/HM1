import math

# 1) eps: größte kleine Zahl mit 1 + eps == 1  (unit roundoff)
eps = 1.0
while True:
    eps_half = eps / 2.0
    if 1.0 + eps_half == 1.0:   # halbiert -> Addition wirkt nicht mehr
        eps = eps_half          # dies ist die größte kleine Zahl mit 1+eps==1
        break
    eps = eps_half

# Alternative: minimale kleine Zahl, die 1 verändert (nur zur Info)
eps_change = 1.0
while 1.0 + eps_change > 1.0:
    eps_change /= 2.0
eps_change *= 2.0  # kleinste Zahl mit 1+eps_change > 1  (entspricht 2*eps)

# 2) qmin: kleinste große Zahl mit 1 + qmin == qmin
qmin = 1.0
while 1.0 + qmin > qmin:
    qmin *= 2.0

# Auswertung / "Stellenzahl"
mantissa_bits = round(-math.log2(eps))         # erwartet 53 bei IEEE-Double
decimal_digits = math.floor(-math.log10(eps))  # ~16 Dezimalstellen

print("Maschinengenauigkeit (unit roundoff):")
print(f"  eps        = {eps:.20e}")
print(f"  -log2(eps) = {mantissa_bits}  (Mantissen-Bits, inkl. führender 1)")
print(f"  ~10^(-{decimal_digits}) Dezimalstellen\n")

print("Kleinste große Zahl mit 1 + qmin == qmin:")
print(f"  qmin       = {qmin:.1f}")
print(f"  qmin * eps = {qmin*eps:.1f}  (sollte ≈ 1 sein)\n")

