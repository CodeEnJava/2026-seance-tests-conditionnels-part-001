# code pour exercice N°3
# code pour exercice N°3
"""
On souhaite indiquer si un nombre entier est :
•	Négatif
•	Positif et impair
•	Positif et pair

en utilisant if else
"""
print("Test du choix N°3 : if - elif:")
# Lire un nombre entier au clavier
while True:
    try:
        nombre = int(input("Entrer un nombre entier :"))
        break
    except ValueError:
        print("Erreur ! le nombre saisi n'est pas valide")

# fin de la lecture du nombre entier

# traitement #
if nombre < 0:
    print("%d est un nombre négatif" %(nombre))
elif nombre % 2 ==0:
    print("%d est un nombre positif et pair")
else:
    print("%d est un nombre positif et impair" %(nombre))
