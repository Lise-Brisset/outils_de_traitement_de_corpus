---
annotations_creators:
- crowdsourced
language:
- fr
license: cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
dataset_info:
  config_name: plain_text
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: answer_start
      dtype: int32
  splits:
  - name: train
    num_examples: 31
  - name: test
    num_examples: 10
  - name: dev
    num_examples: 5
  dataset_size: 46
configs:
- config_name: plain_text
  data_files:
  - split: full corpus
    path: data/clean/clean_datas_chat.csv
  default: true
train-eval-index:
- config: plain_text
  task: question-answering
  task_id: extractive_question_answering
  splits:
    train_split: train
    eval_split: validation
  col_mapping:
    question: question
    context: context
    answers:
      text: text
      answer_start: answer_start
  metrics:
  - type: squad
    name: SQuAD
  - type: Q/A
    name: F1-Score
  - type: Q/A
    name: Exact Match
  - type: Summarization
    name: ROUGE
  - type: Q/A
    name: Word Error Rate (WER)
---

# Carte de dataset de TALQuAD : 

## Table of Contents
- [Dataset Card for "TALQuAD"](#carte-de-dataset-de-talquad)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#description-du-dataset)
    - [Dataset Summary](#resume-du-dataset)
    - [Supported Tasks and Leaderboards](#tache)
    - [Languages](#langue)
  - [Dataset Structure](#structure-du-dataset)
  - [Dataset Visualisation](#visualisation-du-dataset)
  - [Significativity Test](#test-de-significativite)
  - [Dataset Cleaning](#nettoyage-du-dataset)
  - [Dataset Evaluation](#evaluation-du-dataset)
  - [Data Splits](#repartition-du-dataset)
  - [Licensing Information](#licence-cc)
  - [Contributions](#contributions)

# Cours Outils de Traitement de Corpus, M1 PluriTal

## Description du dataset : 

- **Dépot Github:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus
- **Pourquoi ce dataset:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/etapes.md
- **Etapes de conception:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/etapes.md
- **Contact:** https://github.com/Lise-Brisset

### Résumé du dataset

PluriTAL Question Answering Dataset (TALQuAD) est un dataset conçue pour la tâche de TAL de question/answering. Il est constitué de données issues d'introduction d'article Wikipédia. Pour chaque article, une question et une réponse lui sont associés.

TALQuAD est constitué d'un total de 46 lignes dans un tableau à 5 colonnes (id, title, content, question, answer).

### Tâche 

Question Answering.

### Langue

Français (`fr`).

## Structure du dataset

La structure du dataset reprend exactement là que celle du dataset SQuAD (https://huggingface.co/datasets/rajpurkar/squad). 
La strucure est donc comme ceci : 

- `id`: un identifiant (int)
- `title`: nom de l'article Wikipédia (str)
- `context`: l'introduction de l'article aspiré (str)
- `question`: question posée (str)
- `answer`: réponse exacte à la question (dict)
  - `text`: réponse extraite du `context` (str)
  - `answer_start`: l'index du début de `text` dans le `context`

## Visualisation du dataset

- **Notebook:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/notebooks/visualise_data.ipynb

## Test de significativité

- **Notebook:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/notebooks/significativity_test.ipynb

## Nettoyage du dataset

- **Notebook:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/notebooks/clean_data.ipynb

Le dataset a été nettoyé en retirant les données aberrantes sur la base des longueurs des contenus. Il n'y avait pas de doublons.

Le nombre de lignes est passé de 50 à 46 après nettoyage.

## Evaluation du dataset 

- **Notebook:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/notebooks/evaluate_data.ipynb

Les métriques d'évaluations utilisées sont les suivantes : 
- squad : calcul les F1-Score et l'Exact Match (https://github.com/huggingface/evaluate/tree/main/metrics/squad)
- ROUGE : Généralement adapté à la tâche de résumé automatique, permet d'avoir un taux de similarité entre la réponse produite et la réponse de référence.
- WER : Taux d'erreur mot entre la réponse produite et la réponse de référence.

## Répartition du dataset

- **Notebook:** https://github.com/Lise-Brisset/outils_de_traitement_de_corpus/blob/main/notebooks/split_corpus.ipynb

Le dataset a été répartie en trois parties qui sont train, test et dev. Elles contiennent respectivement 31, 10 et 5 lignes de données.

## Licence CC 

CC BY-SA 4.0

## Contributions

[@LiseBrisset](https://github.com/Lise-Brisset)
