## Changelog : transport-site (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la consolidation et la gestion des données IRVE (Infrastructure de Recharge pour Véhicules Électriques). Des corrections ont été apportées pour améliorer la précision des coordonnées et la gestion des données de puissance nominale. Des optimisations ont également été réalisées pour simplifier le processus de consolidation et supprimer du code obsolète.

### Évolutions fonctionnelles
- Amélioration de la précision des coordonnées dans la consolidation IRVE. [#5535](https://github.com/etalab/transport-site/issues/5535)
- Ajout d'un permalien pour faciliter la validation IRVE. [#5524](https://github.com/etalab/transport-site/issues/5524)

### Évolutions techniques
- Utilisation de `float` en base de données pour stocker la valeur `puissance_nominale` des bornes IRVE, améliorant ainsi la précision des données. [#5531](https://github.com/etalab/transport-site/issues/5531)
- Suppression de la consolidation "brute" IRVE et renommage de la consolidation transport pour simplifier l'architecture. [#5529](https://github.com/etalab/transport-site/issues/5529)
- Arrêt du job de consolidation brute IRVE, réduisant la charge de travail et simplifiant la maintenance. [#5527](https://github.com/etalab/transport-site/issues/5527)
- Début d'un refactoring pour sortir les lectures de variables d'environnement à la compilation, améliorant la performance et la sécurité. [#5521](https://github.com/etalab/transport-site/issues/5521)
- Suppression du code obsolète lié au support expérimental pour SIRI, allégeant le code base. [#5523](https://github.com/etalab/transport-site/issues/5523)
- Mise à jour de protobuf. [#5533](https://github.com/etalab/transport-site/issues/5533)

### Autres changements
- Stabilisation des tests. [#5538](https://github.com/etalab/transport-site/issues/5538)
- Ajout d'un script de profiling pour identifier les doublons dans le consolidé dynamique IRVE. [#5526](https://github.com/etalab/transport-site/issues/5526)
