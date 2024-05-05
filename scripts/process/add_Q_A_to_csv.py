"""
Ce programme récupère les données du fichier csv Q_A_chats.csv (dans data/clean/).
Il va chercher la valeur de answer-start en comparant les réponses aux contenus de chaque intro d'article.
Il retourne un csv avec tout le corpus sous sa forme attendue et finale, ayant le même format que le corpus SQuAD.
"""

import csv

# On créé une liste pour chaque colonne pour pouvoir remplir un csv avec toutes les informations au complet.
liste_titres = []
liste_ids = []

# On créé la liste des contenu pour les ocmparer aux réponses et avoir l'id du début de cette réponse
# (respectivement comme le corpus SQuAD)
liste_contenu = []

# On va récupérer la liste de questions et des réponses faites manuellement se trouvant dans le fichier Q_A_chats.csv :
# Comme la grandeur du corpus importe peu dans ce projet, il n'y a qu'une question par fichier.
liste_questions = []
liste_reponses = []

with open("/home/lise/Documents/TAL_M1S2/outil_de_traitement_de_corpus/outils_de_traitement_de_corpus/data/clean/Q_A_chats.csv", "r", encoding='UTF8') as questions_reponses :
    reader = csv.reader(questions_reponses, delimiter=",")
    for colonne in reader:
        # les questions se trouve dans la pénultième colonne
        liste_questions.append(colonne[-2])
        # les réponses sont dans la dernière colonne et sont des sections du contenu de chaque article
        liste_reponses.append(colonne[-1])
        # récupération des contenus
        liste_contenu.append(colonne[2])
        # récupération des ids et des titres
        liste_ids.append(colonne[0])
        liste_titres.append(colonne[1])


# On retire les titres de chaque colonne qui sont au début de chaque liste.
liste_questions.remove("question")
liste_reponses.remove("answer")
liste_contenu.remove("content")
liste_ids.remove("id")
liste_titres.remove("title")

# Format de la dernière colonne de SQuAD :  { "text": [ "Saint Bernadette Soubirous" ], "answer_start": [ 515 ] }
# c'est un dictionnaire avec le text de la réponse et l'id du début de la réponse dans le contenu entier de l'article
# Création du dictionnaire qui contiendra ces informations :
dico_answer = {}
# Cette liste contiendra tous les dico_answer.
liste_dico_answers = []

# On créé la variable id qui portera la valeur de answer_start pour chaque réponse.
id_answer = 0

for i in range(len(liste_reponses)):
    # On cherche l'id de départ de la réponse dans le contenu associé.
    id_answer = liste_contenu[i].find(liste_reponses[i])
    dico_answer["text"] = liste_reponses[i]
    dico_answer["answer_start"] = id_answer
    # On ajoute la réponse et son id dans une liste afin de plus facilement les écrire dans le csv de sortie.
    liste_dico_answers.append(dico_answer)
    dico_answer = {}

# On enregistre toutes les informations au complet dans un csv de sortie qu'on appelera datas_chat.csv.
# Ce fichier se trouve dans data/clean/.
# Pour cela, on procède de la même manière que dans le programme to_csv.py.
tableau = []
for num_ligne in range(len(liste_ids)):
    # Pour chaque ligne on part d'un dictionnaire avec toutes ses informations :
    ligne = {}

    # On remplie le dictionnaire ligne avec les informations récupérées ci-dessus.
    ligne["id"]=liste_ids[num_ligne]
    ligne["title"]=liste_titres[num_ligne]
    ligne["content"]=liste_contenu[num_ligne]
    ligne["question"]=liste_questions[num_ligne]
    ligne["answer"]=liste_dico_answers[num_ligne]
    tableau.append(ligne)

# Liste des noms des colonnes du csv final, conforme à SQuAD :
noms_colonnes = ['id', 'title', 'content', 'question', 'answer']

# Enregistrement des données sous format tabulaire.
with (open('/home/lise/Documents/TAL_M1S2/outil_de_traitement_de_corpus/outils_de_traitement_de_corpus/data/clean/datas_chat.csv',  'w', encoding='UTF8', newline='') as out_file):
    writer = csv.DictWriter(out_file, fieldnames=noms_colonnes)
    # on écrit les noms des colonnes du tableaux :
    writer.writeheader()
    # on insère tous les dictionnaires ligne dans le tableau grace à la fonction .writerows() :
    writer.writerows(tableau)