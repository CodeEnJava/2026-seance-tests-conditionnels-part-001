# code pour : ex04_roulette_maciej.py
# test vers github



option_pari = int(input("Choisiez votre option : "))
choix_numero = int(input("Choisisque votre numéro : "))

mise = 10
gain = 0

if 0 <= option_pari <= 12:
    if option_pari == choix_numero:
        gain = mise * 12
        #cas du 0 identique à 1
        if gain == 0:
            gain = 12
    else:
        gain = 0

elif option_pari == 13:
    if choix_numero % 2 == 0:
        gain = mise * 2
    else:
        gain = 0

elif option_pari == 14:
    if choix_numero % 2 == 1:
        # alternative choix_numero % 2 != 0: cette solution est à retenir pour indiquer impair
        gain = mise * 2
    else:
        gain = 0

elif option_pari == 15:
    # alternative  on 1,3,5,7,9   et 12
    # if (choix_pari % 2 != 0 or choix_pari == 12) and choix_pari != 11
    # après avoir étudié les liste
    # if choix_pari in [1,3,5,7,9,12]
    if (choix_numero == 1 or
            choix_numero == 3 or
            choix_numero == 5 or
            choix_numero == 7 or
            choix_numero == 9 or
            choix_numero == 12
    ):
        gain = mise * 2
    else:
        gain = 0

elif option_pari == 16:
    if choix_numero == 2 or choix_numero == 4 or choix_numero == 6 or choix_numero == 8 or \
        choix_numero == 10 or choix_numero == 11:
        gain = mise * 2
    else:
        gain = 0

print(gain)

"""
Pari gagnant sur un numéro

Choisiez votre option : 7
Choisisque votre numéro : 7
120

Process finished with exit code 0

Pari perdant sur un numéro

Choisiez votre option : 7
Choisisque votre numéro : 9
0

Process finished with exit code 0

Pari gagnant sur pair

Choisiez votre option : 13
Choisisque votre numéro : 8
20

Process finished with exit code 0

Pari gangnant sur impair 

Choisiez votre option : 14
Choisisque votre numéro : 7
20

Process finished with exit code 0

Pari gangant rouge 

Choisiez votre option : 15
Choisisque votre numéro : 9
20

Process finished with exit code 0

Pari gangant sur noir

Choisiez votre option : 16
Choisisque votre numéro : 11
0

Process finished with exit code 0

Pari perdant

Choisiez votre option : 15
Choisisque votre numéro : 4
0

Process finished with exit code 0




























"""





