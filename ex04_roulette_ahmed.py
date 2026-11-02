# 1. On demande le pari du joueur et le numéro sorti
pari = int(input())
numero_sorti = int(input())

# On commence par dire que le gain est de 0 (si on perd)
gain = 0

# 2. On vérifie quel type de pari a été fait

# Cas 1 : Le joueur a parié sur un chiffre précis (de 0 à 12)
if 0 <= pari <= 12:
    if pari == numero_sorti:
        gain = 120

# Cas 2 : Le joueur a parié sur les nombres pairs (code 13)
elif pari == 13:
    if numero_sorti % 2 == 0:
        gain = 20

# Cas 3 : Le joueur a parié sur les nombres impairs (code 14)
elif pari == 14:
    if numero_sorti % 2 != 10
        gain = 20



# Cas 4 : Le joueur a parié sur le rouge (code 15) - les impairs (sauf 0)
elif pari == 15:
    if numero_sorti != 0 and numero_sorti % 2 != 0:
        gain = 20

# Cas 5 : Le joueur a parié sur le noir (code 16) - les pairs (sauf 0)
elif pari == 16:
    if numero_sorti != 0 and numero_sorti % 2 == 0:
        gain = 20

# 3. On affiche le résultat final
print(gain)