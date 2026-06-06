# Synthèse d'activité : datagouv (du 29 mai au 04 juin 2026)

## Résumé de l'activité
L'organisation datagouv a connu une semaine riche en activités, avec des mises à jour significatives sur plusieurs dépôts. Les efforts se sont concentrés sur l'amélioration de l'infrastructure (migration vers PNPM, Airflow 3, GoodJob), l'ajout de nouvelles fonctionnalités (intégration CNOUS dans relais, API de délégations dans apistration, export de données Parquet et GeoJSON dans hydra, notifications dans hubee), et l'amélioration de la qualité des données (mises à jour des données cadastrales et de découpage administratif). Plusieurs dépôts ont bénéficié de corrections de bugs et d'améliorations de la documentation, renforçant la stabilité et l'accessibilité des outils.

## Sécurité
Une vulnérabilité de sécurité a été corrigée dans [datagouv-mcp](/repos/datagouv/datagouv-mcp) en contraignant la version de la librairie `urllib3`.

## Autres changements notables
- Migration vers PNPM dans [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) pour une meilleure gestion des dépendances.
- Mise à jour vers Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack) pour des performances améliorées.
- Refonte majeure de l'infrastructure de [relais](/repos/datagouv/relais) avec passage à Rails 8.1 et intégration de GoodJob.
- Intégration de FranceConnect dans [apistration](/repos/datagouv/apistration) pour l'API Particulier.

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de l'intégration CNOUS et de la gestion des demandes proactives.
- [hydra](/repos/datagouv/hydra) : Ajout de nouvelles fonctionnalités d'export de données (Parquet et GeoJSON) et intégration du stockage S3.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Optimisation de la consommation de mémoire, migration de traitements vers Airflow et corrections de bugs.
- [cdata](/repos/datagouv/cdata) : Améliorations de la recherche, de l'administration et de l'authentification.
- [apistration](/repos/datagouv/apistration) : Ajout d'une API pour la gestion des délégations d'éditeurs et intégration de FranceConnect.
