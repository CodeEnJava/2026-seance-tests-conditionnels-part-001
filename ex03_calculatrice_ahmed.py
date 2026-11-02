# Demande des valeurs a,b et c
a = int(input("entrez a : "))
b = int(input("entrez b : "))
c = int(input("entrez votre choix : "))
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(f"Resultat : {a ** 2-2* (a - b)}")
else: print("erreur")

