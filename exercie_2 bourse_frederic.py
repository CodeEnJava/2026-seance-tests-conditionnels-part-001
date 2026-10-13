#attribution des variable avec l input
nom_action = input("Nom de l'action : ")

volume_action = int(input("Volume des actions: "))

prix_achat = float(input("Prix d'achat : "))

dernier_cours = float(input("Dernies cours : "))


#calcul de la valeur des achats , de la valeur actuelle du portefeuille , des gain et des pertes

valeur_achat = volume_action * prix_achat

valeur_actuelle = volume_action * dernier_cours

gain_perte = valeur_actuelle - valeur_achat

if gain_perte > 0 :
    print (f"vos gain  sont de {gain_perte} € ")
elif gain_perte == 0 :
    print (f"vos gains sont de {gain_perte} €" )
else:
    print (f"vos perte sont de {gain_perte} €")
