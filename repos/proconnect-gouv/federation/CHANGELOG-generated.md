## Changelog : federation (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la gestion des utilisateurs et la simplification de l'infrastructure. Des correctifs ont été apportés pour renforcer la sécurité de la plateforme, notamment en supprimant des configurations TLS obsolètes et en améliorant la gestion des certificats. L'interface d'administration a été enrichie avec des fonctionnalités de blocage d'utilisateurs et de gestion des collaborateurs, et des améliorations ont été apportées à la gestion des identités et des fournisseurs d'identité.

### Évolutions fonctionnelles
- Ajout de la possibilité de bloquer des utilisateurs dans l'interface d'administration. [#1254](https://github.com/proconnect-gouv/federation/issues/1254)
- Possibilité de rechercher des utilisateurs de la fédération par adresse e-mail dans l'interface d'administration. [#1307](https://github.com/proconnect-gouv/federation/issues/1307)
- Ajout de la gestion des collaborateurs pour les utilisateurs partenaires. [#1310](https://github.com/proconnect-gouv/federation/issues/1310)
- Amélioration de la gestion des fournisseurs d'identité avec l'ajout d'un indicateur de conformité MFA. [#1335](https://github.com/proconnect-gouv/federation/issues/1335)
- Mise à jour du libellé du champ "Se souvenir de moi" pour plus de clarté. [#1301](https://github.com/proconnect-gouv/federation/issues/1301)

### Évolutions techniques
- Suppression des configurations TLS inutiles et des certificats orphelins pour améliorer la sécurité et simplifier l'infrastructure. [#1283](https://github.com/proconnect-gouv/federation/issues/1283), [#1285](https://github.com/proconnect-gouv/federation/issues/1285), [#1286](https://github.com/proconnect-gouv/federation/issues/1286)
- Refactorisation du service de fournisseur OIDC. [#1288](https://github.com/proconnect-gouv/federation/issues/1288)
- Mise à jour de la version de PostgreSQL en local pour correspondre à la production. [#1291](https://github.com/proconnect-gouv/federation/issues/1291)
- Suppression de l'utilisation de `unsafe-inline` dans la politique de sécurité du contenu (CSP) pour renforcer la sécurité. [#1362](https://github.com/proconnect-gouv/federation/issues/1362)
- Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/issues/1324)
- Suppression du champ `ownerEmail` obsolète. [#1370](https://github.com/proconnect-gouv/federation/issues/1370)
- Suppression de l'autocomplétion sur le champ collaborateur. [#1372](https://github.com/proconnect-gouv/federation/issues/1372)

### Autres changements
- Mise à jour de la documentation du backend. [#1341](https://github.com/proconnect-gouv/federation/issues/1341)
- Nettoyage des fixtures inutiles pour les tests Kubernetes. [#1365](https://github.com/proconnect-gouv/federation/issues/1365)
- Suppression des tags `@k8s` non essentiels. [#1364](https://github.com/proconnect-gouv/federation/issues/1364)
- Correction d'un bug où l'ID client n'était pas pris en compte lors de la récupération d'un client. [#1366](https://github.com/proconnect-gouv/federation/issues/1366)
- Rejet des timestamps non numériques dans l'API pcdbapi avec un code 401. [#1368](https://github.com/proconnect-gouv/federation/issues/1368)
- Rejet des listes de collaborateurs vides dans l'API pcdbapi. [#1367](https://github.com/proconnect-gouv/federation/issues/1367)
- Backfill des propriétaires d'applications en tant que collaborateurs. [#1344](https://github.com/proconnect-gouv/federation/issues/1344)
- Diverses mises à jour de dépendances.
