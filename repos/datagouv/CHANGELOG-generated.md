# Synthèse d'activité : datagouv (du 12 mai au 26 juin 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour importantes de plusieurs de ses services et API.  Une attention particulière a été portée à la modernisation des infrastructures (migration vers Rails 8.1, PNPM, Airflow 3), à l'amélioration de la qualité des données (mise à jour des découpages administratifs, données cadastrales, données météo) et à la préparation de nouvelles fonctionnalités, notamment dans les domaines de l'IA et de l'évaluation des modèles.  Plusieurs dépôts ont bénéficié d'améliorations de la sécurité et de la robustesse, ainsi que d'optimisations de performance. Les projets `relais`, `hydra`, `datagouvfr_data_pipelines` et `api-tabular` ont été particulièrement actifs.

## Sécurité
Plusieurs dépôts ont intégré des améliorations de sécurité :
- Correction d'une vulnérabilité dans `datagouv-mcp` concernant la librairie `urllib3`.
- Renforcement de la sécurité des informations sensibles dans `hubee` avec l'interdiction de références confidentielles dans le dépôt public.
- Correction d'une vulnérabilité dans `datagouv-mcp` en contraignant la version de `urllib3`.

## Autres changements notables
- Migration vers PNPM dans `ouverture.data.gouv.fr` pour une meilleure gestion des dépendances.
- Mise à jour vers Rails 8.1 et intégration de GoodJob dans `relais` pour une meilleure performance et scalabilité.
- Migration vers Airflow 3 dans `data-engineering-stack` pour des améliorations de performance.
- Refonte de l'architecture de `hubee` vers une approche modulaire.
- Introduction d'une nouvelle version de l'API géographique (v2) dans `api-decoupage-administratif`.
- Migration des buckets vers OVH Minio dans `datagouvfr_data_pipelines`.

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et intégration de nouvelles fonctionnalités pour la gestion des données.
- [hydra](/repos/datagouv/hydra) : Amélioration de la robustesse, de la performance et de la gestion des fichiers.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Migration vers OVH Minio et améliorations de l'automatisation des pipelines.
- [api-tabular](/repos/datagouv/api-tabular) : Amélioration de la configuration de l'agrégation des données et corrections de bugs.
- [passemarche](/repos/datagouv/passemarche) : Amélioration de l'expérience utilisateur pour la gestion des lots et des marchés.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte de l'architecture et ajout de nouvelles fonctionnalités pour l'évaluation des modèles d'IA.
