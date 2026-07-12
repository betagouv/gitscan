## Changelog : federation (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la simplification de l'infrastructure et l'ajout de nouvelles fonctionnalités pour la gestion des utilisateurs et des collaborateurs. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de gérer les collaborateurs pour les clients OIDC [#1312](https://github.com/proconnect-gouv/federation/issues/1312).
- Ajout d'un indicateur de conformité MFA (Multi-Factor Authentication) pour les fournisseurs d'identité [#1335](https://github.com/proconnect-gouv/federation/issues/1335).
- Possibilité de rechercher des utilisateurs fédérés par email dans l'interface d'administration [#1307](https://github.com/proconnect-gouv/federation/issues/1307).
- Ajout de la gestion des collaborateurs pour les utilisateurs partenaires [#1310](https://github.com/proconnect-gouv/federation/issues/1310).
- Mise à jour du libellé du champ "Se souvenir de moi" pour plus de clarté [#1301](https://github.com/proconnect-gouv/federation/issues/1301).
- Mise à jour du libellé du champ email sur la page d'édition du SP [#1244](https://github.com/proconnect-gouv/federation/issues/1244).

### Évolutions techniques
- Suppression de la configuration SSL MongoDB obsolète [#1323](https://github.com/proconnect-gouv/federation/issues/1323).
- Suppression de PM2 des images de production pour simplifier le déploiement [#1244](https://github.com/proconnect-gouv/federation/issues/1244).
- Ajout du support Sentinel pour la configuration Redis [#1265](https://github.com/proconnect-gouv/federation/issues/1265).
- Amélioration de la configuration TLS pour MongoDB, rendue configurable via une variable d'environnement [#1266](https://github.com/proconnect-gouv/federation/issues/1266).
- Mise à jour de la version de PostgreSQL en local et en production [#1287](https://github.com/proconnect-gouv/federation/issues/1287) et [#1296](https://github.com/proconnect-gouv/federation/issues/1296).
- Suppression de la configuration TLS inutile pour PostgreSQL et promotion de pg-admin dans la configuration partagée [#1287](https://github.com/proconnect-gouv/federation/issues/1287).
- Suppression des certificats TLS orphelins dans les volumes Docker [#1286](https://github.com/proconnect-gouv/federation/issues/1286).
- Ajout d'un healthcheck `readyz` au service core dans Docker [#1261](https://github.com/proconnect-gouv/federation/issues/1261).
- Refactorisation du service de provider OIDC [#1288](https://github.com/proconnect-gouv/federation/issues/1288).
- Suppression du widget de chat Crisp [#1324](https://github.com/proconnect-gouv/federation/issues/1324).
- Suppression des fixtures Kubernetes inutiles pour les tests Cypress [#1365](https://github.com/proconnect-gouv/federation/issues/1365) et [#1364](https://github.com/proconnect-gouv/federation/issues/1364).

### Autres changements
- Correction d'un bug où l'ID client n'était pas pris en compte lors de la récupération par ID [#1366](https://github.com/proconnect-gouv/federation/issues/1366).
- Correction d'un problème où les timestamps non numériques étaient acceptés par l'API PCDB [#1368](https://github.com/proconnect-gouv/federation/issues/1368).
- Correction d'un problème où une liste de collaborateurs vide était acceptée par l'API PCDB [#1367](https://github.com/proconnect-gouv/federation/issues/1367).
- Amélioration de la lisibilité du diagramme cinématique dans la documentation [#01a73fc](https://github.com/proconnect-gouv/federation/commit/01a73fc).
- Suppression d'une configuration de test Kubernetes obsolète [#1337](https://github.com/proconnect-gouv/federation/issues/1337).
- Backfill des propriétaires d'applications en tant que collaborateurs [#1344](https://github.com/proconnect-gouv/federation/issues/1344).
- Mise à jour de la documentation backend [#1341](https://github.com/proconnect-gouv/federation/issues/1341).
- Ajout de règles d'ignorance pour les mises à jour de dépendances PostgreSQL.
- Correction de la migration pour ajouter une valeur par défaut à `isMfaCompliant` [#1363](https://github.com/proconnect-gouv/federation/issues/1363).
- Sécurisation de la politique de sécurité du contenu (CSP) en supprimant `unsafe-inline` [#1362](https://github.com/proconnect-gouv/federation/issues/1362).
- De nombreuses mises à jour de dépendances ont été effectuées (voir les commits individuels).
