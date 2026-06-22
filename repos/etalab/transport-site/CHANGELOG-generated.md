## Changelog : transport-site (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la consolidation et la gestion des données IRVE (Infrastructure de Recharge pour Véhicules Électriques). Des corrections ont été apportées aux coordonnées, des optimisations de stockage ont été réalisées et des outils de profiling ont été ajoutés pour améliorer la qualité des données. Des efforts de maintenance ont également été effectués pour simplifier le code et arrêter des processus inutilisés.

### Évolutions fonctionnelles
- Correction des coordonnées dans la consolidation IRVE, améliorant la précision géographique des données.  [#5535](https://github.com/etalab/transport-site/issues/5535)
- Ajout d'un permalien pour faciliter la validation des données IRVE. [#5524](https://github.com/etalab/transport-site/issues/5524)

### Évolutions techniques
- Utilisation de `float` en base de données pour le champ `puissance_nominale` des bornes IRVE, permettant une meilleure précision des valeurs. [#5531](https://github.com/etalab/transport-site/issues/5531)
- Suppression de la consolidation "brute" IRVE et renommage de la consolidation transport pour simplifier l'architecture. [#5529](https://github.com/etalab/transport-site/issues/5529)
- Arrêt du job de consolidation brute IRVE, réduisant la charge de travail et les ressources utilisées. [#5527](https://github.com/etalab/transport-site/issues/5527)
- Début d'un refactoring pour sortir les lectures d'environnement à la compilation, améliorant la performance et la sécurité. [#5521](https://github.com/etalab/transport-site/issues/5521)
- Mise à jour de protobuf. [#5533](https://github.com/etalab/transport-site/issues/5533)

### Autres changements
- Suppression du code inutilisé lié au support expérimental pour SIRI, allégeant le code base. [#5523](https://github.com/etalab/transport-site/issues/5523)
- Ajout d'un script de profiling pour identifier et corriger les doublons dans le consolidé dynamique IRVE. [#5526](https://github.com/etalab/transport-site/issues/5526)
