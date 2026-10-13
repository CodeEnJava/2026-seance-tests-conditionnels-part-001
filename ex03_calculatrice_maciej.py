# code pour : ex03_calculatrice_maciej.py


lettre_a =int(input("Entrez a : "))
lettre_b =int(input("Entrez b : "))
lettre_c =int(input("Entrez votre choix : "))

if lettre_c == 1:
    resultat = lettre_a + lettre_b
    print("Résultat : ",resultat)

elif lettre_c == 2:
    resultat = lettre_a - lettre_b
    print("Résultat : ",resultat)

elif lettre_c == 3:
    resultat = lettre_a * lettre_b
    print("Résultat : ",resultat)

elif lettre_c == 4:
    resultat = lettre_a ** 2 - 2 * (lettre_a - lettre_b)
    print("Résultat : ",resultat)

else:
    print("Erreur : ")

"""
Entrez a : 10
Entrez b : 5
Entrez votre choix : 1
Résultat :  15

Process finished with exit code 0

Entrez a : 10
Entrez b : 5
Entrez votre choix : 2
Résultat :  5

Process finished with exit code 0

Entrez a : 10
Entrez b : 5
Entrez votre choix : 3
Résultat :  50

Process finished with exit code 0

Entrez a : 10
Entrez b : 5
Entrez votre choix : 4
Résultat :  90

Process finished with exit code 0


Entrez a : 10
Entrez b : 5
Entrez votre choix : 7
Erreur : 

Process finished with exit code 0














"""


