## Changelog : dossierfacile-data (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois-ci, le projet a enrichi les données disponibles en intégrant le statut de demande de validation des locataires. Parallèlement, des optimisations de performance et des corrections techniques ont été apportées pour fiabiliser le pipeline de transformation des données.

### Évolutions fonctionnelles
- Ajout de la donnée relative au statut de demande de validation des locataires (`validation_requested`) [#80](https://github.com/MTES-MCT/dossierfacile-data/pull/80).

### Évolutions techniques
- Optimisation des performances de la base de données via l'ajout d'index sur les tables [#74](https://github.com/MTES-MCT/dossierfacile-data/pull/74).
- Correction de la stratégie d'incrémentation des données (incremental strategy) pour assurer la fiabilité des flux [#81](https://github.com/MTES-MCT/dossierfacile-data/pull/81).
- Résolution d'un problème technique lié à l'exécution des commandes dbt [#82](https://github.com/MTES-MCT/dossierfacile-data/pull/82).
