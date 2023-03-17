# Copier/coller le code ci-dessous à l'adresse suivante :
# https://demo.isograd.com/runtest/QuestionDisplayer#output

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
sys.stderr.write("-----------------------------------------------------------------------------------------------------" + "\n")

# -------------------               Nombre de pizzerias et nombre de commandes
nombre_pizzerias_et_commandes = lines[0].split()
nombre_pizzerias = int(nombre_pizzerias_et_commandes[0])
nombre_commandes = int(nombre_pizzerias_et_commandes[1])
#--------------- Debug
# sys.stderr.write("Nombre de pizzerias : " + str(nombre_pizzerias) + "\n")
# sys.stderr.write("Nombre de commandes : " + str(nombre_commandes) + "\n")
del lines[0] # Cleaning data input

# --------------------              Coordonnées des pizzerias en liste
#---------------
coordonnées_pizzerias = []
for i in range(int(nombre_pizzerias)):
    coordonnées_pizzerias.append(lines[0])
    del lines[0] # Cleaning data input
#--------------- Debug
# for pizzeria in coordonnées_pizzerias :
#     sys.stderr.write("Coordonnées pizzeria : " + str(pizzeria) + "\n")

# --------------------               Coordonnées des commandes en liste
#---------------
coordonnées_commandes = []
for i in range(int(nombre_commandes)):
    coordonnées_commandes.append(lines[i])
#--------------- Debug
# for commande in coordonnées_commandes :
#     sys.stderr.write("Coordonnées commande : " + str(commande) + "\n")
    
    
# --------------------               Programme - Réponse
distances_addition = 0
distance_manhattan = 0

# Pour chaque lieu de commande, on calcule la distance de chacun avec chaque pizzeria et on additionne les plus petite distance (x2 pour allez-retour)
for coord_commande in coordonnées_commandes :
    x1,y1 = coord_commande.split()
    distance_référence = 1000000  # Ce nombre est ainsi choisi dans la mesure où la distance maximale entre une pizzeria et un lieu de commande est de 1.000.000
    for coord_pizzeria in coordonnées_pizzerias :
        x2, y2 = coord_pizzeria.split()
        distance_manhattan = abs(int(x1)-int(x2)) + abs(int(y1)-int(y2))
        if distance_manhattan > distance_référence or distance_manhattan == distance_référence :
            continue
        else :
            distance_référence = distance_manhattan
    distances_addition += distance_référence*2
            
print(distances_addition)