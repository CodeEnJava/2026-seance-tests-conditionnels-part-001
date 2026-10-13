# code pour : ex02_bourse_maciej.py

nom_action = input("Nom de l'action : ")
volume_action = int(input("Volume des actions: "))
prix_achat = float(input("Prix d'achat : "))
dernier_cours = float(input("Dernies cours : "))

valeur_achat = volume_action * prix_achat
valeur_actuelle = volume_action * dernier_cours
gain_perte = valeur_actuelle - valeur_achat

print("Action          :", nom_action)
print("Valeur d'achat  :", valeur_achat, "€")
print("Valeur actuelle :", valeur_actuelle, "€")

if gain_perte > 0:
    print("Gain :", gain_perte, "€")

elif gain_perte < 0:
    print("Perte :", abs(gain_perte), "€")

else:
    print("Ni gain ni perte.")


"""
Nom de l'action : XYZ
Volume des actions: 10
Prix d'achat : 50
Dernies cours : 65
Action          : XYZ
Valeur d'achat  : 500.0 €
Valeur actuelle : 650.0 €
Gain : 150.0 €

Nom de l'action : ABC
Volume des actions: 20
Prix d'achat : 80
Dernies cours : 65
Action          : ABC
Valeur d'achat  : 1600.0 €
Valeur actuelle : 1300.0 €
Perte : 300.0 €







"""