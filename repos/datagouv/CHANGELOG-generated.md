# Synthèse d'activité : datagouv (du 13 mai 2026 au 02 juillet 2026)

## Résumé de l'activité
L'organisation datagouv a connu une période d'activité soutenue, marquée par des mises à jour importantes de plusieurs de ses produits phares. On observe une forte concentration sur l'amélioration de l'infrastructure et de la qualité du code, avec des migrations vers de nouvelles versions de librairies et des refactorings architecturaux majeurs (notamment sur `relais`, `hubee` et `api-tabular`). Des efforts significatifs ont également été déployés pour améliorer la gestion des données géographiques et administratives, avec des mises à jour des données de découpage administratif et des corrections pour assurer la cohérence des informations. Enfin, plusieurs dépôts ont bénéficié d'améliorations de l'expérience utilisateur, comme l'ajout de nouvelles fonctionnalités de recherche et de filtrage sur `passemarche` et `cdata`.

## Sécurité
Des corrections de vulnérabilités ont été apportées à `apistration` pour corriger des failles liées au tabnapping et au XSS sur les liens DataPass. De plus, `datagouv-mcp` a bénéficié d'une mise à jour de la librairie `urllib3` pour corriger une vulnérabilité de sécurité.

## Autres changements notables
- Migration vers Rails 8.1 et intégration de GoodJob pour la gestion des tâches asynchrones dans `relais`.
- Refonte architecturale majeure de `hubee` vers un modèle modulaire.
- Migration de `api-tabular` vers une configuration plus flexible de l'agrégation des données.
- Passage à Airflow 3 dans `data-engineering-stack`.
- Nouvelle version (v2) de l'API géographique dans `api-decoupage-administratif`.
- Migration de `datagouv-cli` pour une distribution autonome et des builds multi-plateformes.

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et de l'architecture, avec intégration de CNOUS et gestion des demandes proactives.
- [passemarche](/repos/datagouv/passemarche) : Amélioration significative de la gestion des lots et de l'expérience utilisateur.
- [cdata](/repos/datagouv/cdata) : Nombreuses corrections de bugs, améliorations de l'interface et optimisations de performance.
- [hydra](/repos/datagouv/hydra) : Amélioration de la robustesse, corrections de bugs et intégration de nouvelles fonctionnalités.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Migration vers OVH, gestion des données géographiques et corrections de bugs.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : Migration du code CLI et amélioration du processus de construction.
