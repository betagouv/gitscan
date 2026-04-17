## Changelog : agreste-crawler (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, le projet agreste-crawler a connu des évolutions majeures axées sur l'extraction, la préparation et l'importation de données vers Nuxeo.  De nouveaux scripts ont été ajoutés pour mapper des thèmes, gérer les dates de publication, et nettoyer les données, notamment en corrigeant des erreurs liées aux identifiants "disaron". L'objectif principal est d'améliorer la qualité et la complétude des données importées dans Nuxeo, ainsi que de faciliter le processus d'extraction et de transformation.

### Évolutions fonctionnelles
- Ajout d'un script pour ajouter des identifiants aux pages (`add_ids_to_pages.py`).
- Amélioration de l'affichage du nom de fichier lors du téléchargement.
- Ajout de champs "collection" et "sous-collection" aux données extraites.
- Ajout de la gestion du champ "catégorie".
- Possibilité de spécifier un fichier `.env.scalingo` pour la configuration en environnement de production.
- Ajout d'un script pour supprimer les documents inutilisés dans Nuxeo (`remove_unused_documents.py`).
- Création de scripts pour créer des pages Wagtail avec des titres, slugs et documents associés.
- Ajout d'un script pour lister les auteurs (`author-lister.py`).
- Ajout d'un script pour corriger les identifiants "disaron" mal formés (`disaron_fixer`).
- Ajout d'un script pour préfixer les fichiers avec l'identifiant "disaron" (`disaron_prefixer`).
- Ajout d'un script pour extraire les dates de publication à partir d'un fichier CSV (`set_publication_date.py`).
- Ajout d'un script pour définir les métadonnées de manière générale (`set_metadata.py`).
- Ajout d'un script pour mapper les thèmes (`map_themes.py`).
- Ajout d'un script pour définir la collection (`set_collection.py`).

### Évolutions techniques
- Refactorisation du code pour une meilleure organisation, avec déplacement des scripts dans des répertoires dédiés et transformation en modules.
- Utilisation de Playwright comme moteur de crawling pour permettre le clic sur des liens et l'extraction de données dynamiques.
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés.
- Ajout de mécanismes de retries en cas d'échec de chargement des pages.
- Utilisation de collections pour stocker les documents.
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés.
- Utilisation de `markitdown` pour convertir le contenu en Markdown.
- Correction de bugs liés à la gestion des identifiants et des données manquantes.
- Amélioration de la gestion des fichiers et des chemins.
- Ajout de tests de sanity check pour valider l'intégrité des données extraites.
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés.

### Autres changements
- Ajout d'un fichier `.gitignore` pour exclure les fichiers temporaires et les fichiers de configuration sensibles.
- Mise à jour de la documentation README.
- Ajout de commentaires dans le code pour améliorer la lisibilité.
- Correction de petites erreurs et améliorations de la qualité du code.
- Ajout de données de test pour faciliter le développement et les tests.
- Ajout d'un script pour nettoyer les entrées de blog (`clear_blog_entries.py`).
- Ajout de la possibilité de ne pas utiliser la concurrence pour le crawling avec le flag `--no-concurrency`.
