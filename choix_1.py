# Code pour l'exercice N°1
"""
On souhaite indiquer si un nombre entier est :
•	Négatif
•	Positif et impair
•	Positif et pair

"""

# Lire un nombre entier au clavier
while True:
    try:
        nombre = int(input("Entrer un nombre entier :"))
        break
    except ValueError:
        print("Erreur ! le nombre saisi n'est pas valide")

# fin de la lecture du nombre entier

# Négatif
if nombre < 0:
    print("%d est un nombre négatif" %(nombre))

# Positif et impair
if nombre >= 0 and nombre % 2 !=0:
    print("%d est un nombre positif impair" %(nombre))

# Positif et pair
if nombre >=0 and nombre % 2 == 0:
    print("%d est un nombre positif pair" %(nombre))
