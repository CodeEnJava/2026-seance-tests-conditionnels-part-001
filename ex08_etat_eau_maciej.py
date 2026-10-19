#Ex08



temp_eau= float(input("température  de l eau  :"))

if temp_eau < 0:
    print("Solide")
elif 0 <= temp_eau <= 100:
    print("Liquide")
else:
    print("Gazeuse")

"""
température  de l eau  :-1
Solide

Process finished with exit code 0

température  de l eau  :0
Liquide

Process finished with exit code 0

température  de l eau  :1
Liquide

Process finished with exit code 0

température  de l eau  :50
Liquide

Process finished with exit code 0

température  de l eau  :99
Liquide

Process finished with exit code 0

température  de l eau  :100
Liquide

Process finished with exit code 0

température  de l eau  :101
Gazeuse

Process finished with exit code 0

température  de l eau  :-0.1
Solide

Process finished with exit code 0

température  de l eau  :0.5
Liquide

Process finished with exit code 0

température  de l eau  :37.5
Liquide

Process finished with exit code 0

température  de l eau  :99.9
Liquide

Process finished with exit code 0

température  de l eau  :100.1
Gazeuse

Process finished with exit code 0









"""