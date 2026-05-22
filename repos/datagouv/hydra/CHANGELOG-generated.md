## Changelog : hydra (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation de l'export de données, notamment en permettant la génération de GeoJSON et Parquet directement à partir de la base de données, évitant ainsi de relire les fichiers CSV.  Une refactorisation du code de conversion a également été effectuée pour une meilleure organisation.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des données au format GeoJSON directement depuis la base de données, lors du pipeline CSV. [#423](https://github.com/datagouv/hydra/pull/423)
- Ajout de la possibilité d'exporter des données au format Parquet directement depuis la base de données. [#424](https://github.com/datagouv/hydra/pull/424)
- Amélioration de la génération de GeoJSON à partir de PostgreSQL, en évitant la relecture des fichiers CSV. [#404](https://github.com/datagouv/hydra/pull/404)

### Évolutions techniques
- Refactorisation du code de conversion des données, avec séparation des méthodes de conversion dans des fichiers dédiés dans le répertoire `/conversion`. [#422](https://github.com/datagouv/hydra/pull/422)
- Suppression d'une protection obsolète dans la conversion CSV vers GeoJSON.
- Alignement de la disposition des tests avec le package de conversion. [#427](https://github.com/datagouv/hydra/pull/427)
- Suppression du `__all__` redondant dans l'analyse CSV. [#426](https://github.com/datagouv/hydra/pull/426)

### Autres changements
- Correction d'une erreur mineure dans la docstring de la fonction `enqueue`.
- Publication de la version 2.10.1.
- Publication de la version 2.10.0.
- Publication de la version 2.9.0.
