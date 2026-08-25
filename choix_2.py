# Code pour l'exercice n°2
"""
On souhaite indiquer si un nombre entier est :
•	Négatif
•	Positif et impair
•	Positif et pair

en utilisant if else
"""
print("Test du choix N°2 : if - else:")
# Lire un nombre entier au clavier
while True:
    try:
        nombre = int(input("Entrer un nombre entier :"))
        break
    except ValueError:
        print("Erreur ! le nombre saisi n'est pas valide")

# fin de la lecture du nombre entier

if nombre < 0:
    print("%d est un nombre négatif" %(nombre))
else:
    if nombre%2==0:
        print("%d le nombre est positif et pair" % (nombre))
    else:
        print("%d le nombre est positif et impair" % (nombre))