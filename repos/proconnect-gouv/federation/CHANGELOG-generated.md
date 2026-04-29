## Changelog : federation (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'observabilité de la plateforme. Des améliorations ont été apportées aux healthchecks, à la gestion des erreurs et à la journalisation pour faciliter le diagnostic et la résolution des problèmes. Des corrections ont également été apportées pour assurer la compatibilité et la stabilité des différents composants.

### Évolutions fonctionnelles
- Ajout d'un indicateur de validation d'email configurable via un flag de fonctionnalité. [#1144](https://github.com/proconnect-gouv/federation/pull/1144)
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés pour faciliter le débogage, notamment concernant les appels à l'API Entreprise et les erreurs OIDC. [#1038](https://github.com/proconnect-gouv/federation/pull/1038), [#1040](https://github.com/proconnect-gouv/federation/pull/1040), [#1041](https://github.com/proconnect-gouv/federation/pull/1041), [#1063](https://github.com/proconnect-gouv/federation/pull/1063), [#1070](https://github.com/proconnect-gouv/federation/pull/1070), [#1074](https://github.com/proconnect-gouv/federation/pull/1074)
- Amélioration des messages d'erreur et des logs pour les erreurs OIDC et les emails. [#1064](https://github.com/proconnect-gouv/federation/pull/1064)
- Ajout d'une bannière de maintenance. [#1091](https://github.com/proconnect-gouv/federation/pull/1091)
- Remplacement des cookies par des session cookies pour une meilleure sécurité. [#1042](https://github.com/proconnect-gouv/federation/pull/1042)

### Évolutions techniques
- Implémentation d'un pattern ping/pong pour les healthchecks du broker, améliorant la détection des problèmes de connectivité. [#1117](https://github.com/proconnect-gouv/federation/pull/1117)
- Ajout de routes `livez` et `readyz` pour les healthchecks, et configuration du `HEALTHCHECK` dans les Dockerfiles. [#1087](https://github.com/proconnect-gouv/federation/pull/1087), [#1110](https://github.com/proconnect-gouv/federation/pull/1110), [#1111](https://github.com/proconnect-gouv/federation/pull/1111), [#1114](https://github.com/proconnect-gouv/federation/pull/1114)
- Utilisation de `https` pour récupérer le core-fca. [#1118](https://github.com/proconnect-gouv/federation/pull/1118)
- Suppression des healthchecks redondants dans les Dockerfiles. [#1119](https://github.com/proconnect-gouv/federation/pull/1119), [#1120](https://github.com/proconnect-gouv/federation/pull/1120)
- Refactorisation de l'appel à l'API Entreprise pour une meilleure modularité et testabilité. [#1032](https://github.com/proconnect-gouv/federation/pull/1032)
- Correction d'un problème de flaky tests ChangeStream avec Mongoose. [#1096](https://github.com/proconnect-gouv/federation/pull/1096)
- Utilisation de `fetch` au lieu de `axios` pour certains appels réseau. [#1018](https://github.com/proconnect-gouv/federation/pull/1018)
- Suppression de l'utilisation d'axios dans l'admin. [#1088](https://github.com/proconnect-gouv/federation/pull/1088)
- Autorisation de la connexion Redis sans TLS. [#1089](https://github.com/proconnect-gouv/federation/pull/1089)

### Autres changements
- Mise à jour de diverses dépendances (lodash, otplib, jsdom, etc.).
- Amélioration de la configuration pour se rapprocher de l'environnement de production. [#1071](https://github.com/proconnect-gouv/federation/pull/1071)
- Ajout d'informations `isEntraId` et `hyyyperbridge` à Grist pour faciliter le suivi. [#1115](https://github.com/proconnect-gouv/federation/pull/1115)
- Suppression de l'API health test. [#1120](https://github.com/proconnect-gouv/federation/pull/1120)
- Correction de la regression dans `getToken`. [#1041](https://github.com/proconnect-gouv/federation/pull/1041)
