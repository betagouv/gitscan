# Synthèse d'activité : datagouv (du 29 mai au 12 juin 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue ces dernières semaines, marquée par des mises à jour importantes de plusieurs de ses projets clés.  Les efforts se sont concentrés sur l'amélioration de l'infrastructure (migration vers PNPM, Airflow 3, GoodJob), l'ajout de nouvelles fonctionnalités (intégration CNOUS dans relais, export Parquet/GeoJSON dans hydra, API pour apistration), et la mise à jour des données (découpage administratif, données cadastrales).  Ces évolutions visent à améliorer la performance, la sécurité, la maintenabilité et l'accessibilité des services proposés aux utilisateurs, notamment dans les domaines de la donnée ouverte, de l'efficacité énergétique et de l'évaluation de l'IA.  Plusieurs projets ont également bénéficié d'améliorations de la documentation et de corrections de bugs.

## Sécurité
Plusieurs projets ont intégré des améliorations de sécurité :
- [datagouv-mcp](/repos/datagouv/datagouv-mcp) a corrigé une vulnérabilité dans la librairie `urllib3`.
- [apistration](/repos/datagouv/apistration) a renforcé la protection contre les attaques CSRF et restreint l'accès à certains endpoints.
- [roles.data](/repos/datagouv/roles.data) a anonymisé les adresses email dans les logs Sentry pour améliorer la confidentialité.

## Autres changements notables
- [relais](/repos/datagouv/relais) a subi une refonte majeure avec la migration vers Rails 8.1 et l'intégration de GoodJob pour la gestion des tâches asynchrones.
- [hydra](/repos/datagouv/hydra) a été mis à jour vers Python 3.14 et a intégré le stockage S3.
- [data-engineering-stack](/repos/datagouv/data-engineering-stack) a migré vers Airflow 3.
- [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) a migré vers PNPM.
- [api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif) a déployé une nouvelle version de l'API géographique (v2).

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de nouvelles fonctionnalités d'intégration et de gestion des demandes.
- [hydra](/repos/datagouv/hydra) : Amélioration des performances, ajout de nouveaux formats d'export et intégration du stockage S3.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Optimisation de la consommation de mémoire, migration vers Airflow et correction de bugs.
- [apistration](/repos/datagouv/apistration) : Ajout d'une API pour les délégations et amélioration de la gestion des administrateurs.
- [cdata](/repos/datagouv/cdata) : Ajout d'icônes personnalisables, gestion des notifications et amélioration de l'accessibilité.
