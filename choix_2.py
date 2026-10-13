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

# traitement #
# SI le nombre est inférieure à 0 alors c'est nombre négatif

# je teste le nombre , pour savoir s'il est négatif
if nombre < 0:# tester le nombre  est-ce que le nombre est négatif ?
    #ALORS
    print("%d est un nombre négatif" %(nombre))
else:
    #SINON
    # ne nombre n'est pas négatif
    if nombre%2==0: # est-ce ce nombre est pair ?
        print("%d le nombre est positif et pair" % (nombre))
    else:
        print("%d le nombre est positif et impair" % (nombre))
