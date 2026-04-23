## Changelog : federation (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'observabilité de la plateforme, notamment en ajoutant des points de contrôle de santé (healthchecks) et en améliorant la journalisation. Des corrections ont également été apportées pour résoudre des problèmes de configuration et de tests. Enfin, des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance du système.

### Évolutions fonctionnelles
- Amélioration des messages d'erreur et des informations affichées pour l'authentification OIDC [#1064](https://github.com/proconnect-gouv/federation/issues/1064).
- Ajout d'une bannière de maintenance pour informer les utilisateurs [#1091](https://github.com/proconnect-gouv/federation/issues/1091).
- Remplacement des cookies par des cookies de session pour une sécurité accrue [#1042](https://github.com/proconnect-gouv/federation/issues/1042).
- Ajout des champs `isEntraId` et `hyyyperbridge` à Grist pour une meilleure traçabilité [#1115](https://github.com/proconnect-gouv/federation/issues/1115).

### Évolutions techniques
- Implémentation d'un pattern ping/pong pour les contrôles de santé du broker, améliorant la détection des problèmes de connectivité [#1117](https://github.com/proconnect-gouv/federation/issues/1117).
- Ajout de points de contrôle de santé (livez et readyz) pour les différentes images Docker, permettant une meilleure surveillance de l'état des services [#1111](https://github.com/proconnect-gouv/federation/issues/1111), [#1087](https://github.com/proconnect-gouv/federation/issues/1087).
- Utilisation de `fetch` au lieu de `axios` dans certaines parties du code pour simplifier les requêtes HTTP [#1018](https://github.com/proconnect-gouv/federation/issues/1018).
- Extraction de la configuration de l'API Entreprise dans un provider dédié pour une meilleure modularité [#1016](https://github.com/proconnect-gouv/federation/issues/1016).
- Correction de tests d'intégration instables liés à Mongoose [#1096](https://github.com/proconnect-gouv/federation/issues/1096).
- Suppression des tests d'API health [#1120](https://github.com/proconnect-gouv/federation/issues/1120) et des healthchecks du Dockerfile [#1119](https://github.com/proconnect-gouv/federation/issues/1119).
- Possibilité de désactiver le proxy Axios pour le service CSM RIE [#1125](https://github.com/proconnect-gouv/federation/issues/1125).
- Correction pour autoriser les connexions Redis sans TLS [#1089](https://github.com/proconnect-gouv/federation/issues/1089).
- Ajout de traces de pile (stack traces) aux exceptions pour faciliter le débogage [#1118](https://github.com/proconnect-gouv/federation/issues/1118).

### Autres changements
- Mise à jour de plusieurs dépendances (lodash, handlebars, jsdom, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration de la journalisation pour les erreurs de découverte et les problèmes liés aux rôles.
- Suppression de l'utilisation d'Axios dans l'admin.
- Mise à jour de la configuration pour se rapprocher de l'environnement de production.
- Correction de problèmes de tests d'intégration.
- Mise à jour de la configuration k8s DNS dans les fixtures de qualité.
- Suppression de eslint et mise à jour des commandes de lint.
