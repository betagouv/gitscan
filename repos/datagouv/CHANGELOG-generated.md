# Synthèse d'activité : datagouv (du 22 mai au 20 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation datagouv a été marquée par une forte concentration sur l'amélioration de l'infrastructure, la sécurité et la qualité des données. Plusieurs projets ont bénéficié de mises à jour majeures, comme la migration vers Rails 8.1 pour [relais](/repos/datagouv/relais) et l'adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).  Des efforts importants ont également été consacrés à l'intégration de nouvelles données (ODM, DVF, qualité de l'eau) et à l'amélioration de l'accessibilité des données via des API plus performantes et sécurisées (apistration, api-tabular). L'accent mis sur la documentation et les tests unitaires témoigne d'une volonté d'améliorer la maintenabilité et la fiabilité des projets.

## Sécurité
Plusieurs dépôts ont intégré des améliorations de sécurité :
- Anonymisation des adresses email dans les logs Sentry dans [roles.data](/repos/datagouv/roles.data).
- Correction d'une vulnérabilité dans `urllib3` dans [datagouv-mcp](/repos/datagouv/datagouv-mcp).
- Renforcement de la sécurité des sessions utilisateurs dans [apistration](/repos/datagouv/apistration).

## Autres changements notables
- Migration vers Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack).
- Refonte de l'architecture de [relais](/repos/datagouv/relais) avec l'intégration de GoodJob pour la gestion des tâches asynchrones.
- Nouvelle version de l'API géographique (v2) dans [api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif).
- Refonte de l'API [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) avec l'ajout d'une couche sémantique et l'amélioration des tests.

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de nouvelles fonctionnalités d'intégration avec CNOUS et de gestion des demandes proactives.
- [hydra](/repos/datagouv/hydra) : Amélioration de l'exportation des données et intégration avec le stockage S3.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Ajout de nouveaux jeux de données et optimisation de la consommation de mémoire.
- [apistration](/repos/datagouv/apistration) : Amélioration de la sécurité, intégration de FranceConnect et ajout de la gestion des délégations d'éditeurs.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte de l'architecture et amélioration de la documentation pour faciliter l'évaluation des modèles d'IA.
