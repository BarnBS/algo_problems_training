# Copy/Paste the code below at :
# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=33&reg_typ_id=2&que_str_id=&cli_id=45alrk6jpdnaguf3oa3gto2875&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D57

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# Nombre d'articles
nombreArticles = int(lines[0])
sys.stderr.write("Nombre d'articles : " + str(nombreArticles) + "\n")
del lines[0]

# Articles splités
produitsSplités = []
for i in range(nombreArticles):
    produitsSplités.append(lines[i].split())
sys.stderr.write("\n PRODUITS SPLITES : \n" + str(produitsSplités) + "\n")

# Liste de chaque article et prix de l'article invendu
produitsRestantListe = []
produitsListeSplitée = []
for i in range(nombreArticles) :
    if lines[i] in produitsRestantListe:
        continue
    else :
        produitsRestantListe.append(lines[i])
        produitsListeSplitée.append(lines[i].split())
sys.stderr.write("\n LISTE DES PRODUITS ET PRIX: \n" + str(produitsListeSplitée) + "\n")

# Dictionnaire des articles et nombre de fois qu'il est répété dans l'input
articlesRestantsDictionnaire = {}
for produitsSplités[0] in produitsSplités :
    article = produitsSplités[0][0]
    if str(article) in articlesRestantsDictionnaire:
        articlesRestantsDictionnaire[str(article)] += 1
    else:
        articlesRestantsDictionnaire[str(article)] = 1
sys.stderr.write("\n PRODUITS REPETES NOMBRE DE FOIS : \n" + str(articlesRestantsDictionnaire) + "\n")


# Cout pour chaque type de produit restant en fonction du nombre de produit qu'il reste
coutDictionnaire = {}
for article in articlesRestantsDictionnaire :
    for produit in produitsListeSplitée :
        if article == produit[0] :
            coutDictionnaire[str(article)] = articlesRestantsDictionnaire[article] *int(produit[1])
sys.stderr.write("\n COUT PRODUITS : \n" + str(coutDictionnaire) + "\n" + "\n" + "------------------------" + "\n")


# Réponse finale : le type de produit qui coute le plus cher à Papi
réponse = []
coutRéférent = 0
for article in coutDictionnaire :
    if coutRéférent == 0 :
        coutRéférent = coutDictionnaire[article]
        réponse.append(article)
    elif coutDictionnaire[article] == coutRéférent :
        réponse.append(article)
    elif coutDictionnaire[article] > coutRéférent :
        coutRéférent = coutDictionnaire[article]
        réponse.append(article)
        del réponse[0:réponse.index(article)]
        
sys.stderr.write("\n REPONSE : \n" + str(article) + "\n" + "\n" + "------------------------" + "\n")
print(' '.join(réponse))
