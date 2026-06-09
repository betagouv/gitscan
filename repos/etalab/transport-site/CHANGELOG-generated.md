## Changelog : transport-site (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des données IRVE, notamment la déduplication et la validation des informations. Des optimisations ont également été apportées à l'infrastructure et au code, avec la suppression de fonctionnalités obsolètes et la correction de problèmes de sécurité.

### Évolutions fonctionnelles

- **IRVE :** Ajout d'un permalien pour la validation IRVE, facilitant le partage et la vérification des informations. [#5524](https://github.com/etalab/transport-site/issues/5524)
- **API :** Simplification de la récupération de la référence du demandeur (`requestor_ref`) via l'API, et ajout d'un script `CheckStatus` pour le suivi. [#5516](https://github.com/etalab/transport-site/issues/5516)
- **Données :** Intégration des données GBFS de Yégo dans les métadonnées disponibles. [#5512](https://github.com/etalab/transport-site/issues/5512)
- **Interface utilisateur :** Correction de l'affichage des icônes après une mise à jour. [#5506](https://github.com/etalab/transport-site/issues/5506)

### Évolutions techniques

- **IRVE :** Suppression de la consolidation "brute" IRVE et renommage de la consolidation transport pour une meilleure clarté. [#5529](https://github.com/etalab/transport-site/issues/5529)
- **IRVE :** Arrêt du job de consolidation brute IRVE, optimisant ainsi les ressources. [#5527](https://github.com/etalab/transport-site/issues/5527)
- **Sécurité :** Application de correctifs de sécurité pour JavaScript afin de réduire les vulnérabilités. [#5517](https://github.com/etalab/transport-site/issues/5517)
- **Configuration :** Début de la migration des variables d'environnement vers la compilation, améliorant la sécurité et la performance. [#5521](https://github.com/etalab/transport-site/issues/5521)
- **Code :** Suppression du code inutilisé lié au support expérimental SIRI. [#5523](https://github.com/etalab/transport-site/issues/5523)
- **Code :** Suppression de code mort concernant l'ancien agrégateur dynamique IRVE du proxy unlock. [#5510](https://github.com/etalab/transport-site/issues/5510)

### Autres changements

- **IRVE :** Amélioration de la regex pour la validation des adresses email IRVE, rendant la validation plus stricte. [#5513](https://github.com/etalab/transport-site/issues/5513)
- **IRVE :** Ajout d'un script de profiling pour identifier les doublons dans le consolidé dynamique IRVE. [#5526](https://github.com/etalab/transport-site/issues/5526)
