## Changelog : agreste-crawler (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du processus de création de pages web à partir de données, notamment en préparant les données pour de nouvelles vagues d'uploads et en corrigeant des erreurs de données existantes. Des améliorations ont également été apportées à la gestion des fichiers, à la journalisation et à la compatibilité des données.

### Évolutions fonctionnelles
- Ajout de la date de première publication et des documents lors de la création de pages.
- Amélioration du script `create_blog_entry.py` pour accepter de nouveaux formats d'entrée et autoriser une liste de documents vide.
- Ajout d'identifiants HTML aux blocs de contenu (chapeau et titre complémentaire) pour faciliter le ciblage CSS.
- Correction de l'affichage du nom de fichier correct sur la tuile de téléchargement.
- Ajout des champs "collection" et "sous-collection" au data-finder.
- Ajout du script `data_exporter` pour l'exportation de données.

### Évolutions techniques
- Refactoring et amélioration de la journalisation dans les scripts `page_creator` et `downloader`.
- Ajout de scripts pour le pré-traitement des données de téléchargement (`downloader_preprocessor.py`).
- Ajout de scripts pour la gestion et le mappage des thèmes (`map_themes.py`, `set_collection.py`).
- Refactoring du script `set_publication_date.py` en un script plus général `set_metadata.py`.
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés pour le préfixeur de données.
- Suppression du code obsolète (grafra).
- Renommage de plusieurs fichiers et variables pour plus de clarté.

### Autres changements
- Correction de plusieurs erreurs de données dans les fichiers CSV, notamment des erreurs de dates et de noms de fichiers.
- Suppression des caractères non-ASCII, des diacritiques et des apostrophes dans les données.
- Normalisation des noms de fichiers pour une meilleure compatibilité.
- Ajout de fichiers de données pour les 2ème et 3ème vagues de téléchargements.
- Ajout d'un fichier `.gitignore` pour exclure le dossier `theme-mapper/output/`.
- Amélioration de la documentation pour `page_creator` et `disaron_prefixer.py`.
- Ajout de tests pour la correction des noms de fichiers.
- Correction de bugs mineurs et amélioration de la lisibilité du code.
