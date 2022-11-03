# Instructions de lancement

1. Installation du package test_graph

Se rendre à la racine, ensuite deux manières de faire 
à partir de anaconda prompt:

Soit activer un environnement virtuel
    conda create -n test_graph_env 
    conda activate test_graph_env
    conda install --file requirements.txt -c conda-forge (cette étape prend du temps)
Ensuite pip install -e . pour installer le package

Soit installer le package directement dans l'environnement de base avec 
pip install -e . à la racine de répertoire

NB : à noter que la première procédure peut ne pas fonctionner sur un ordinateur
avec certaines sécurités (cf https://github.com/conda/conda/issues/8691)

2. Répertoire de données

Je n'ai pas versionné le répertoire data/ (voir le .gitignore)
Il faut donc placer dans ce répertoire l'ensemble de la donnée fournie 
pour réaliser le test au préalable de l'exéution du code

3. Exécution du code

Une fois le package installé dans l'environnement, deux manières de lancer le traitement :

a) via test.ipynb dans le dossier notebooks/
Cela permet de visualiser les résultats directement dans le notebook
(étapes intermédiaires, création du graphe, résultat de la feature
identifiant le journal mentionnant le plus grand nombre de médicaments),
et de dumper le JSON représentant le graphe dans le dossier output/

b) soit via le main.py en ligne de commande, pour cela
se placer à la racine du répertoire et lancer la commande suivante :
python src/test_graph/main.py
le main dumpe le JSON représentant le graphe dans le dossier output/
et affiche le journal mentionnant le plus grand nombre de médicaments différents

NB : le fichier output/ est versionné et le résultat peut donc être 
directement visualisé sur le repo

# Détails sur la construction des features

0. Enchainement des étapes

Chargement des données (package load) -> 
Cleaning/preprocessing (package preprocessing) ->
Construction du graphe (package graph) ->
Feature retournatn le journal mentionnant le plus de médicaments différents (package counting_feature)

1. Construction du graphe

On prend pour chaque médicament les étapes suivantes :
1. Trouver le subset de la base d'articles pubmed 
dont le titre de l'article mentionne le médicament
2. Trouver le subset de la base d'essais cliniques 
dont le titre mentionne le médicament
3. Créer un dictionnaire résumant l'information sur les journaux
ayant publié un article dont le titre mentionne le médicament
(que l'article soit pubmed ou essai cliniue)
4. Créer un dictionnaire résumant l'information sur les articles
pubmed mentionnant le médicament
5. Créer un dictionnaire résumant l'information sur les articles
essais cliniques mentionnant le médicament
6. Stocker l'information dans un dictionnaire final avec les trois clés suivantes :
pubmed_articles, journal, trials

Finalement chacun de ces dictionnaires est associé à une clé qui est
le atccode du médicament

2. Feature retournant le journal mentionnant le plus de médicaments différents

Prend en entrée le graphe produit à l'étape précédente. 
La feature se décompose ensuite en trois étapes de traitement :
1. Extraire du graphe les identifiants uniques de chaque drug (fonction get_drug_ids_from_graph)
2. Pour chaque drug, extraire la liste des journaux qui la mentionnent (sans doublons) et concaténer 
les listes produites pour chaque drug (fonction get_journal_unique_list)
3. Renvoyer le nom du journal qui apparait le plus dans la liste (fonction get_journal_with_max_drugs_from_list)


# Requêtes SQL

Elles sont placées dans le fichier sql.txt

# Q1 : Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?

Eléments à considérer :
- Parallélisation du calcul (traitement en parallèle de chaque drug)
- Utilisation de Dask 
- Utilisation de Spark

# Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?

Réécriture du code selon la solution adoptée :
- en utilisant la librairie multiprocessing de python
- en utilisant Dask plutôt que pandas
- en passant par pyspark si accès à un cluster