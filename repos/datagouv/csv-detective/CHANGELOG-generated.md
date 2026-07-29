## Changelog : csv-detective (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations de performance, des corrections de typage et de formatage, ainsi que des ajustements pour une meilleure détection des types de données, notamment pour les numéros SIREN et SIRET. Des tests supplémentaires ont été ajoutés et la compatibilité Python a été étendue à la version 3.14.

### Évolutions fonctionnelles
- Amélioration de la détection des types de données pour les numéros SIREN et SIRET, avec une gestion plus stricte des formats numériques.
- Ajout de tests de performance dans le processus d'intégration continue (CI) [#261](https://github.com/datagouv/csv-detective/pull/261).
- Correction de la gestion du nombre total de lignes et des colonnes catégorielles lors de l'analyse par blocs [#249](https://github.com/datagouv/csv-detective/pull/249).

### Évolutions techniques
- Ajout de tests pour Python 3.14 [#262](https://github.com/datagouv/csv-detective/pull/262).
- Correction de problèmes de typage dans le code [#263](https://github.com/datagouv/csv-detective/pull/263).
- Amélioration du formatage de la documentation (README) [#264](https://github.com/datagouv/csv-detective/pull/264).
- Corrections de format dans la documentation des formats de données [#260](https://github.com/datagouv/csv-detective/pull/260) et [#258](https://github.com/datagouv/csv-detective/pull/258), [#259](https://github.com/datagouv/csv-detective/pull/259).

### Autres changements
- Mise à jour de la version à 0.12.0 [#258](https://github.com/datagouv/csv-detective/pull/258).
- Ajout d'une valeur de test supplémentaire [#260](https://github.com/datagouv/csv-detective/pull/260).
