
# cas n° 1
nb_choisi = int (input("entrer une chiffre ou un nombre :"))


if nb_choisi in range (-20 , 7 ) or nb_choisi >= 10 :
    print ( "ce nombre appartient a l ensemble")
else:
    print("n appartient pas a ce groupe ")

#Cas n° 2

nb_choisi_2 = int(input("entrer un nombre ou un chiffre :"))

if nb_choisi_2 < 4 or nb_choisi_2 >= 10 :
    print("Ce nombre appartient a cet ensemble")
else :
    print("ce nombre n appartient pas a cet ensemble")