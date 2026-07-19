## Changelog : csv-detective (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à la détection de formats de données, notamment pour les numéros SIREN et SIRET, et corrige des erreurs liées à la détection de nombres entiers. Des corrections de documentation et des ajustements pour le CI/CD complètent cette version.

### Évolutions fonctionnelles
- Possibilité de passer des valeurs NaN supplémentaires pour une meilleure détection des données manquantes [#255](https://github.com/datagouv/csv-detective/pull/255).
- Amélioration de la détection des formats numériques, notamment pour les numéros SIREN et SIRET, avec des tests supplémentaires pour garantir la précision.
- Correction d'un bug empêchant la détection correcte des valeurs uniques dans les colonnes complexes [#257](https://github.com/datagouv/csv-detective/pull/257).

### Évolutions techniques
- Ajout de tests pour Python 3.14 [#262](https://github.com/datagouv/csv-detective/pull/262).
- Corrections de format dans la documentation.
- Correction des tags.
- Utilisation d'un token pour la publication sur PyPI [#256](https://github.com/datagouv/csv-detective/pull/256).

### Autres changements
- Mise à jour de la version à 0.12.0.
- Amélioration de la robustesse de la détection des entiers.
- Ajout de valeurs de test pour améliorer la couverture.
