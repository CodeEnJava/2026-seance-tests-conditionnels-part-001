
# Vérifier si le caractère saisi est un chiffre.
caractère = input("Saisir un caractère : ")

resultat = caractère >= '0' and caractère <= '9'
print(resultat)

# Saisir un caractère : a False
# Saisir un caractère : 2 True

# Objectif : Déterminer si un caractère saisi par l'utilisateur est un chiffre (0 à
# On récupère la saisie de l'utilisateur avec input().
# Les caractères '0' à '9' se suivent dans l'ordre. On vérifie donc si le
#    caractère est supérieur ou égal à '0' ET inférieur ou égal à '9'.
# Le résultat de cette comparaison est directement un booléen (True ou False).
