## Changelog : federation (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, de la stabilité et de la maintenabilité du projet. Des correctifs ont été apportés pour renforcer la sécurité, notamment en supprimant des configurations potentiellement dangereuses et en améliorant la gestion des certificats TLS. Des mises à jour de dépendances ont été effectuées pour bénéficier des dernières corrections et améliorations de sécurité. Des améliorations ont également été apportées à la gestion des collaborateurs et à l'interface d'administration.

### Évolutions fonctionnelles

*   Ajout de la possibilité de gérer les collaborateurs pour les clients OIDC. [#1299](https://github.com/proconnect-gouv/federation/issues/1299)
*   Ajout d'un indicateur de conformité MFA (Multi-Factor Authentication) pour les fournisseurs d'identité. [#1335](https://github.com/proconnect-gouv/federation/issues/1335)
*   Possibilité de rechercher des utilisateurs fédérés par email dans l'interface d'administration. [#1307](https://github.com/proconnect-gouv/federation/issues/1307)
*   Amélioration de la gestion des collaborateurs pour les utilisateurs partenaires. [#1310](https://github.com/proconnect-gouv/federation/issues/1310)
*   Correction d'un bug où l'ID client n'était pas correctement récupéré. [#1366](https://github.com/proconnect-gouv/federation/issues/1366)
*   Correction d'un problème où la validation des timestamps non numériques était incorrecte. [#1368](https://github.com/proconnect-gouv/federation/issues/1368)
*   Correction d'un problème où une liste vide de collaborateurs était acceptée. [#1367](https://github.com/proconnect-gouv/federation/issues/1367)
*   Correction du label du checkbox "Se souvenir de moi". [#1301](https://github.com/proconnect-gouv/federation/issues/1301)

### Évolutions techniques

*   Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité. [#1362](https://github.com/proconnect-gouv/federation/issues/1362)
*   Suppression de l'utilisation de PM2 dans les images de production. [#1244](https://github.com/proconnect-gouv/federation/issues/1244)
*   Suppression de la configuration TLS obsolète de MongoDB. [#1323](https://github.com/proconnect-gouv/federation/issues/1323) (annulé puis rétabli)
*   Mise à jour de la version de PostgreSQL dans les conteneurs Docker. [#1217](https://github.com/proconnect-gouv/federation/issues/1217) et [#1311](https://github.com/proconnect-gouv/federation/issues/1311)
*   Ajout de healthchecks `readyz` pour le service core. [#1261](https://github.com/proconnect-gouv/federation/issues/1261)
*   Refactorisation de la gestion des providers OIDC. [#1288](https://github.com/proconnect-gouv/federation/issues/1288)
*   Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/issues/1324)
*   Correction d'un bug dans la migration pour ajouter une valeur par défaut à `isMfaCompliant`. [#1363](https://github.com/proconnect-gouv/federation/issues/1363)
*   Backfill des propriétaires d'applications en tant que collaborateurs. [#1344](https://github.com/proconnect-gouv/federation/issues/1344)

### Autres changements

*   Mise à jour de la documentation du backend. [#1341](https://github.com/proconnect-gouv/federation/issues/1341) et [#1364](https://github.com/proconnect-gouv/federation/issues/1364)
*   Amélioration de la lisibilité du diagramme cinématique dans la documentation du backend. [#1301](https://github.com/proconnect-gouv/federation/issues/1301)
*   Nettoyage des fixtures Kubernetes inutiles. [#1365](https://github.com/proconnect-gouv/federation/issues/1365)
*   Suppression des tags `@k8s` non essentiels. [#1364](https://github.com/proconnect-gouv/federation/issues/1364)
*   Plusieurs mises à jour de dépendances (prettier, fastapi, mongodb, etc.).
*   Correction de la configuration de l'environnement pour Redis et MongoDB.
*   Correction d'un test Kubernetes obsolète. [#1337](https://github.com/proconnect-gouv/federation/issues/1337)
