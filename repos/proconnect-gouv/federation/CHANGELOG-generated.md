## Changelog : federation (30 derniers jours, au 2026-04-16)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'observabilité de la plateforme, notamment en ajoutant des vérifications de santé (healthchecks) et en affinant la gestion des erreurs et des logs. Des améliorations ont également été apportées à la sécurité, avec le remplacement des cookies par des sessions, et à l'intégration avec des services tiers comme Hyyyperbridge. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et fonctionnalités.

### Évolutions fonctionnelles
- Ajout d'une bannière de maintenance. [#1091](https://github.com/proconnect-gouv/federation/issues/1091)
- Amélioration des messages d'erreur pour les emails et OIDC, rendant les informations plus claires pour les utilisateurs. [#1064](https://github.com/proconnect-gouv/federation/issues/1064)
- Ajout des rôles dans les informations renvoyées par l'API. [#1012](https://github.com/proconnect-gouv/federation/issues/1012)
- Tolérance accrue pour les codes TOTP dans l'interface d'administration. [#1011](https://github.com/proconnect-gouv/federation/issues/1011)
- Mise à jour de la configuration pour se rapprocher de l'environnement de production. [#1071](https://github.com/proconnect-gouv/federation/issues/1071)

### Évolutions techniques
- Implémentation de vérifications de santé (healthchecks) pour différents composants (CSMR, Hyyyperbridge) avec des points de contrôle personnalisés. [#1114](https://github.com/proconnect-gouv/federation/issues/1114), [#1116](https://github.com/proconnect-gouv/federation/issues/1116), [#1110](https://github.com/proconnect-gouv/federation/issues/1110)
- Remplacement de l'utilisation d'Axios par `fetch` pour certaines requêtes, améliorant potentiellement la performance et réduisant les dépendances. [#1068](https://github.com/proconnect-gouv/federation/issues/1068)
- Refactorisation du code pour extraire la logique d'appel à l'API Entreprise dans un provider dédié. [#1088](https://github.com/proconnect-gouv/federation/issues/1088)
- Correction de tests ChangeStream MongoDB qui étaient instables. [#1096](https://github.com/proconnect-gouv/federation/issues/1096)
- Amélioration de la gestion des erreurs et ajout de traces de pile pour faciliter le débogage. [#1111](https://github.com/proconnect-gouv/federation/issues/1111), [#1062](https://github.com/proconnect-gouv/federation/issues/1062)
- Remplacement des cookies par des sessions pour une meilleure sécurité. [#1042](https://github.com/proconnect-gouv/federation/issues/1042)
- Mise à jour de la librairie openid-client en version 6.8.1. [#1013](https://github.com/proconnect-gouv/federation/issues/1013)
- Ajout de logs plus détaillés pour faciliter le diagnostic des problèmes liés à la découverte des services et aux erreurs d'authentification. [#1070](https://github.com/proconnect-gouv/federation/issues/1070), [#1038](https://github.com/proconnect-gouv/federation/issues/1038)

### Autres changements
- Ajout de `isEntraId` et `hyyyperbridge` aux métadonnées Grist. [#1115](https://github.com/proconnect-gouv/federation/issues/1115)
- Configuration pour autoriser les connexions Redis sans TLS. [#1089](https://github.com/proconnect-gouv/federation/issues/1089)
- Suppression de la dépendance Axios dans le module d'administration. [#1088](https://github.com/proconnect-gouv/federation/issues/1088)
- Mise à jour de la configuration Kubernetes pour les tests d'intégration. [#1063](https://github.com/proconnect-gouv/federation/issues/1063)
- Plusieurs mises à jour de dépendances (lodash, handlebars, jsdom, otplib, etc.) pour corriger des bugs et améliorer la sécurité. (Ces mises à jour sont listées dans les commits mais ne sont pas détaillées individuellement ici).
