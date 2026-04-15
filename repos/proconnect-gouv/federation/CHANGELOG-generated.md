## Changelog : federation (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la supervision de l'application, avec l'ajout de points de santé (healthchecks) pour une meilleure gestion des déploiements et de la disponibilité. Des améliorations ont également été apportées à la journalisation et à la gestion des erreurs, notamment au niveau de l'authentification OIDC et de l'API Entreprise. Enfin, plusieurs mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance du projet.

### Évolutions fonctionnelles
- Ajout d'une bannière de maintenance (#1091).
- Amélioration des messages d'erreur pour les emails et OIDC (#1064).
- Ajout des rôles dans les informations retournées par l'API (#1012).
- Correction d'un problème de tolérance pour le TOTP dans l'interface d'administration (#1011).
- Activation du scope "roles" dans FSA1 (#1017).

### Évolutions techniques
- Implémentation de points de santé (livez/readyz) et configuration du healthcheck Dockerfile (#1111, #1110, #1087).
- Correction de tests ChangeStream Mongoose instables (#1096).
- Autorisation de la connexion Redis sans TLS (#1089).
- Suppression de l'utilisation d'Axios au profit de `fetch` dans certaines parties du code (#1086, #1032, #1018).
- Suppression de la dépendance Axios dans l'administration (#1088).
- Ajout de traces de pile (stack traces) aux exceptions pour faciliter le débogage (#1110).
- Remplacement des cookies par des cookies de session pour une meilleure sécurité (#1042).
- Migration de ESLint vers Prettier pour l'ensemble du projet (#996, #992, #994).
- Refactorisation de l'appel à l'API Entreprise pour une meilleure modularité (#1088).
- Mise à jour de plusieurs dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour des dépendances suivantes :
    - `ts-jest` (#1098, #1102)
    - `@nestjs/common` (#1100, #1073, #1027)
    - `@nestjs/cli` (#1101)
    - `@nestjs/testing` (#1103, #1077)
    - `@nestjs/microservices` (#1104, #1079)
    - `python` (#1105)
    - `uvicorn` (#1106)
    - `pytest` (#1108)
    - `ruff` (#1109, #1085, #1057)
    - `axios` (#1092)
    - `axe-core` (#1076)
    - `docker/login-action` (#1075)
    - `moment-timezone` (#1080)
    - `amqplib` (#1083)
    - `lodash` (#1066, #1061, #1060)
    - `cryptography` (#1036)
    - `handlebars` (#1028, #1000)
    - `jose` (#1023, #997)
    - `motor` (#1008)
    - `openapi-fetch` (#1005)
    - `jest` (#1003)
    - `pytest-cov` (#1007, #1056)
    - `ejs` (#1053, #1000)
    - `otplib` (#1054, #1048, #1047)
    - `jsdom` (#1029, #1020)
    - `cypress` (#1026, #1021, #1043)
- Ajout de logs pour faciliter le débogage des erreurs de découverte et de validation (#1070, #1038, #1039).
- Mise à jour de la configuration pour se rapprocher de l'environnement de production (#1071).
- Correction de tests d'intégration (#1031).
- Mise à jour de la variable d'environnement pour hyyyperbridge (#1071).
- Suppression d'une configuration d'asset serving (#993).
- Mise à jour de la configuration k8s dns dans les fixtures de qualité (#1059).
