"""
Ce programme parcourt le dossier data/raw/ avec les contenus aspirés et cherche les informations suivantes
pour chaque document :
- le titre
- le contenu textuel
- génère un id pour chaque document.

Ces informations sont sauvegardées dans un fichier csv de sortie appelé sortie.csv (dans data/clean/).
Afin de coller le plus possible au corpus de référence SQuAD, nous avons ajouté les colonnes "question" et "answer".
Ces deux dernières colonnes sont actuellement vides en attendant d'obtenir les informations qui les rempliront.
"""

import csv
import os

# on récupère toute la liste de nos fichiers :
liste_fichiers = os.listdir('../../data/raw/')
# pour vérifier le contenu de la liste de fichiers :
#print(liste_fichiers)

# liste qui contiendra le contenu de chaque fichier :
liste_textes = []

# liste qui contiendra les informations de chaque ligne du tableau de données :
tableau = []

# on va attribuer un ID à chaque lignes de notre corpus sous forme csv :
id = 0

# on parcourt chaque fichier un par un :
for fichier in liste_fichiers:
    # on ajoute un à l'ID :
    id += 1
    # pour chaque document on part d'un dictionnaire avec toutes les informations :
    ligne = {}
    # on ouvre chaque document aspiré pour en récupérer ses informations :
    with open(f"../../data/raw/{fichier}", "r") as fichier_txt:
        #liste_textes.append(fichier_txt.read().replace("\xa0", "")) # on pense à retirer les espacements automatiques à chaque caractère spécial noté \xa0
        contenu = fichier_txt.read().replace("\xa0", "")
        # on concidère le titre de l'article comme étant la base du nom de chaque fichier (ils correspondent) :
        titre = fichier.replace(".txt", "")
        # on n'a pas encore les questions, donc on indique une chaine de caractère vide :
        question = ""
        # même remarque pour les réponses :
        answer = ""
    # on remplie le dictionnaire ligne avec les informations de chaque document txt récupérées ci-dessus:
    ligne["id"]=id
    ligne["title"]=titre
    ligne["content"]=contenu
    ligne["question"]=""
    ligne["answer"]=""
    tableau.append(ligne)

#print(tableau)

# liste des noms des colonnes du future csv :
noms_colonnes = ['id', 'title', 'content', 'question', 'answer']

# enregistrement des données sous format tabulaire.
with (open('../../data/clean/sortie.csv',  'w', encoding='UTF8', newline='') as out_file):
    writer = csv.DictWriter(out_file, fieldnames=noms_colonnes)
    # on écrit les noms des colonnes du tableaux :
    writer.writeheader()
    # on insère tous les dictionnaires ligne dans le tableau grace à la fonction .writerows() :
    writer.writerows(tableau)

