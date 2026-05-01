## Changelog : csv-detective (30 derniers jours, au 2026-04-29)

### Résumé
Les récentes mises à jour de csv-detective se concentrent sur l'amélioration de la robustesse et de la performance, notamment en optimisant la détection des types de données dans les colonnes, en particulier pour les colonnes vides et les formats de date. Des corrections de bugs ont également été apportées pour garantir une analyse plus précise des fichiers CSV.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la validation de se terminer correctement en cas de crash lors du chargement des données par blocs. [#1f9788f](https://github.com/datagouv/csv-detective/commit/1f9788f)
- Correction d'un bug sur les colonnes vides qui empêchait l'analyse correcte des données. [#998be02](https://github.com/datagouv/csv-detective/commit/998be02)
- Amélioration de la détection des dates au format RFC 822. [#e624e48](https://github.com/datagouv/csv-detective/commit/e624e48)
- Optimisation de la détection en ne testant que les valeurs uniques dans les colonnes. [#e4c67c0](https://github.com/datagouv/csv-detective/commit/e4c67c0)
- Amélioration de la performance en utilisant des itérateurs dans les fonctions `any` et `all`. [#6e49268](https://github.com/datagouv/csv-detective/commit/6e49268)
- Les tests ne sont plus exécutés sur les colonnes vides. [#02240fa](https://github.com/datagouv/csv-detective/commit/02240fa)
- Les tests sont ignorés pour les colonnes d'étiquettes obligatoires. [#0df0057](https://github.com/datagouv/csv-detective/commit/0df0057)

### Évolutions techniques
- Mise à jour de la version minimale de Python supportée (documentée). [#7855f7e](https://github.com/datagouv/csv-detective/commit/7855f7e)
- Ajout d'un test pour vérifier que tous les formats ont des étiquettes. [#231](https://github.com/etalab/csv-detective/pull/231) (via CHANGELOG.md)
- Amélioration de la détection de l'encodage. [#218](https://github.com/etalab/csv-detective/pull/218) (via CHANGELOG.md)
- Mise à jour de la librairie `frformat`. [#234](https://github.com/etalab/csv-detective/pull/234) (via CHANGELOG.md)
- Mise à jour de la librairie `pandas` vers la version 3.0. [#236](https://github.com/etalab/csv-detective/pull/236) (via CHANGELOG.md)

### Autres changements
- Corrections de linting et ajout de tests. [#fb220a9](https://github.com/datagouv/csv-detective/commit/fb220a9), [#7298276](https://github.com/datagouv/csv-detective/commit/7298276)
