## Changelog : transport-site (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur le module IRVE (Infrastructure de Recharge pour Véhicules Électriques) avec des optimisations de la base de données, l'ajout de permaliens pour la validation et la suppression de processus de consolidation obsolètes. Des efforts ont également été faits pour améliorer la sécurité et la configuration du projet.

### Évolutions fonctionnelles
- Ajout de permaliens pour faciliter la validation des données IRVE. [#5524](https://github.com/etalab/transport-site/issues/5524)
- Amélioration de la récupération du `requestor_ref` via l'API, facilitant l'identification des requêtes. [#5516](https://github.com/etalab/transport-site/issues/5516)
- Renforcement de la validation des adresses e-mail dans le module IRVE avec une expression régulière plus stricte. [#5513](https://github.com/etalab/transport-site/issues/5513)

### Évolutions techniques
- Modification du type de données de la colonne `puissance_nominale` en `float` dans la base de données IRVE pour une meilleure précision. [#5531](https://github.com/etalab/transport-site/issues/5531)
- Suppression du job de consolidation brute IRVE et renommage de la consolidation transport pour simplifier l'architecture. [#5527](https://github.com/etalab/transport-site/issues/5527) et [#5529](https://github.com/etalab/transport-site/issues/5529)
- Refactoring initial pour sortir les lectures de variables d'environnement à la compilation, améliorant la configuration et la sécurité. [#5521](https://github.com/etalab/transport-site/issues/5521)
- Suppression de code inutilisé lié au support expérimental SIRI. [#5523](https://github.com/etalab/transport-site/issues/5523)
- Mise à jour de protobuf. [#5533](https://github.com/etalab/transport-site/issues/5533)

### Autres changements
- Correction de failles de sécurité JavaScript. [#5517](https://github.com/etalab/transport-site/issues/5517)
- Ajout d'un script pour profiler les doublons dans le consolidé dynamique IRVE. [#5526](https://github.com/etalab/transport-site/issues/5526)
- Ajout d'un script CheckStatus pour faciliter le monitoring de l'API. [#5516](https://github.com/etalab/transport-site/issues/5516)
