# outils_de_traitement_de_corpus
Dépot git pour le cours d'outils de traitement de corpus du M1 Plurital 2023/24.

## Séance 1 :

__Tâche que je souhaite réaliser__ :

Je souhaite m'interessée à la tâche appelée dans le TAL Question/Answering ou Question/Réponse en français. Cette tâche consiste à partir d'un corpus, à ce que l'on pose des questions par exemple déterminées par un groupe de spécialistes humains et le programme va apprendre et reprérer les informations du corpus afin de répondre et ressortir un passage du corpus qui contient la réponse à la question.

_ Chercher les données Wikipédia sur lesquelles je souhaite travailler._

__Corpus qui répondrait à cette tâche__ :

- Corpus SQuAD

Liens vers le corpus :

- https://paperswithcode.com/dataset/squad _( à appronfondir )_
- https://huggingface.co/datasets/rajpurkar/squad

Le corpus qui pourrait répondre à cette tâche serait par exemple le corpus SQuAD diminutif de Stanford Question Answering Dataset. Il s'agit d'un corpus connu et beaucoup utilisé pour répondre à cette tâche.

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

__A quel type de prédiction peut servir ce corpus__ :

Ce corpus permet par exemple de produire des chatbots, un module de questions/réponses. Celà permet aussi de retrouver plus rapidement une information.

__A quel modèle il a servi :__

Ce corpus a été utilisé dans de nombreux modèle de par sa popularité. Nous pouvons cité les modèles comme __Dynamic-TinyBERT__ (https://huggingface.co/Intel/dynamic_tinybert), __DistilBERT__ base cased distilled SQuAD (https://huggingface.co/distilbert/distilbert-base-cased-distilled-squad) pour des tâches de Q/A. Ce deux derniers modèles sont combinés au transfomers BERT.

Il y a encore __T5__ (https://huggingface.co/valhalla/t5-base-e2e-qg) pour une tâche de Text2Text Generation. La tâche de text2text generation consiste à générer un texte à partir d'un autre texte de départ. C'est une tâche qui permet de faire par exemple un résumé d'un texte ou la traduction de ce dernier dans une autre langue.

__D'autres choses concernant ce corpus :__

Voici comment est constitué le corpus :

- une colonne __id__ contenant un str de l'id de la Q/A
- une colonne __title__ contenant un str du titre de l'article Wikipédia
- une colonne __context__ contenant un str du contenu texte de l'article
- une colonne __question__ contenant un str de la question posée à propos de l'article
- une colonne __answers__ contenant un dictionnaire avec une clé "text" avec pour valeur une liste avec l'extrait du contexte qui répond à la question et une clé __answer_start__ qui a pour valeur un entier (int) qui correspond à la position du premier caractère de la section de réponse

Voici l'exemple de la structure d'une donnée présenté dans sur la page huggingFace du modèle :
`{"answers": {"answer_start": [1],"text": ["This is a test text"]},"context": "This is a test context.","id": "1","question": "Is this a test?","title": "train test"}`

__Remarque__ : Il existe une verison plus récente de ce même corpus nommée SQuAD2.0, cette version n'est pas forcément meilleure que la précédente. Ce qui change est la plage de donnée Wikipédia. De plus, cette version 2.0 contient sur l'ensemble de ses questions des questions qui n'ont pas de réponse possible. C'est une différence majeure par rapport à la première version du corpus.
