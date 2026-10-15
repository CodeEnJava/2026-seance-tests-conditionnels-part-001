#tp n°8

#relevé de la temperature de l 'eau
temp_eau= float(input("température  de l eau  :"))

#etat de l'eau selon la temperature
if temp_eau < 0:
    print("l'eau est Solide")
elif 0 <= temp_eau <= 100:
    print("l'eau est Liquide")
else:
    print("l'eau est Gazeuse")

