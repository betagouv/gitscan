## Changelog : federation (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la surveillance de la plateforme, notamment en ajoutant des vérifications de santé (healthchecks) et en améliorant la gestion des rôles utilisateurs. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité du système. L'accessibilité a été améliorée avec l'ajout d'une déclaration d'accessibilité.

### Évolutions fonctionnelles
- Ajout d'une bannière d'environnement de test pour informer les utilisateurs qu'ils se trouvent sur un environnement non productif. [#1141](https://github.com/proconnect-gouv/federation/pull/1141)
- Amélioration de l'accessibilité : ajout d'un lien vers la déclaration d'accessibilité et modifications de la structure HTML pour une meilleure compatibilité avec les lecteurs d'écran. [#1142](https://github.com/proconnect-gouv/federation/pull/1142)
- Ajout de la possibilité de définir des rôles par défaut dans l'interface d'administration. [#1158](https://github.com/proconnect-gouv/federation/pull/1158)
- Implémentation d'un mécanisme de validation d'email configurable via un flag de fonctionnalité. [#1144](https://github.com/proconnect-gouv/federation/pull/1144)
- Ajout d'informations `isEntraId` et `hyyyperbridge` à Grist pour faciliter le débogage et le suivi. [#1115](https://github.com/proconnect-gouv/federation/pull/1115)

### Évolutions techniques
- Ajout de vérifications de santé (healthchecks) pour différents composants : broker, CSM, Hyyyperbridge, et amélioration de la configuration des healthchecks dans Dockerfile. [#1116](https://github.com/proconnect-gouv/federation/pull/1116), [#1117](https://github.com/proconnect-gouv/federation/pull/1117), [#1118](https://github.com/proconnect-gouv/federation/pull/1118), [#1119](https://github.com/proconnect-gouv/federation/pull/1119), [#1120](https://github.com/proconnect-gouv/federation/pull/1120), [#1121](https://github.com/proconnect-gouv/federation/pull/1121)
- Correction d'un problème de flaky tests dans ChangeStream avec Mongoose. [#1096](https://github.com/proconnect-gouv/federation/pull/1096)
- Mise à jour de la configuration pour utiliser HTTPS lors de la récupération du core-fca. [#1118](https://github.com/proconnect-gouv/federation/pull/1118)
- Amélioration de la gestion des exclusions multiples dans la configuration du core-fca low support. [#1154](https://github.com/proconnect-gouv/federation/pull/1154)
- Correction d'un bug où le champ `acr` était incorrectement assigné si les `acrs` n'étaient pas reconnus. [#1122](https://github.com/proconnect-gouv/federation/pull/1122)
- Remplacement de `resolveMx` par une requête DNS-over-HTTPS pour une meilleure sécurité et performance de la validation d'email. [#1159](https://github.com/proconnect-gouv/federation/pull/1159)
- Renommage de `isProduction` en `hasRedBorder` pour plus de clarté. [#1157](https://github.com/proconnect-gouv/federation/pull/1157)

### Autres changements
- Ajout de logs pour les valeurs `acr` pour faciliter le débogage. [#1139](https://github.com/proconnect-gouv/federation/pull/1139)
- Mises à jour de diverses dépendances (Mongoose, axios, fastapi, pydantic, etc.). Ces mises à jour sont principalement des correctifs de sécurité et de performance.
- Amélioration de la configuration CI/CD et des workflows de test.
