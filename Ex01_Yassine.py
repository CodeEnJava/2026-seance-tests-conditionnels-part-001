#Exercice n°1 — Déterminer si une saisie est un chiffre
from idlelib.sidebar import EndLineDelegator

#Saisie de l'utilisateur

chiffre = input("Entrez un chiffre : ")

#Vérification
verification_chiffre = False

if chiffre > "9":
    verification_chiffre = False
elif chiffre <= "9":
    verification_chiffre = True

print(verification_chiffre)