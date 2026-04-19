## Changelog : federation (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'observabilité de la plateforme, notamment en ajoutant des vérifications de santé (healthchecks) et en améliorant la gestion des erreurs et des logs. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du système. Des améliorations ont été apportées à l'authentification et à l'intégration avec des services tiers.

### Évolutions fonctionnelles
- Ajout d'un banner de maintenance. [#1091](https://github.com/proconnect-gouv/federation/issues/1091)
- Amélioration des messages d'erreur pour les emails et OIDC. [#1064](https://github.com/proconnect-gouv/federation/issues/1064)
- Ajout des rôles dans la réponse FSA1. [#1012](https://github.com/proconnect-gouv/federation/issues/1012)
- Mise à jour de la configuration pour se rapprocher de l'environnement de production. [#1071](https://github.com/proconnect-gouv/federation/issues/1071)
- Amélioration de la gestion des erreurs et ajout de logs pour le service d'entreprise API. [#1070](https://github.com/proconnect-gouv/federation/issues/1070) et [#1039](https://github.com/proconnect-gouv/federation/issues/1039)

### Évolutions techniques
- Implémentation d'un pattern ping/pong pour vérifier la disponibilité du broker. [#1117](https://github.com/proconnect-gouv/federation/issues/1117)
- Ajout de vérifications de santé (healthchecks) avec des points de terminaison `/livez` et `/readyz` pour améliorer la surveillance et la résilience. [#1116](https://github.com/proconnect-gouv/federation/issues/1116), [#1111](https://github.com/proconnect-gouv/federation/issues/1111), [#1087](https://github.com/proconnect-gouv/federation/issues/1087)
- Suppression des healthchecks redondants dans le Dockerfile. [#1119](https://github.com/proconnect-gouv/federation/issues/1119) et [#1120](https://github.com/proconnect-gouv/federation/issues/1120)
- Utilisation de `fetch` au lieu de `axios` pour certaines requêtes. [#1063](https://github.com/proconnect-gouv/federation/issues/1063)
- Mise à jour de la librairie `openid-client` en version 6.8.1. [#1013](https://github.com/proconnect-gouv/federation/issues/1013)
- Refactorisation de l'appel à l'API entreprise pour une meilleure modularité. [#1088](https://github.com/proconnect-gouv/federation/issues/1088)
- Correction de tests flaky avec ChangeStream. [#1096](https://github.com/proconnect-gouv/federation/issues/1096)
- Autorisation de la connexion Redis sans TLS. [#1089](https://github.com/proconnect-gouv/federation/issues/1089)

### Autres changements
- Ajout de traces de pile (stack traces) aux exceptions pour faciliter le débogage. [#1111](https://github.com/proconnect-gouv/federation/issues/1111)
- Ajout de logs pour les erreurs de découverte et les erreurs d'accès aux organisations. [#1074](https://github.com/proconnect-gouv/federation/issues/1074) et [#1038](https://github.com/proconnect-gouv/federation/issues/1038)
- Suppression de la dépendance `axios` dans le module admin. [#1088](https://github.com/proconnect-gouv/federation/issues/1088)
- Diverses mises à jour de dépendances (lodash, handlebars, jest, cypress, etc.).
- Configuration de prettier avec la configuration par défaut. [#996](https://github.com/proconnect-gouv/federation/issues/996)
- Ajout de `isEntraId` et `hyyyperbridge` dans Grist. [#1115](https://github.com/proconnect-gouv/federation/issues/1115)
- Ajout d'un check de readiness pour le CSM. [#1114](https://github.com/proconnect-gouv/federation/issues/1114)
- Ajout d'un check de readiness pour hyyyperbridge. [#1110](https://github.com/proconnect-gouv/federation/issues/1110)
