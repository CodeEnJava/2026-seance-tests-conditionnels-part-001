# code pour : ex06_intervalles_maciej.py

print("="*50)
print("Cas 1".center(50))
print("="*50)
print()
lire = float(input("Saisissez un nombre : "))

if -20 <= lire <= 6 or lire >= 9:
    print("Appartient")
else:
    print("N'appartient pas")
print()
print("="*50)
print("Cas 2".center(50))
print("="*50)
print()
lire = float(input("Saisissez un nombre : "))

if  lire <= 4 or lire >= 10:
    print("Appartient")
else:
    print("N'appartient pas")
print()

"""-
==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : -25
N'appartient pas

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : -50
Appartient


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : -20
Appartient

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 0
Appartient


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : 0
Appartient

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 4
Appartient


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : 6
Appartient

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 5
N'appartient pas


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : 7
N'appartient pas

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 7.5
N'appartient pas


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : 8.5
N'appartient pas

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 9.99
N'appartient pas


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : 9
Appartient

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 10
Appartient


Process finished with exit code 0

==================================================
                      Cas 1                       
==================================================

Saisissez un nombre : 15
Appartient

==================================================
                      Cas 2                       
==================================================

Saisissez un nombre : 25
Appartient


Process finished with exit code 0
























"""