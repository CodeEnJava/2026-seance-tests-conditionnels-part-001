"""
SEANCE S-PYTHON-1010
Exercice n°1 — Déterminer si une saisie est un chiffre
🎯 Objectif
Écrire un programme Python permettant de déterminer si le caractère saisi par l’utilisateur correspond à un chiffre (0 à 9), sans utiliser de fonction ou de mécanisme permettant directement de déterminer le type de la donnée, comme type() ou isinstance().
📋 Consignes
Le programme doit :
1.	Demander à l’utilisateur de saisir un seul caractère à l’aide de la fonction input().
2.	Vérifier si le caractère saisi est un chiffre.
3.	Afficher :
o	True si le caractère est un chiffre ;
o	False dans le cas contraire.
4.	Ajouter des commentaires explicatifs dans le code afin de présenter la démarche utilisée.
5.	Ajouter des preuves de bon fonctionnement, par exemple sous forme de captures d’écran montrant plusieurs tests.
Important : pour cet exercice, on considère que l’utilisateur saisit exactement un caractère.
🧪 Exemples de fonctionnement
Exemple 1 :
Saisir un caractère : a
False
Exemple 2 :
Saisir un caractère : 2
True


la table ascii

48	060	30	00110000	0	&#48;	 	Chiffre zéro
49	061	31	00110001	1	&#49;	 	Chiffre un
50	062	32	00110010	2	&#50;	 	Chiffre deux
51	063	33	00110011	3	&#51;	 	Chiffre trois
52	064	34	00110100	4	&#52;	 	Chiffre quatre
53	065	35	00110101	5	&#53;	 	Chiffre cinq
54	066	36	00110110	6	&#54;	 	Chiffre six
55	067	37	00110111	7	&#55;	 	Chiffre sept
56	070	38	00111000	8	&#56;	 	Chiffre huit
57	071	39	00111001	9	&#57;	 	Chiffre neuf
"""

# Un chiffre est un symbole utilisé pour représenter un nombre
# dans la table ASCII les symboles se suivent

# la lecture est un chiffre s'il appartient à l'intervalle ["0","9"]
# soit ["0","9"] --> "0" <= lecture <= "9"
# soit lecture <= "9" ET lecture >= "0"

# soit le chiffre appartient à la plage des codes ASCII [48,57] exprimé en décimal.

# première solution

str_chiffre = input("Saisir un caractère : ")

# on va traiter uniquement le premier caractère saisi
str_chiffre = str_chiffre[0]

if str_chiffre >="0" and str_chiffre <= "9":
    print("version 1 ",True)
else:
    print("version 1 ",False)

# version souhaité par python
if "0" <= str_chiffre <= "9":
    print("version 2 ",True)
else:
    print("version 2 ",False)


# soit le chiffre appartient à la plage des codes ASCII [48,57] exprimé en décimal.
# appartient        --> in
# n'appartient pas  --> not in

# une plage         --> range
# range(48,57)    ou range(0,9)
# la lecture va retourner une chaine de caractères
# ON PREND UNIQUEMENT LE PREMIER CARACTERE

# il faut convertir le caractère en code ASCII  on dispose d'une fonction ord()

OFFSET = 48 # la valeur du code ASCII de '0'
chiffre = ord(str_chiffre) -  OFFSET

if chiffre  in range(0,9):
    print("version 3 ", True)
else:
    print("version 3 ", False)

if chiffre not in range(0,9):
    print("version 3 ", False)
else:
    print("version 3 ", True)
