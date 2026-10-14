#Exercice n°7 — Calcul de l’inverse d’un nombre

#Saisie du nombre reel par l'utilisateur
nombre_saisi = float(input("Saisissez un nombre reel :"))

#Vérification si le nombre saisi correspond ou differe de 0
if nombre_saisi == 0:
    print("Impossible")
else:
    print("l'inverse de ce nombre est :" , 1 / nombre_saisi)

