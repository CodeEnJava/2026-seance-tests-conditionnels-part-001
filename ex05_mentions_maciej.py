# code pour : ex05_mentions_maciej.py
#A
print("="*50)
print("Solution 1")
print("="*50)
print()
moyenne = float(input(" Saisissez vote moyenne : "))

if moyenne < 8:
    print("Refusé")
elif 8 <= moyenne < 10:
    print("Admis au second groupe")
elif 10 <= moyenne < 12:
    print("Admis")
elif 12 <= moyenne < 14:
    print("Admis mention assez bien")
elif 14 <= moyenne < 16:
    print("Admis mention bien")
elif moyenne >= 16:
    print("Admis mention très bien")
print()
print("="*50)
print("Solution 2")
print("="*50)
print()
moyenne = float(input(" Saisissez vote moyenne : "))

if moyenne < 8:
    print("Refusé")
else:
    if moyenne < 10:
        print("Admis au second groupe")
    else:
        if moyenne < 12:
            print("Admis")
        else:
            if moyenne < 14:
                print("Admis mention assez bien")
            else:
                if moyenne < 16:
                    print("Admis mention bien")
                else:
                    if moyenne >= 16:
                        print("Admis avec mention très bien")
print()
print("="*50)
print("Solution 3")
print("="*50)
print()
moyenne = float(input(" Saisissez vote moyenne : "))

if moyenne < 8:
    print("Refusé")
elif moyenne < 10:
    print("Admis au second groupe")
elif moyenne < 12:
    print("Admis")
elif moyenne < 14:
    print("Admis mention assez bien")
elif moyenne < 16:
    print("Admis mention bien")
elif moyenne >= 16:
    print(" Admis avec mention très bien")
print()

# VERIFICATION SOL : 1, 2 et 3 :
"""
==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 7.99
Refusé

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 7.99
Refusé

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 7.99
Refusé


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 8
Admis au second groupe

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 8
Admis au second groupe

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 8
Admis au second groupe


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 9.99
Admis au second groupe

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 9.99
Admis au second groupe

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 9.99
Admis au second groupe


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 10
Admis

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 10
Admis

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 10
Admis


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 11.99
Admis

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 11.99
Admis

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 11.99
Admis


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 12
Admis mention assez bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 12
Admis mention assez bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 12
Admis mention assez bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 13.99
Admis mention assez bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 13.99
Admis mention assez bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 13.99
Admis mention assez bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 14
Admis mention bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 14
Admis mention bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 14
Admis mention bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 15.99
Admis mention bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 15.99
Admis mention bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 15.99
Admis mention bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 16
Admis mention très bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 16
Admis avec mention très bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 16
 Admis avec mention très bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 5
Refusé

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 5
Refusé

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 5
Refusé


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 8.5
Admis au second groupe

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 8.5
Admis au second groupe

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 8.5
Admis au second groupe


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 10.5
Admis

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 10.5
Admis

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 10.5
Admis


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 12.5
Admis mention assez bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 12.5
Admis mention assez bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 12.5
Admis mention assez bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 14.5
Admis mention bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 14.5
Admis mention bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 14.5
Admis mention bien


Process finished with exit code 0

==================================================
Solution 1
==================================================

 Saisissez vote moyenne : 18
Admis mention très bien

==================================================
Solution 2
==================================================

 Saisissez vote moyenne : 18
Admis avec mention très bien

==================================================
Solution 3
==================================================

 Saisissez vote moyenne : 18
 Admis avec mention très bien


Process finished with exit code 0





























"""

