## Changelog : transport-site (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des données IRVE (Infrastructure de Recharge pour Véhicules Électriques). Des corrections ont été apportées pour assurer la validité des coordonnées et la précision des données stockées, ainsi que des améliorations de l'interface de validation.

### Évolutions fonctionnelles
- Ajout d'avertissements dans le validateur IRVE lors de la détection d'inversions de coordonnées. [#5541](https://github.com/etalab/transport-site/issues/5541)
- Mise en place de permaliens pour faciliter l'accès aux validations IRVE. [#5524](https://github.com/etalab/transport-site/issues/5524)

### Évolutions techniques
- Correction de problèmes de coordonnées dans la consolidation des données IRVE. [#5535](https://github.com/etalab/transport-site/issues/5535)
- Utilisation du type de données `float` en base de données pour le champ `puissance_nominale` des données IRVE, améliorant la précision des données. [#5531](https://github.com/etalab/transport-site/issues/5531)
- Suppression de la consolidation "brute" IRVE et renommage de la consolidation transport pour simplifier l'architecture. [#5529](https://github.com/etalab/transport-site/issues/5529)
- Arrêt du job de consolidation brute IRVE, suite à la suppression de la consolidation brute. [#5527](https://github.com/etalab/transport-site/issues/5527)
- Mise à jour de la définition Protobuf. [#5533](https://github.com/etalab/transport-site/issues/5533)
- Stabilisation de tests pour améliorer la fiabilité du projet. [#5538](https://github.com/etalab/transport-site/issues/5538)
