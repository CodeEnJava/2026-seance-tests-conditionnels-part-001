#Exercice n°8 — État de l’eau en fonction de la température

#Saisie de la temperature typée en float
temperature_saisie = float(input("Saisissez une température :"))

#Analyse de l'état physique de l'eau en fonction de la température
if temperature_saisie < 0:
    print("l'état est Solide")
elif 0 <= temperature_saisie <= 100:
    print("l'état est Liquide")
else:
    print("l'état est Gazeux")
