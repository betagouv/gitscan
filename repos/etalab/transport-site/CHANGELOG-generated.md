## Changelog : transport-site (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la consolidation et la gestion des données IRVE (Infrastructure de Recharge pour Véhicules Électriques). Des corrections de coordonnées, des optimisations de stockage en base de données et des améliorations du processus de validation ont été apportées. Des efforts de maintenance ont également été réalisés pour simplifier le code et arrêter des processus inutiles.

### Évolutions fonctionnelles
- Correction des coordonnées dans la consolidation IRVE, améliorant la précision des données géographiques. [#5535](https://github.com/etalab/transport-site/issues/5535)
- Ajout d'un permalien pour faciliter la validation des données IRVE. [#5524](https://github.com/etalab/transport-site/issues/5524)
- Script de profiling des doublons sur le consolidé dynamique IRVE pour identifier et potentiellement résoudre les problèmes de données dupliquées. [#5526](https://github.com/etalab/transport-site/issues/5526)

### Évolutions techniques
- Utilisation de `float` en base de données pour le champ `puissance_nominale` des données IRVE, optimisant le stockage et la précision des valeurs. [#5531](https://github.com/etalab/transport-site/issues/5531)
- Mise à jour des définitions de Protobuf. [#5533](https://github.com/etalab/transport-site/issues/5533)
- Suppression de la consolidation "brute" IRVE et renommage de la consolidation transport pour simplifier l'architecture. [#5529](https://github.com/etalab/transport-site/issues/5529)
- Arrêt du job de consolidation brute IRVE, réduisant la charge de travail du système. [#5527](https://github.com/etalab/transport-site/issues/5527)
- Début de la migration des lectures de variables d'environnement vers la compilation, améliorant la sécurité et la performance. [#5521](https://github.com/etalab/transport-site/issues/5521)
- Suppression du code obsolète lié au support expérimental pour SIRI, allégeant le code base. [#5523](https://github.com/etalab/transport-site/issues/5523)
