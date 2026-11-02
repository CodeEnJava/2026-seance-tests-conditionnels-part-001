# 1. Demander les informations à l'utilisateur

nom_action = input("Nom de l'action : ")
volume = int(input("Nombre d'actions détenues : "))
prix_achat = float(input("Prix d'achat d'une action : "))
dernier_cours = float(input("Prix actuel d'une action : "))

# 2. Faire les calculs
valeur_achat = volume * prix_achat
valeur_actuelle = volume * dernier_cours
gain_perte = valeur_actuelle - valeur_achat

# 3. Afficher les résultats de base
print("--- Bilan ---")
print("Action :", nom_action)
print("Valeur d'achat totale :", valeur_achat)
print("Valeur actuelle totale :", valeur_actuelle)

# 4. Vérifier s'il y a un gain ou une perte
if gain_perte > 0:
    print("C'est un gain de :", gain_perte, "€")
else:
    # On utilise abs() pour afficher la perte en nombre positif
    print("C'est une perte de :", abs(gain_perte), "€")