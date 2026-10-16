                                                #Exercice n°5 — Mentions

#Saisie de la moyenne

m = float(input("Entrez votre moyenne : "))

# ============================
# Solution 1
# ============================

#Si la moyenne est inférieure a 8
if m < 8:
    print("Refusé")
#Si la moyenne est comprise entre 8 et 10 exclu
elif m >= 8 and m < 10:
    print("Admis au second groupe")
#Si la moyenne est comprise entre 10 et 12 exclu
elif m >= 10 and m < 12:
    print("Admis")
#Si la moyenne est comprise entre 12 et 14 exclu
elif m >= 12 and m < 14:
    print("Admis avec mention assez bien")
#Si la moyenne est comprise entre 14 et 16 exclu
elif m >= 14 and m < 16:
    print("Admis avec mention bien")
#Si la moyenne est strictement supérieure a 16
elif m >= 16:
    print("Admis avec mention très bien")

# ============================
# Solution 2
# ============================

#Structure conditionnelles imbriquées
if m >= 8:
    if m >= 10:
        if m >= 12:
            if m >= 14:
                if m >= 16:
                    print("Admmis avec mention très bien")
                else:
                    print("Admmis avec mention bien")
            else:
                print("Admis avec mention assez bien ")
        else:
            print("Admis")
    else:
        print("Admis au second groupe")
else:
    print("Refusé")
# ============================
# Solution 3
# ============================

#Vérification de la moyenne en partant de la condition la plus haute
if m >= 16:
    print("Admis avec mention très bien")
elif m >= 14:
    print("Admis avec mention bien")
elif m >= 12:
    print("Admis avec mention assez bien")
elif m >= 10:
    print("Admis")
elif m >= 8:
    print("Admis au second groupe")
else:
    print("Refusé")
