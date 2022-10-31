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