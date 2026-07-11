# Synthèse d'activité : datagouv (du 22 mai au 10 juillet 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour majeures d'infrastructures et d'API, ainsi que par des améliorations continues de ses outils et services.  Plusieurs projets ont bénéficié de refontes architecturales importantes, comme `relais` et `api-tabular`, avec l'adoption de nouvelles technologies (Rails 8.1, GoodJob, PNPM) pour améliorer la performance, la sécurité et la maintenabilité. L'accent a également été mis sur la préparation des données pour les années à venir, notamment avec les mises à jour des découpages administratifs et des données cadastrales.  De nouvelles fonctionnalités ont été ajoutées pour supporter des usages spécifiques, comme l'intégration CNOUS dans `relais` et l'API TVA DGFIP dans `apistration`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité CVE dans la librairie Crass dans [hubee](/repos/datagouv/hubee).
- Correction de problèmes de sécurité liés aux liens externes et à la gestion des jetons dans [apistration](/repos/datagouv/apistration).
- Mise à jour de la dépendance `urllib3` pour corriger une vulnérabilité de sécurité dans [hydra](/repos/datagouv/hydra).

## Autres changements notables
- Migration vers PNPM dans [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) pour une meilleure gestion des dépendances.
- Passage à Rails 8.1 et intégration de GoodJob dans [relais](/repos/datagouv/relais) pour une meilleure performance et scalabilité.
- Mise à jour d'Airflow vers la version 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack).
- Refonte de l'API géographique avec une nouvelle version (v2) dans [api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif).
- Migration du code de l'interface en ligne de commande vers `datagouv-cli` dans [datagouv-client](/repos/datagouv/datagouv-client).

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de nouvelles fonctionnalités d'intégration avec CNOUS et de gestion de demandes proactives.
- [hubee](/repos/datagouv/hubee) : Modernisation de l'infrastructure et préparation du portail V2 avec l'intégration de Sentry et la mise à jour de PostgreSQL.
- [hydra](/repos/datagouv/hydra) : Améliorations de la robustesse, corrections de bugs, ajout de fonctionnalités et optimisation des performances.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Ajout de la prise en charge de nouveaux packs PNT et amélioration de la gestion des données.
- [apistration](/repos/datagouv/apistration) : Ajout de l'endpoint TVA DGFIP et refonte de l'interface d'administration des éditeurs.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Création d'un nouveau dépôt pour l'interface en ligne de commande et amélioration de la distribution.
