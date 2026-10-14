#Exercice n°3 — Calculatrice

#Saisie des valeurs

a = 0
b = 0
c = 0

a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxieme nombre : ")
c = input("Choisir une opération a effectuer : ")

a = int(a)
b = int(b)
c = int(c)

print("Résultat")
if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a ** 2 - 2 * (a-b))
else:
    print("Erreur !")