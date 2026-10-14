#Exercice n°4 — La roulette du casino

MISE = 10
gain = 0
type_pari = 0
numero_sorti = 0

pari = input("Sur quel numero pariez-vous ? : ")
numero_sorti = input("Quel numero est sorti ? : ")

pari = int(pari)
numero_sorti = int(numero_sorti)


if pari > 0 and pari <= 12:
    type_pari = 1
elif pari == 13:
    type_pari = 2
elif pari == 14:
    type_pari = 3
elif pari == 15:
    type_pari = 4
elif pari == 16:
    type_pari = 5

print(type_pari)

if type_pari == 1 and numero_sorti == pari:
    gain = 12*MISE
elif type_pari == 2 and numero_sorti % 2 == 0:
    gain = MISE*2
elif type_pari == 3 and numero_sorti % 2 == 1:
    gain = MISE*2
elif type_pari == 4 and (numero_sorti == 3 or numero_sorti == 9 or numero_sorti == 12 or numero_sorti == 1
      or numero_sorti == 7 or numero_sorti == 5):
    gain = MISE*2
elif type_pari == 5 and (numero_sorti == 6 or numero_sorti == 2 or numero_sorti == 8 or numero_sorti == 11
    or numero_sorti == 10 or numero_sorti == 4):
    gain = MISE * 2
else:
    gain = 0

print(f"Votre gain est = {gain} €")

