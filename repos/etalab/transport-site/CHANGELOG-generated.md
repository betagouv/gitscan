## Changelog : transport-site (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la maintenance technique du site, l'amélioration de la sécurité et la préparation de futures évolutions. Des corrections ont été apportées à l'affichage des icônes et des mises à jour de dépendances JavaScript ont été réalisées. Des travaux ont également été menés sur l'infrastructure et la configuration pour optimiser le site et préparer la sortie de certaines fonctionnalités expérimentales.

### Évolutions fonctionnelles
- Ajout de la prise en charge des données GBFS de Yégo dans les métadonnées. [#5512](https://github.com/etalab/transport-site/issues/5512)
- Correction de l'affichage des icônes. [#5505](https://github.com/etalab/transport-site/issues/5505) [#5506](https://github.com/etalab/transport-site/issues/5506)
- Amélioration de la récupération du `requestor_ref` via l'API, facilitant l'identification des requêtes. [#5516](https://github.com/etalab/transport-site/issues/5516)

### Évolutions techniques
- Mise à jour de FontAwesome de la version 6 à la version 7 pour bénéficier des dernières icônes et améliorations. [#5500](https://github.com/etalab/transport-site/issues/5500)
- Mise à jour de plusieurs dépendances JavaScript (DeckGL, Vega, etc.). [#5499](https://github.com/etalab/transport-site/issues/5499)
- Migration du système de gestion des styles SCSS de `@import` vers `@use` pour une meilleure organisation et performance. [#5502](https://github.com/etalab/transport-site/issues/5502)
- Patchs de sécurité appliqués aux dépendances JavaScript. [#5517](https://github.com/etalab/transport-site/issues/5517)
- Début d'une refactorisation pour sortir les variables d'environnement à la compilation. [#5521](https://github.com/etalab/transport-site/issues/5521)
- Suppression du code obsolète lié au support expérimental SIRI. [#5523](https://github.com/etalab/transport-site/issues/5523)
- Suppression du code mort de l'ancien agrégateur dynamique IRVE du proxy unlock. [#5510](https://github.com/etalab/transport-site/issues/5510)

### Autres changements
- Arrêt du job de consolidation brute. [#5527](https://github.com/etalab/transport-site/issues/5527)
- Amélioration de la regex de validation des adresses email pour l'IRVE. [#5513](https://github.com/etalab/transport-site/issues/5513)
- Ajout d'un script de profiling pour identifier les doublons dans le consolidé dynamique IRVE. [#5526](https://github.com/etalab/transport-site/issues/5526)
- Correction d'un warning dans le CI. [#5504](https://github.com/etalab/transport-site/issues/5504)
