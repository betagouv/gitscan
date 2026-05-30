# Synthèse d'activité : datagouv (du 29 avril 2026 au 29 mai 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour importantes de plusieurs de ses services et APIs.  Les efforts se sont concentrés sur l'amélioration de la qualité des données (découpage administratif, données cadastrales), la modernisation de l'infrastructure (migration vers Airflow 3, PNPM, Rails 8.1) et l'ajout de nouvelles fonctionnalités pour faciliter l'accès et l'utilisation des données, notamment via des APIs (apistration, api-tabular, api-meteo) et des outils d'intégration (relais, datagouv-mcp). L'accent a également été mis sur la sécurité avec la correction d'une vulnérabilité dans `datagouv-mcp`.

## Sécurité
- Correction d'une vulnérabilité de sécurité (CVE-2026-44432) dans [datagouv-mcp](/repos/datagouv/datagouv-mcp) en contraignant la version de la librairie `urllib3`.

## Autres changements notables
- Migration vers Rails 8.1 et intégration de GoodJob pour la gestion des tâches asynchrones dans [relais](/repos/datagouv/relais).
- Migration vers PNPM dans [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) et [schema.data.gouv.fr](/repos/datagouv/schema.data.gouv.fr).
- Mise à jour vers Airflow 3 dans plusieurs dépôts, notamment [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) et [api-tabular](/repos/datagouv/api-tabular).
- Intégration de FranceConnect pour l'API Particulier dans [apistration](/repos/datagouv/apistration).

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de l'intégration avec CNOUS et la gestion de demandes proactives.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Amélioration de la robustesse des pipelines, migration vers Airflow 3 et adaptation pour l'infrastructure OVH.
- [apistration](/repos/datagouv/apistration) : Ajout d'une API pour la gestion des délégations d'éditeurs et intégration de FranceConnect.
- [datagouv-mcp](/repos/datagouv/datagouv-mcp) : Ajout de nouveaux outils pour interagir avec les données data.gouv.fr et correction d'une vulnérabilité de sécurité.
- [cdata](/repos/datagouv/cdata) : Amélioration de la recherche, de l'administration et de l'accessibilité de la plateforme.
- [hydra](/repos/datagouv/hydra) : Optimisation des exportations de données avec l'ajout des formats Parquet et GeoJSON.
