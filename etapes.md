# outils_de_traitement_de_corpus
Dépot git pour le cours d'outils de traitement de corpus du M1 Plurital 2023/24.

## Séance 1 :

#### __Tâche que je souhaite réaliser__ :

Je souhaite m'interessée à la tâche appelée dans le TAL Question/Answering ou Question/Réponse en français. Cette tâche consiste à partir d'un corpus, à ce que l'on pose des questions par exemple déterminées par un groupe de spécialistes humains et le programme va apprendre et reprérer les informations du corpus afin de répondre et ressortir un passage du corpus qui contient la réponse à la question.

_ Chercher les données Wikipédia sur lesquelles je souhaite travailler._

#### __Corpus qui répondrait à cette tâche__ :

- Corpus SQuaD

Liens vers le corpus :

- https://paperswithcode.com/dataset/SQuaD _( à appronfondir )_
- https://huggingface.co/datasets/rajpurkar/SQuaD

Le corpus qui pourrait répondre à cette tâche serait par exemple le corpus SQuaD diminutif de Stanford Question Answering Dataset. Il s'agit d'un corpus connu et beaucoup utilisé pour répondre à cette tâche.

Voici les caractéristiques de ce corpus :

- C'est un corpus créer pour la tâche générale de Question/Answering.
- La sous-tâche de ce corpus est  de type extractive-qa, c'est un modèle utilisé en TAL qui permet de faire l'extraction d'information permettant de répondre à une question.
- L'unique langue de ce corpus est l'anglais.
- Sa taille est de 87.6k de lignes.
- Les données sont prises du site Wikipédia.
- Le corpus été aussi créer avec de l'aide exterieur (crowdsource) et de la recherche (found). Ceci surtout au niveau des questions qui ont été générée par des humains.
- La licence de ce corpus est cc-by-sa-4.0.


Un autre exemple de corpus pour répondre à cette tâche serait le corpus MS MARCO. Ce dernier semble plus complet au niveau des réponses produites, il peut produire des réponses à partir de partie du corpus, il peut formuler à la manière d'un humain ses réponses et donner plusieurs éléments de réponse quand celà est possible.

