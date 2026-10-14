#Exercice n°6 — Les intervalles

valeur_saisie = float(input("Veuillez saisir un nombre :"))

#CAS 1
print("Cas n°1 :")
#Vérification d'appartenance l'ensemble : [-20 ; 6] U [9 ; +∞[
if -20 <= valeur_saisie <= 6 or 9 <= valeur_saisie:
    print("Appartient !")
else:
    print("N'apprartient pas")
print("Cas n°2 :")
#CAS 2
#Vérification d'appartenance l'ensemble : ]-∞ ; 4] U [10 ; +∞[
if valeur_saisie <= 4 or 10 <= valeur_saisie:
    print("Appartient !")
else:
    print("N'appartient pas")
