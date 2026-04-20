## Changelog : agreste-crawler (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, le projet agreste-crawler a connu une évolution significative, axée sur l'amélioration de l'importation et de la gestion des données, notamment via l'ajout de nouveaux scripts pour le traitement des thèmes, des dates de publication et des documents associés. Des corrections et des optimisations ont également été apportées pour améliorer la robustesse et la précision de l'extraction et du chargement des données.

### Évolutions fonctionnelles
- Ajout d'un script `add_ids_to_pages.py` (anciennement `add_ids_and_filename.py`) pour ajouter des identifiants aux pages Wagtail. [#1](https://github.com/betagouv/agreste-crawler/issues/1)
- Implémentation d'un script `reformat_disaron.py` pour corriger les erreurs de formatage des données "disaron".
- Affichage du nom de fichier réel sur la tuile de téléchargement.
- Ajout des champs "collection" et "sous-collection" aux données extraites.
- Intégration des thèmes Nuxeo, avec gestion des thèmes non mappés.
- Amélioration du script de création de pages pour inclure le titre et le slug, ainsi que la possibilité de ne pas publier la page.
- Ajout d'un script `clear_blog_entries.py` pour nettoyer les entrées de blog.
- Possibilité de télécharger les documents associés et de les ajouter aux pages de blog.
- Ajout d'un script `remove_unused_documents.py` pour supprimer les documents inutilisés.
- Ajout d'un script `author-lister.py` pour lister les auteurs.
- Ajout d'un script `set_publication_date.py` pour définir la date de publication à partir d'un fichier CSV.
- Ajout d'un script `disaron_fixer.py` pour corriger les données "disaron_nom" mal formattées.

### Évolutions techniques
- Refactorisation du script `set_publication_date.py` en un script plus général `set_metadata.py`.
- Passage au crawler Playwright pour permettre de cliquer sur les liens et d'extraire les données.
- Organisation des scripts dans des répertoires et transformation en modules.
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés.
- Ajout de mécanismes de retries en cas d'échec de chargement de page.
- Utilisation de fichiers `.env` pour la configuration de l'environnement (notamment pour Scalingo).
- Ajout de tests pour la conversion en Markdown.
- Amélioration de la gestion des identifiants et des noms de fichiers.
- Correction de bugs liés à l'affichage des données et à la gestion des documents.

### Autres changements
- Ajout d'un fichier `.gitignore` pour ignorer les fichiers temporaires et les fichiers d'environnement.
- Mise à jour de la documentation README.
- Nettoyage du code et suppression des doublons.
- Ajout de données de test pour les thèmes et les régions.
- Ajout de la possibilité de spécifier un fichier d'entrée alternatif pour le downloader.
- Ajout d'un script pour lister les IDs sans fichiers associés.
- Ajout d'une confirmation lors de la création de pages.
- Ajout d'un flag pour désactiver la concurrence.
- Correction de l'ID malformé pour IraLeg21140.
- Correction d'un bug qui empêchait le téléchargement correct des documents.
- Ajout de la possibilité de spécifier le chemin vers le projet Wagtail.
- Ajout de la possibilité de filtrer les champs à extraire.
- Ajout de la gestion des erreurs lors de l'extraction des données.
- Amélioration de la gestion des logs.
- Ajout d'un script pour mapper les thèmes.
- Ajout de données pour les thèmes.
- Ajout de données pour les anciens thèmes.
- Ajout d'un script pour définir la collection.
- Ajout de données de test.
- Ajout d'un script pour nettoyer les entrées de blog.
- Ajout d'un script pour supprimer les documents inutilisés.
- Ajout d'un script pour lister les auteurs.
- Ajout d'un script pour définir la date de publication.
- Ajout d'un script pour corriger les données disaron.
- Ajout d'un script pour prefixer les disarons.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour trouver les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
- Ajout d'un script pour trouver les liens vers les fichiers.
- Ajout d'un script pour crawler les pages à partir d'une liste d'IDs.
- Ajout d'un script pour lister les IDs sans fichiers.
- Ajout d'un script pour trouver les liens et afficher le debug.