(https://hal.science/hal-02377119 : lien intéressant, donnant des indication sur le question/answering)

#### __A quel type de prédiction peut servir ce corpus__ :

Ce corpus permet par exemple de produire des chatbots, un module de questions/réponses. Celà permet aussi de retrouver plus rapidement une information.

#### __A quel modèle il a servi :__

Ce corpus a été utilisé dans de nombreux modèle de par sa popularité. Nous pouvons cité les modèles comme __Dynamic-TinyBERT__ (https://huggingface.co/Intel/dynamic_tinybert), __DistilBERT__ base cased distilled SQuaD (https://huggingface.co/distilbert/distilbert-base-cased-distilled-SQuaD) pour des tâches de Q/A. Ce deux derniers modèles sont combinés au transfomers BERT.

Il y a encore __T5__ (https://huggingface.co/valhalla/t5-base-e2e-qg) pour une tâche de Text2Text Generation. La tâche de text2text generation consiste à générer un texte à partir d'un autre texte de départ. C'est une tâche qui permet de faire par exemple un résumé d'un texte ou la traduction de ce dernier dans une autre langue.

#### __D'autres choses concernant ce corpus :__

Voici comment est constitué le corpus :

- une colonne __id__ contenant un str de l'id de la Q/A
- une colonne __title__ contenant un str du titre de l'article Wikipédia
- une colonne __context__ contenant un str du contenu texte de l'article
- une colonne __question__ contenant un str de la question posée à propos de l'article
- une colonne __answers__ contenant un dictionnaire avec une clé "text" avec pour valeur une liste avec l'extrait du contexte qui répond à la question et une clé __answer_start__ qui a pour valeur un entier (int) qui correspond à la position du premier caractère de la section de réponse

Voici l'exemple de la structure d'une donnée présenté dans sur la page huggingFace du modèle :
`{"answers": {"answer_start": [1],"text": ["This is a test text"]},"context": "This is a test context.","id": "1","question": "Is this a test?","title": "train test"}`

__Remarque__ : Il existe une verison plus récente de ce même corpus nommée SQuaD2.0, cette version n'est pas forcément meilleure que la précédente. Ce qui change est la plage de donnée Wikipédia. De plus, cette version 2.0 contient sur l'ensemble de ses questions des questions qui n'ont pas de réponse possible. C'est une différence majeure par rapport à la première version du corpus.


## Séance 2 :

### Création du scrapper : 
L'objectif de cette séance est de programmer un scrapper. Ce dernier viendrait à partir d'une première url, récupérer toutes les informations que l'on souhaite sur tous les autres liens de la page.

Dans le cas du corpus de référence SQuaD choisi, nous devions donc récupérer toutes les introductions Wikipédia des liens de la première page. Le plus important étant la manipulation des données, la page sur laquelle le scrapper se lance est la suivante : https://fr.wikipedia.org/wiki/Chat .

Nous sommes donc lancés sur une tâche de Q/A sur le thème général des chats.

Le programme utilise les librairies requests (qui permet de récupérer le contenu d'un site) et lxml (qui récupère le contenu textuel du site).

Voici le déroulement du programme de scrapping, `scripts/process/scrapper.py` :

1. il visite le lien https://fr.wikipedia.org/wiki/Chat
2. il récupère tous les liens de cette page, qui sont situés dans des balises `a`, avec attribut `href` (avec la fonction `get_urls()`)
3. il parcourt toutes ces urls dans la fonction `save_all_urls_contents()`, et pour chacune d'entre elles, il récupère le contenu textuel de l'intro (avec la fonction `get_first_header_text()`), et enregistre ce contenu dans un fichier texte (avec la fonction `save_txt()`).

Nous avons limité le scrapping à 50 liens car dans le cadre de ce projet le plus important n'est pas le nombre de nos données mais la manière dont on va les manipuler.
De plus, 50 liens n'étant pas énorme, les données ont donc été mises sur ce dépôt git dans le dossier `data/raw/` .
Les données textuelles sont déjà assez propres et ne nécessitent pas de nettoyage, elles ont donc été directement placées dans le sous-dossier `data/raw/`.

Vous trouverez aussi un dossier `tests/` qui contient quatres programmes pythons ayant servis à la prise en main des différentes librairies pour scrapper le web.


### Création du csv : 

Afin de coller le plus possible à notre corpus de référence, nous avons besoin d'ordonner nos données dans un fichier au format sérialisé. Dans notre cas, le corpus SQuaD est sérialisé sous un format tabulaire. Nous avons donc décider d'avoir nos données sous format **CSV**. 
Le script servant à cet effet est `script/process/to_csv.py`. Voici son fonctionnement : 

1. il parcourt tous les documents ressortant de l'aspiration du programme précédement présenté ;
2. il extrait les informations de ces documents (titre, contenu, ID), qu'il stocke dans un dictionnaire (nous avons donc une liste de dictionnaires) ;
3. il écrit dans un fichier de type csv les informations contenues dans les dictionnaires.


## Séance 3 : 

### Ajout des colonnes manquantes :

A l'aide du programme `script/process/add_Q_A_to_csv.py`, nous avons pu ajouter les colonnes de questions et de réponses manquantes à notre corpus sérialisé. Ces données n'étaient pas encore collectées. Nous avons du les générer manuellement tout comme celà avait été fait pour le corpus de référence. Ces questions/réponses sont présentes dans le csv `data/clean/Q_A_chats.csv`. Afin d'avoir un corpus identique dans sa forme et ses colonnes par rapport à SQuaD, le programme `add_Q_A_to_csv.py` vient calculer l'emplacement de la partie du contexte prise pour la réponse. Bien que la création des questions et la selection des réponses ait été manuelle, l'ID du début de la réponse dans "answer_start" a été récupéré automatiquement car il s'agissait d'une technique trop laborieuse.
Le csv final de sortie de ce programme est : `data/clean/datas_chat.csv`.

### Exploration du corpus avec _csv_, _pandas_ et _datasets_ : 

Afin d'observer le contenu de nos colonnes et de notre csv en général, nous avons le notebook `notebooks/open_data.ipynb`. 
Ce dernier ouvre notre csv et permet d'afficher par exemple le contenu d'une ligne du tableau grace aux librairies _csv_ et _pandas_. Ce programme nous sert à comparer le format de nos données avec celui de notre corpus de référence qui se trouve sur HuggingFace. Nous pouvons importer et ouvrir le corpus SQuaD grâce à la librairie _datasets_ qui a accès à chaque corpus déposé sur le site. 
Grâce à ce programme nous pouvons voir que notre corpus est de la même forme que le corpus de référence. Il contient les mêmes colonnes avec le mêmes types de données. 
Le corpus est donc prêt pour les étapes suivantes du projet.


## Séance 4 : 

### Choix des métriques :

Notre corpus est un corpus constitué pour une tâche de question/answering. Nos métriques vont donc être tournées vers le texte, la taille des contenus de nos colonnes par exemple. 
Comme les réponses sont issues des contenus des articles Wikipédia, la première métrique pourrait être la taille du contenu par rapport à la taille de la réponse. Normalement la réponse ne doit pas être plus longue que le contenu. Autrement celà signifie qu'il y a une erreur dans la ligne du tableau.
Nous avons appliqué l'analyseur syntaxique _spacy_ à notre corpus.

### Visualisation des données avec des graphiques : 

Afin d'obtenir des graphiques de la répartition des tailles des contenus et des réponses, nous utilisons la librairie _matplotlib_. 
Nous obtenons donc le graphique de la répartition de la taille des contenus et de la taille des réponses. Nous avons aussi le graphique de la lois de Zipf sur ces deux derniers. 
Nous parlons ici du programme `notebooks/visualise_data.ipynb`. 
Il applique ces graphiques sur les données du corpus de référence SQuaD, puis sur notre corpus. L'analyse morphosyntaxique a été adaptée en fonction de la langue des deux corpus qui est diffirentes. En changeant le module de _spacy_ utilisé, l'un anglais et l'autre français.

Nous avons rencontré des difficultées concernant la récupération de la taille des réponses car la colonne _answer_ contient normalement un dictionnaire, mais _pandas_ reconnait cet élément comme une chaine de caractères. Même en utilisant la librairie _json_, nous n'avons pas réussi à convertir correctement cette chaine de caractères en dictionnaire sans rencontrer d'erreur.
La taille des réponses a donc été calculée sur la longueur de la chaine complète plutôt que la réponse en elle-même. 
Voici un exemple de ce qui de ce qui se trouve dans la colonne _answer_ et de ce qu'on souhaite normalement prendre : 

- `{'text': 'la sympathie', 'answer_start': 124}` : contenu de la colonne.
- `la sympathie` : réponse qu'on souhaite prendre en compte.

La taille indiquée est donc approximative car elle sera plus grande que ce qu'elle devrait être mais elle permet tout de même d'avoir une représentation de la répartition et de l'ordre de grandeur de la taille des réponses.


## Séance 5 : 

### Calcul de la corrélation et test de significativité : 

Nous avons appliqué les calculs de corrélation et le test de significativité à la relation entre les métriques de longueurs des contextes et celles des réponses de notre corpus.
Les résultats obtenus montrent qu'il n'y pas de corrélation entre ces valeurs car ils sont proches de 0. 
De plus, les résultats obtenus ne sont pas du tout significatifs car les p-values sont toutes supérieures à 0,05.
Tous les résultats sont accessibles sur le notebook `notebooks/significativity_test.ipynb`. Vous y trouverez aussi un graphique de la longueur des contextes en fonction de la longueur des réponses. Vous y trouverez aussi une démonstration de la loi binomiale avec l'exemple de la probabilité de tomber sur pile ou face lors d'un lancer de pièces.

### Nettoyage du corpus : 

Le corpus a été nettoyé, en supprimant les données aberrantes et les doublons en fonction de la tailles des contextes de notre corpus.
Il n'y avait aucun doublon dans notre corpus.
Le programme est un notebook dans `notebooks/clean_data.ipynb`.

Le corpus nettoyé est dans `data/clean/clean_datas_chat.csv`.

### Augmenter les données :

Nous n'avons pas le besoin d'augmenter nos données car notre tâche est Question/Answering. Contrairement à une tâche de classification qui a généralement besoin d'augmenter les données.

### Evaluation du corpus : 

Notebook : `notebooks/evaluate_data.ipynb`

#### Métriques adaptées : 

Les métriques d'évaluations des tâches de Q/A sont les suivantes : 
- __Exact Match__ (calcule la ressemblance stricte entre la réponse prédite et la vraie réponse).
- __F1-Score__ (valorisaiton des faux positifs et des faux négatifs mot pour mot entre les réponses prédites et les vraies réponses)

Lien vers la page sur la tâche de Q/A : 
- https://huggingface.co/tasks/question-answering 
Section : 
- "Metrics for Question Answering" 

Page expliquant l'importation des métriques du corpus SQuaD, utilisé dans le notebook : 
- https://github.com/huggingface/evaluate/tree/main/metrics/SQuaD 

#### Métriques proposées : 

Nous pouvons proposer quelques autres métriques d'évaluations pour notre corpus : 
- ROUGE : Recall-Oriented Understudy for Gisting Evaluation
- WER : taux d'erreur mot entre réponse de référence et réponse prédite

Ces métriques d'évaluations ont été détaillées dans le notebook. 

Le calcul ROUGE n'a pas été fait dans le code mais vous pourrez trouver celui du WER. Nous avons produit la focntion calcul_wer() qui calcule le WER entre une référence et une prédiction. 
Comme nous n'avons pas lancé de modèle sur nos données, nous avons tout de même produit le code qui permettrait de comparer les références avec les prédictions.

## Séance 6 : 

### Split du corpus en train, test et dev : 

notebook : `notebooks/split_corpus.ipynb`

Afin de répartir notre corpus en trois parties qui sont le train, le test et le dev, nous avons utilisé la librairie __scikit-learn__. 
La fonction permettant la répartition est _`train_test_split()`_.

Afin de répartir en trois parties et non deux, nous avons appliqué deux fois cette dernière fonction. La première ayant servi à séparer la partie test du reste. Et la seconde ayant servi à répartir le reste dans les parties train et dev.
Nous avons réparti les données de manière aléatoire pour de meilleurs résultats et une répartition homogène des données entre les trois parties.

### Création de la carte de dataset :

Nous avons écrit la carte de dataset qui est le fichier `README.md` de ce dépôt github. Elle contient les métadonnées en format YAML et une description du dataset nommé _TALQuAD_ rédigé en format markdown.

### Application de linters à nos codes : 

Afin d'avoir l'ensemble de nos notebooks et scripts pythons correctement rédigés et propres, nous avons appliqué les formateurs de code python black et isort.

- __black__ : https://pypi.org/project/black/
- __isort__ : https://pycqa.github.io/isort/
