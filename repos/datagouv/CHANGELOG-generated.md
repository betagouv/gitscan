# Synthèse d'activité : datagouv (du 22 mai 2026 au 17 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation datagouv a été marquée par une forte concentration sur l'amélioration de la qualité des données, la modernisation de l'infrastructure et l'amélioration de l'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour de données (cadastre, découpage administratif, api-meteo), tandis que d'autres ont été refactorisés pour adopter de nouvelles technologies (relais, ouverture.data.gouv.fr, data-engineering-stack, api-tabular) ou pour améliorer leur performance et leur robustesse (roles.data, hubee, cdata). L'accessibilité a également été un point d'attention majeur, notamment pour l'API Apistration.  De nouvelles fonctionnalités ont été ajoutées, en particulier pour l'intégration avec des services externes (relais, apistration) et pour faciliter l'utilisation des APIs (datagouv-cli, api-tabular).

## Sécurité
Plusieurs projets ont intégré des améliorations de sécurité :
- Correction d'une vulnérabilité CVE dans [hubee](/repos/datagouv/hubee).
- Corrections de sécurité concernant le tabnapping et les XSS sur les liens DataPass dans [apistration](/repos/datagouv/apistration).

## Autres changements notables
- Migration vers Rails 8.1 et intégration de GoodJob pour la gestion des tâches asynchrones dans [relais](/repos/datagouv/relais).
- Mise à jour vers Airflow 3 dans [data-engineering-stack](/repos/datagouv/data-engineering-stack).
- Migration du gestionnaire de paquets vers PNPM dans [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr).
- Refonte de l'API géographique et passage à la version v2 dans [api-decoupage-administratif](/repos/datagouv/api-decoupage-administratif).
- Migration de l'interface en ligne de commande vers `datagouv-cli` dans [datagouv_client](/repos/datagouv/datagouv_client).

## Dépôts les plus actifs
- [relais](/repos/datagouv/relais) : Refonte majeure de l'infrastructure et ajout de nouvelles fonctionnalités pour l'intégration avec CNOUS et la gestion de demandes proactives.
- [passemarche](/repos/datagouv/passemarche) : Améliorations de l'interface utilisateur et corrections de bugs pour une meilleure expérience acheteurs/candidats.
- [apistration](/repos/datagouv/apistration) : Améliorations significatives de l'accessibilité, ajout de la gestion des tokens éditeur et corrections de bugs.
- [cdata](/repos/datagouv/cdata) : Ajout de nouvelles pages (HVD, édition des organisations) et améliorations de l'exploration tabulaire des données.
- [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Corrections de bugs et migration du stockage objet vers OVH.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : Refonte du code, amélioration de la documentation et ajout d'une nouvelle couche sémantique pour l'évaluation des modèles d'IA.
