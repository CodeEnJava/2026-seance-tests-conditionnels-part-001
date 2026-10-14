#assignation des constantes

multiplicateur_gain = 12
multiplicateur_pair_impair = 2
multiplicateur_couleur = 2
mise = 10


#variable du numero gagnant
numero_gagnant = 0
gains = 0


#assignation des variables via input

pari_choisi = int(input("choisir un numéro entre 0 et 16 : "))
numero_gagnant = int(input("le numero gagnant est le : "))

#pari sur un nombre

if  0 <= pari_choisi <= 12 and pari_choisi == numero_gagnant :
    gains = mise * multiplicateur_gain
    print(f"vous avez gagné { gains } € ")
    if gains == 0 :
        gains == 12

 #Pair ou impair
elif pari_choisi== 13 and  numero_gagnant %2 == 0 :
        gains = mise * multiplicateur_pair_impair
        print(f"vous avez gagné {gains} €")
elif pari_choisi == 14 and numero_gagnant %2 != 0 :
    print(f"vous avez gagné {gains} €")


#pari sur la couleur
elif pari_choisi == 15 and numero_gagnant in [1,3,5,7,9,12] :
    gain == mise * multiplicateur_couleur
    print (f"vous avez gagné {gains} €")
elif pari_choisi == 16 and  numero_gagnant not in [1,3,5,7,9,12] :
    gains =mise * multiplicateur_couleur
    print (f"vous avez gagné {gains} €")


else:
    print(f"vous avez perdu {mise} € ")




























