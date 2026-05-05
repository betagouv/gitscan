## Changelog : federation (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'observabilité de la plateforme, notamment en ajoutant des vérifications de santé (healthchecks) et en améliorant la journalisation. Des corrections ont également été apportées pour améliorer la compatibilité et la gestion des erreurs, ainsi que des améliorations de la qualité du code et des dépendances.

### Évolutions fonctionnelles
- Amélioration des messages d'erreur pour les emails et OIDC, rendant les diagnostics plus clairs pour les utilisateurs et administrateurs. [#1064](https://github.com/proconnect-gouv/federation/pull/1064)
- Ajout d'un indicateur de maintenance visible dans l'interface. [#1091](https://github.com/proconnect-gouv/federation/pull/1091)
- Possibilité de désactiver la validation d'email via un flag de configuration. [#1144](https://github.com/proconnect-gouv/federation/pull/1144)
- Ajout des champs `isEntraId` et `hyyyperbridge` dans Grist pour une meilleure visibilité des données. [#1115](https://github.com/proconnect-gouv/federation/pull/1115)

### Évolutions techniques
- Implémentation d'un système de healthchecks basé sur un pattern ping/pong pour vérifier la disponibilité du broker. [#1117](https://github.com/proconnect-gouv/federation/pull/1117)
- Ajout de healthchecks spécifiques pour les composants CSM et Hyyyperbridge. [#1114](https://github.com/proconnect-gouv/federation/pull/1110)
- Configuration des images Docker pour utiliser `/livez` comme healthcheck par défaut. [#1087](https://github.com/proconnect-gouv/federation/pull/1087)
- Correction d'un problème de flaky tests ChangeStream avec Mongoose. [#1096](https://github.com/proconnect-gouv/federation/pull/1096)
- Utilisation de HTTPS pour récupérer le core-fca. [#1118](https://github.com/proconnect-gouv/federation/pull/1118)
- Suppression du proxy Axios pour CSM, permettant à l'environnement Node.js de gérer la connexion. [#1125](https://github.com/proconnect-gouv/federation/pull/1125)
- Amélioration de la gestion des erreurs et ajout de logs pour les problèmes de rôles. [#1074](https://github.com/proconnect-gouv/federation/pull/1074)
- Suppression des tests de santé API obsolètes. [#1120](https://github.com/proconnect-gouv/federation/pull/1120) et suppression des healthchecks de Dockerfile [#1119](https://github.com/proconnect-gouv/federation/pull/1119)

### Autres changements
- Mise à jour de plusieurs dépendances (axios, docker-login-action, etc.).
- Amélioration de la journalisation pour les valeurs `acr_values`. [#1139](https://github.com/proconnect-gouv/federation/pull/1139)
- Correction de la configuration de TypeScript pour assurer l'utilisation de la version interne dans VSCode. [#1086](https://github.com/proconnect-gouv/federation/pull/1086)
- Suppression de la dépendance Axios dans le module admin. [#1088](https://github.com/proconnect-gouv/federation/pull/1088)
- Autorisation de la connexion Redis sans TLS. [#1089](https://github.com/proconnect-gouv/federation/pull/1089)
