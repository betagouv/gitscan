## Changelog : federation (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de la plateforme. Des mises à jour de dépendances ont été effectuées pour assurer la compatibilité et la sécurité du code. Des améliorations ont été apportées à l'administration, notamment la gestion des rôles et l'ajout d'un indicateur visuel pour l'environnement de production. L'accessibilité a également été améliorée avec l'ajout d'un lien vers la déclaration d'accessibilité.

### Évolutions fonctionnelles
- Ajout d'un label par défaut pour les organisations lors de la création d'un prestataire de service. [#1159](https://github.com/proconnect-gouv/federation/pull/1159)
- Amélioration de l'accessibilité : ajout d'un lien vers la déclaration d'accessibilité et modifications de la structure HTML pour une meilleure compatibilité avec les lecteurs d'écran. [#1142](https://github.com/proconnect-gouv/federation/pull/1142)
- Ajout d'un avertissement pour l'environnement de test dans l'interface d'administration. [#1141](https://github.com/proconnect-gouv/federation/pull/1141)
- Gestion des rôles : suppression des rôles de base de données et ajout de rôles par défaut dans l'administration pour une meilleure gestion des permissions. [#1184](https://github.com/proconnect-gouv/federation/pull/1184), [#1185](https://github.com/proconnect-gouv/federation/pull/1185), [#1161](https://github.com/proconnect-gouv/federation/pull/1161)
- Correction d'un bug où le champ `acr` était assigné même si les `acrs` n'étaient pas reconnus. [#1122](https://github.com/proconnect-gouv/federation/pull/1122)

### Évolutions techniques
- Mise à jour de Node.js en version 24.16 dans l'application d'administration. [#1187](https://github.com/proconnect-gouv/federation/pull/1187), [#1186](https://github.com/proconnect-gouv/federation/pull/1186)
- Amélioration de la gestion des exclusions dans le composant `core-fca-low` pour supporter plusieurs exclusions sur le endpoint `readyz`. [#1154](https://github.com/proconnect-gouv/federation/pull/1154)
- Remplacement de `resolveMx` par une requête DNS-over-HTTPS dans le validateur d'email. [#1159](https://github.com/proconnect-gouv/federation/pull/1159)
- Publication de l'image `core-fca-low-migrator` sur GitHub Container Registry. [#1195](https://github.com/proconnect-gouv/federation/pull/1195)
- Refonte de l'indicateur d'environnement de production dans l'administration (remplacement de `isProduction` par `hasRedBorder`). [#1157](https://github.com/proconnect-gouv/federation/pull/1157)

### Autres changements
- Mises à jour de nombreuses dépendances (FastAPI, Pydantic, Mongoose, Cypress, etc.) pour améliorer la sécurité et la stabilité.
- Corrections de linting dans l'application d'administration.
- Suppression d'un test API santé obsolète.
