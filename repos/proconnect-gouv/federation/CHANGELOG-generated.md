## Changelog : federation (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la classification des services publics, la gestion des rôles et des permissions, ainsi que des corrections et optimisations techniques pour une meilleure stabilité et sécurité. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance du projet.

### Évolutions fonctionnelles
- Mise à jour de la classification des services publics pour correspondre à la définition légale la plus récente. [#1215](https://github.com/proconnect-gouv/federation/issues/1215)
- Ajout de l'organisation label par défaut lors de la création d'un prestataire de services. [#1181](https://github.com/proconnect-gouv/federation/issues/1181)
- Ajout de rôles par défaut dans l'application d'administration pour une gestion simplifiée des permissions. [#1161](https://github.com/proconnect-gouv/federation/issues/1161)
- Amélioration de l'accessibilité de l'application, notamment en ajoutant un lien vers la déclaration d'accessibilité et en améliorant la structure des titres. [#1142](https://github.com/proconnect-gouv/federation/issues/1142)
- Correction d'un bug empêchant l'assignation du champ `acr` lorsque les `acrs` ne sont pas reconnus. [#1122](https://github.com/proconnect-gouv/federation/issues/1122)
- Ajout d'une exception si aucun `acr` correspondant aux attentes n'est trouvé.

### Évolutions techniques
- Suppression de la configuration `healthcheck_live` de la configuration de construction Docker pour simplifier le processus de build. [#1194](https://github.com/proconnect-gouv/federation/issues/1194)
- Suppression de l'application `BridgeHttpProxyRie` pour rationaliser l'architecture. [#1198](https://github.com/proconnect-gouv/federation/issues/1198)
- Publication de l'image `core-fca-low-migrator` sur GHCR pour faciliter le déploiement. [#1195](https://github.com/proconnect-gouv/federation/issues/1195)
- Remplacement de `resolveMx` par une requête DNS-over-HTTPS `fetch` dans le validateur d'email.
- Mise à jour des packages ProConnect Identité. [#1214](https://github.com/proconnect-gouv/federation/issues/1214)
- Passage à Node 24.16 dans l'application d'administration. [#1186](https://github.com/proconnect-gouv/federation/issues/1186)
- Suppression des rôles de base de données dans l'administration.
- Ajout de la possibilité de supporter plusieurs exclusions sur `readyz` pour `core-fca-low`.
- Amélioration de la gestion de la bordure rouge en production dans l'administration.

### Autres changements
- Ajout de logs lors de la détection d'une discrepancy entre l'ancienne et la nouvelle computation du service public. [#1199](https://github.com/proconnect-gouv/federation/issues/1199)
- Ajout de scopes, roles et organization_label par défaut dans l'API PCDb. [#1200](https://github.com/proconnect-gouv/federation/issues/1200)
- Correction de lint dans admin app.ts pour HAS_RED_BORDER.
- Renommage de `isProduction` en `hasRedBorder`.
- De nombreuses mises à jour de dépendances ont été appliquées pour améliorer la sécurité et la stabilité du projet. (Ces mises à jour de routine ne sont pas listées individuellement).
