# Synthèse d'activité : datagouv (du 13 mai 2026 au 17 juillet 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour importantes de plusieurs de ses services clés. On observe une forte concentration sur l'amélioration de l'infrastructure et de la robustesse des outils, avec des migrations vers de nouvelles versions de technologies (Rails 8.1, Airflow 3, Python 3.14, PNPM) et des corrections de vulnérabilités.  Plusieurs projets ont bénéficié de l'ajout de nouvelles fonctionnalités, notamment l'intégration de nouveaux services (CNOUS pour relais, API Albert pour datagouv-ai-evaluation) et l'amélioration des APIs existantes (api-tabular, api-geo). L'accent est également mis sur l'amélioration de l'expérience utilisateur, avec des refontes d'interfaces (hubee, datagouv-cli) et l'ajout de fonctionnalités facilitant l'accès et la manipulation des données (csv-detective, datagouv-mcp).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité CVE dans la gem `crass` dans [hubee](/repos/datagouv/hubee).
- Mise à jour de la dépendance `urllib3` pour corriger une vulnérabilité de sécurité (GHSA-mf9v-mfxr-j63j) dans [hydra](/repos/datagouv/hydra).
- Correction d'une vulnérabilité dans [datagouv-mcp](/repos/datagouv/datagouv-mcp).
- Ajout de la gestion de `force_ssl` et d'une Content Security Policy (CSP) minimale dans [hubee](/repos/datagouv/hubee).

## Autres changements notables
- Migration vers PNPM dans [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) pour une meilleure gestion des dépendances.
- Refonte majeure de l'infrastructure de [relais](/repos/datagouv/relais) avec passage à Rails 8.1 et intégration de GoodJob.
- Mise à jour vers Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack).
- Introduction d'une nouvelle version de l'API géographique (v2) dans [api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif).
- Migration de l'interface en ligne de commande vers `datagouv-cli` dans [datagouv_client](/repos/datagouv/datagouv_client).

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de nouvelles fonctionnalités pour l'intégration avec CNOUS et la gestion des demandes proactives.
- [hydra](/repos/datagouv/hydra) : Améliorations de la robustesse, corrections de bugs et ajout de nouvelles fonctionnalités pour l'évaluation des modèles d'IA.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Refonte de l'interface en ligne de commande et amélioration de l'expérience utilisateur.
- [cdata](/repos/datagouv/cdata) : Ajout de nouvelles pages (HVD, organisations), améliorations des visualisations et corrections de bugs.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Ajout de la prise en charge de nouveaux packs PNT et amélioration de la fiabilité des uploads.
