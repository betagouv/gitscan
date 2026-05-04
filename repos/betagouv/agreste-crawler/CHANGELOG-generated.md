## Changelog : agreste-crawler (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la qualité des données, notamment par la correction d'identifiants, le remplissage de données manquantes et la gestion des formats de données (disaron). De nouvelles fonctionnalités ont été ajoutées pour faciliter le téléchargement de fichiers et la création de pages Wagtail, ainsi que des scripts pour automatiser certaines tâches de préparation des données.

### Évolutions fonctionnelles
- Ajout d'un script pour ajouter la date de publication aux pages : [#1234](https://github.com/betagouv/agreste-crawler/issues/1234)
- Amélioration du script d'ajout d'identifiants aux pages, corrigeant une régression.
- Ajout d'un script pour reformater les champs "disaron_nom" en blocs HTML.
- Possibilité de spécifier des options d'entrée supplémentaires pour le script `disaron_prefixer.py`.
- Ajout d'un script pour télécharger des fichiers à partir d'une liste, avec journalisation des URL téléchargées.
- Ajout d'un script pour mapper les thèmes.
- Ajout d'un script pour définir la collection et la sous-collection.
- Ajout d'une confirmation lors de la création de pages.
- Le downloader accepte maintenant un format alternatif pour le fichier d'entrée.
- Le downloader utilise maintenant un emplacement différent pour le fichier d'entrée.

### Évolutions techniques
- Refactorisation du code pour organiser les scripts en répertoires et les transformer en modules.
- Amélioration de la journalisation (logging) pour faciliter le débogage et le suivi des erreurs.
- Ajout de tests et de gestion des erreurs pour le script de téléchargement.
- Modification du script `set_publication_date.py` pour lire les dates dans un fichier CSV et écrire les erreurs dans un autre fichier.
- Remplacement de l'utilisation de `h4` par `h2` pour les titres "Complement_titre".
- Utilisation d'une Collection pour les Documents.
- Correction de problèmes d'identifiants malformés.
- Ajout de la gestion des cas où le formatage "disaron" a déjà été effectué.

### Autres changements
- Ajout de documentation pour le script `disaron_prefixer.py`.
- Ajout de fichiers de données pour les thèmes et les téléchargements.
- Suppression de fichiers inutiles du `.gitignore`.
- Nettoyage du code et suppression de doublons.
- Ajout de champs "collection" et "sous-collection" au data-finder.
- Ajout du champ "categorie".
- Ajout de logs pour les champs manquants.
- Ajout d'un script pour corriger les "disaron_nom" mal formés.
- Ajout d'un script pour gérer les cas "bis" ou "ter" dans la correspondance des disarons.
- Ajout d'un script pour remplir les données manquantes.
- Ajout d'un script pour lister les auteurs.
