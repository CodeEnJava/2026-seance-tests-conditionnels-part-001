#assignation des variable via input

valeur_a = int(input ("entrer un premier nombre entier :"))
valeur_b = int(input ("entrer un second nombre entier :"))
valeur_c = int(input ("entrer un troisiemme entier :"))

# condition des pour les calcul a effecteuer

if valeur_c == 1 :
    resulat =  valeur_a + valeur_b
    print(f"la resulat de l operation est {resulat}")
elif valeur_c == 2:
    resulat= valeur_a - valeur_b
    print(f"la resulat de l operation est {resulat}")
elif valeur_c == 3 :
    resulat = valeur_a * valeur_b
    print(f"la resulat de l operation est {resulat}")
elif valeur_c == 4 :
    resulat = valeur_a ** 2-2* (valeur_a - valeur_b)
    print(f"la resulat de l operation est {resulat}")






