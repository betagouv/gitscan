## Changelog : federation (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la correction de bugs et la maintenance technique du projet. Des améliorations ont été apportées à la gestion des collaborateurs, à la configuration de la sécurité et à la robustesse de l'infrastructure. Plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Possibilité de rechercher des utilisateurs fédérés par email dans l'interface d'administration. [#1307](https://github.com/proconnect-gouv/federation/issues/1307)
- Ajout de la gestion des collaborateurs pour les clients OIDC. [#1312](https://github.com/proconnect-gouv/federation/issues/1312)
- Amélioration de la gestion des collaborateurs : suppression de l'autocomplétion sur le champ collaborateur pour éviter les erreurs. [#1372](https://github.com/proconnect-gouv/federation/issues/1372)
- Ajout d'un indicateur de conformité MFA (Multi-Factor Authentication) pour les fournisseurs d'identité. [#1335](https://github.com/proconnect-gouv/federation/issues/1335)
- Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/issues/1324)

### Évolutions techniques
- Renforcement de la sécurité : suppression de `unsafe-inline` de la Content Security Policy pour réduire les risques d'attaques XSS. [#1362](https://github.com/proconnect-gouv/federation/issues/1362)
- Amélioration de la configuration : possibilité de configurer TLS pour MongoDB via une variable d'environnement. [#1266](https://github.com/proconnect-gouv/federation/issues/1266)
- Mise à jour de la version de PostgreSQL en local pour correspondre à la version de production. [#1217](https://github.com/proconnect-gouv/federation/issues/1217)
- Ajout de healthchecks pour le broker. [#1262](https://github.com/proconnect-gouv/federation/issues/1262)
- Suppression de code obsolète : suppression du champ `ownerEmail` obsolète. [#1370](https://github.com/proconnect-gouv/federation/issues/1370)
- Suppression de configurations TLS inutiles. [#1323](https://github.com/proconnect-gouv/federation/issues/1323)
- Refactorisation du service de provider OIDC. [#1288](https://github.com/proconnect-gouv/federation/issues/1288)
- Nettoyage des fixtures et tests Kubernetes. [#1364](https://github.com/proconnect-gouv/federation/issues/1364), [#1365](https://github.com/proconnect-gouv/federation/issues/1365)

### Autres changements
- Mise à jour de nombreuses dépendances (Node.js, TypeScript, Docker, PostgreSQL, MongoDB, Redis, etc.) pour bénéficier des dernières corrections et améliorations.
- Correction de la migration pour ajouter une valeur par défaut au champ `isMfaCompliant`. [#1363](https://github.com/proconnect-gouv/federation/issues/1363)
- Amélioration de la documentation. [#1301](https://github.com/proconnect-gouv/federation/issues/1301)
- Correction de bugs dans l'API PCDB : gestion des timestamps non numériques et des listes de collaborateurs vides. [#1368](https://github.com/proconnect-gouv/federation/issues/1368), [#1367](https://github.com/proconnect-gouv/federation/issues/1367)
- Correction d'un bug dans l'API PCDB : récupération correcte du client par ID. [#1366](https://github.com/proconnect-gouv/federation/issues/1366)
- Backfill des propriétaires d'applications en tant que collaborateurs. [#1344](https://github.com/proconnect-gouv/federation/issues/1344)
- Mise à jour des labels de l'interface d'authentification. [#1243](https://github.com/proconnect-gouv/federation/issues/1243)
