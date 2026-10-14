#Exercice n°2 — Calculer les gains et les pertes en bourse


#Saisie

nom_action = input("Nom de l'action : ")
volume_action = input("Nombre d'actions détenues : ")
prix_action = input("Prix d'achat d'une action : ")
dernier_cours = input("Valeur actuelle de l'action : ")

#Calculs

valeur_achat = int(volume_action) * float(prix_action)
valeur_actuelle = int(volume_action) * float(dernier_cours)

gain_perte = float(valeur_actuelle) - float(valeur_achat)

if (gain_perte > 0):
    print(f"Votre gain est de {gain_perte:.2f} €")
elif (gain_perte < 0):
    print(f"Votre perte est de {abs(gain_perte):.2f} €")
else:
    print("Il n y a eut ni gain ni pertes")

