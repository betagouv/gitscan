## Changelog : federation (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des rôles et des autorisations, notamment dans l'API PCDb et l'interface d'administration. Des corrections et des améliorations de la sécurité ont également été apportées. De nombreuses mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de scopes, rôles et labels d'organisation par défaut dans l'API PCDb [#1200](https://github.com/proconnect-gouv/federation/issues/1200).
- Ajout d'un label d'organisation lors de la création d'un prestataire de service [#1188](https://github.com/proconnect-gouv/federation/issues/1188).
- Amélioration de l'accessibilité avec l'ajout d'un lien vers la déclaration d'accessibilité et des ajustements de balises HTML [#1142](https://github.com/proconnect-gouv/federation/issues/1142).
- Ajout de rôles par défaut dans l'interface d'administration [#1161](https://github.com/proconnect-gouv/federation/issues/1161).
- Mise à jour de l'utilisation du flag de fonctionnalité de validation d'email [#1160](https://github.com/proconnect-gouv/federation/issues/1160).
- Correction d'un bug empêchant l'assignation du champ ACR si les ACRs ne sont pas reconnus [#1158](https://github.com/proconnect-gouv/federation/issues/1158).

### Évolutions techniques
- Suppression de l'application BridgeHttpProxyRie [#1198](https://github.com/proconnect-gouv/federation/issues/1198).
- Publication de l'image core-fca-low-migrator sur GHCR [#1195](https://github.com/proconnect-gouv/federation/issues/1195).
- Remplacement de `resolveMx` par une requête DNS-over-HTTPS `fetch` dans le validateur d'email [#1159](https://github.com/proconnect-gouv/federation/issues/1159).
- Suppression des rôles de base de données dans l'administration [#1185](https://github.com/proconnect-gouv/federation/issues/1185).
- Utilisation de `fetch` au lieu de `axios` dans le projet hybride RIE (deuxième tentative) [#1069](https://github.com/proconnect-gouv/federation/issues/1069).
- Mise à jour vers Node 24.16 dans l'administration [#1187](https://github.com/proconnect-gouv/federation/issues/1187) et [#1186](https://github.com/proconnect-gouv/federation/issues/1186).
- Amélioration de la gestion des exclusions multiples sur la route readyz pour core-fca-low [#1154](https://github.com/proconnect-gouv/federation/issues/1154).
- Ajout d'un avertissement pour l'environnement de test [#1141](https://github.com/proconnect-gouv/federation/issues/1141).

### Autres changements
- Ajout d'un log en cas de divergence entre l'ancien et le nouveau calcul du service public [#1199](https://github.com/proconnect-gouv/federation/issues/1199).
- Mise à jour des dépendances (FastAPI, Uvicorn, Jose, ioredis, NestJS, Cypress, Prettier, Docker, etc.).
- Correction de lint dans admin app.ts pour HAS_RED_BORDER.
- Renommage de `isProduction` en `hasRedBorder`.
- Suppression du test API health [#1120](https://github.com/proconnect-gouv/federation/issues/1120) (puis rétabli).
