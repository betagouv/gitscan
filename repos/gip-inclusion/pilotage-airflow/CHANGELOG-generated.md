## Changelog : pilotage-airflow (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration de nouvelles sources de données (FAGERH, RDV-I, Dora, Matomo, IMER) et l'amélioration des modèles de données existants, notamment pour les enquêtes ESAT.  Des optimisations ont également été apportées aux modèles DBT pour faciliter l'analyse et la jointure des données.

### Évolutions fonctionnelles
- Intégration des données de l'enquête FAGERH : ajout de modèles pour l'analyse du taux d'emploi et des réponses, avec gestion des codes départementaux et des bénéficiaires directs. [#7a3ad92](https://github.com/gip-inclusion/pilotage-airflow/commit/7a3ad92) [#3f03ff9](https://github.com/gip-inclusion/pilotage-airflow/commit/3f03ff9) [#e324274](https://github.com/gip-inclusion/pilotage-airflow/commit/e324274) [#46c0ea3](https://github.com/gip-inclusion/pilotage-airflow/commit/46c0ea3)
- Ajout de l'orchestration pour l'IMER (Indicateur de Mesure de l'Équité des Représentations). [#62c8c70](https://github.com/gip-inclusion/pilotage-airflow/commit/62c8c70) [#e61d488](https://github.com/gip-inclusion/pilotage-airflow/commit/e61d488)
- Intégration des données Dora pour les actes métier : ajout de DAG et de modèles DBT. [#c534002](https://github.com/gip-inclusion/pilotage-airflow/commit/c534002)
- Intégration des données Matomo pour les actes métier : ajout de DAG et de modèles DBT. [#43ecc6b](https://github.com/gip-inclusion/pilotage-airflow/commit/43ecc6b)
- Intégration des données RDV-I pour les actes métier : ajout de modèles DBT et d'une étape de construction dans le DAG. [#7ed7c92](https://github.com/gip-inclusion/pilotage-airflow/commit/7ed7c92)
- Amélioration de la gestion des exclusions au niveau des champs dans l'enquête ESAT. [#a3cc427](https://github.com/gip-inclusion/pilotage-airflow/commit/a3cc427)
- Ajout du numéro de département dans les données. [#c79c42a](https://github.com/gip-inclusion/pilotage-airflow/commit/c79c42a)

### Évolutions techniques
- Refactorisation des modèles de données d'inclusion autour de tables de dimensions pour les structures et les services. [#178c574](https://github.com/gip-inclusion/pilotage-airflow/commit/178c574)
- Refactorisation des modèles DI (Données d'Intégration) et suppression des structures en double. [#d950006](https://github.com/gip-inclusion/pilotage-airflow/commit/d950006)
- Refactorisation des modèles de réponses ESAT pour utiliser les réponses d'enquête mappées pour l'analyse et modification du DAG pour lancer avec un tag. [#f225c7e](https://github.com/gip-inclusion/pilotage-airflow/commit/f225c7e)
- Création d'une macro pour indexer les colonnes dans DBT. [#787785a](https://github.com/gip-inclusion/pilotage-airflow/commit/787785a)
- Amélioration de la documentation des tables RDVI dans les fichiers `_sources.yml` de DBT. [#afb0eb2](https://github.com/gip-inclusion/pilotage-airflow/commit/afb0eb2)
- Suppression des doublons dans les offres/demandes. [#fd5da07](https://github.com/gip-inclusion/pilotage-airflow/commit/fd5da07)

### Autres changements
- Correction de définitions dans la documentation des modèles DBT de l'enquête ESAT. [#7513506](https://github.com/gip-inclusion/pilotage-airflow/commit/7513506)
- Correction d'un test d'inclusion de données obsolètes. [#379f31a](https://github.com/gip-inclusion/pilotage-airflow/commit/379f31a)
- Bump de versions de dépendances (mheap/github-action-required-labels, astral-sh/setup-uv, actions/checkout). (Ignoré car routine)
- Airflow bump [#68cdceb](https://github.com/gip-inclusion/pilotage-airflow/commit/68cdceb)
