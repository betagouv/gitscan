## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 22 avril 2026)

### Résumé
Ce changelog couvre une période d'amélioration continue des pipelines de données. Les modifications incluent des corrections de bugs, des optimisations de performance, des refactorisations pour une meilleure maintenabilité et l'ajout de nouvelles colonnes dans certaines tables. Un effort particulier a été fait pour améliorer la robustesse des pipelines et la gestion des erreurs.

### Évolutions fonctionnelles
- Correction de la récupération de l'ID maximum pour les pétitions [#654](https://github.com/datagouv/datagouvfr_data_pipelines/issues/654).
- Ajout de nouvelles colonnes dans les tables météo et IRVE.
- Exclusion du JDD consolidé du PAN pour IRVE [#645](https://github.com/datagouv/datagouvfr_data_pipelines/issues/645).
- Correction du chemin vers le fichier geojson dans IRVE [#648](https://github.com/datagouv/datagouvfr_data_pipelines/issues/648).
- Correction des types de données (dtypes) dans les fichiers Parquet.

### Évolutions techniques
- Refactorisation du DAG météo postgres pour une vérification plus précoce de l'insertion déjà effectuée [#650](https://github.com/datagouv/datagouvfr_data_pipelines/issues/650).
- Déplacement de toutes les informations relatives au schéma dans un dossier dédié [#649](https://github.com/datagouv/datagouvfr_data_pipelines/issues/649).
- Optimisation de la vérification de l'existence des fichiers PostgreSQL.
- Suppression d'un DAG obsolète de géocodage SIRENE.
- Amélioration de la gestion des erreurs lors des requêtes PUT vers datagouv.
- Prévention des exécutions concurrentes de certains DAGs.
- Amélioration de l'efficacité du code et correction de petites erreurs (variables incorrectes, double slash).

### Autres changements
- Suppression d'une vérification de santé inutile.
- Désactivation des notifications pour les tops.
- Suppression de l'utilisation de Markdown temporaire.
- Amélioration du linting du code.
- Ajout de notifications sur le canal Simplifions et Tchap.
- Nettoyage et simplification du code.
