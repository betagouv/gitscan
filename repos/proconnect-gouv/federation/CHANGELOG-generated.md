## Changelog : federation (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, de la gestion des utilisateurs et de la stabilité de la plateforme. Des correctifs ont été apportés pour renforcer la sécurité, notamment en supprimant des configurations SSL obsolètes et en améliorant la gestion des politiques de sécurité du contenu. Des fonctionnalités de gestion des collaborateurs pour les clients OIDC et les utilisateurs partenaires ont été ajoutées, ainsi que des améliorations de l'expérience utilisateur, comme la mise à jour des libellés et la correction de bugs.

### Évolutions fonctionnelles
- Ajout de la gestion des collaborateurs pour les clients OIDC [#1310](https://github.com/proconnect-gouv/federation/issues/1310).
- Ajout de la gestion des collaborateurs pour les utilisateurs partenaires [#1310](https://github.com/proconnect-gouv/federation/issues/1310).
- Possibilité de rechercher des utilisateurs fédérés par email dans l'interface d'administration [#1307](https://github.com/proconnect-gouv/federation/issues/1307).
- Mise à jour du libellé de la case à cocher "Se souvenir de moi" pour une meilleure clarté [#1301](https://github.com/proconnect-gouv/federation/issues/1301).
- Activation des tests MFA avec des alias d'email "+mfa" [#1348](https://github.com/proconnect-gouv/federation/issues/1348).
- Ajout d'indicateurs de santé (livez/readyz) pour l'application d'administration [#1391](https://github.com/proconnect-gouv/federation/issues/1391).

### Évolutions techniques
- Mise à jour de PostgreSQL en version 18 dans l'environnement Docker Compose [#1296](https://github.com/proconnect-gouv/federation/issues/1296).
- Refactorisation pour supprimer un champ d'email propriétaire obsolète [#1370](https://github.com/proconnect-gouv/federation/issues/1370).
- Amélioration des performances des requêtes MongoDB en utilisant une correspondance de chaîne exacte [#1369](https://github.com/proconnect-gouv/federation/issues/1369).
- Suppression de la configuration SSL MongoDB non sécurisée [#1323](https://github.com/proconnect-gouv/federation/issues/1323).
- Ajout de la bibliothèque `@fc/mailer` avec des adaptateurs SMTP/Brevo/noop [#1343](https://github.com/proconnect-gouv/federation/issues/1343).
- Suppression de l'autocomplétion sur le champ des collaborateurs [#1372](https://github.com/proconnect-gouv/federation/issues/1372).
- Mise en place d'une politique de sécurité du contenu (CSP) plus stricte en supprimant `unsafe-inline` [#1362](https://github.com/proconnect-gouv/federation/issues/1362).
- Extraction du script de confirmation de déconnexion vers un fichier externe [#1410](https://github.com/proconnect-gouv/federation/issues/1410).

### Autres changements
- Mise à jour de la documentation du backend [#1341](https://github.com/proconnect-gouv/federation/issues/1341).
- Suppression du widget de chat Crisp [#1324](https://github.com/proconnect-gouv/federation/issues/1324).
- Amélioration du formatage du code avec Prettier [#1389](https://github.com/proconnect-gouv/federation/issues/1389) et [#1309](https://github.com/proconnect-gouv/federation/issues/1309).
- Nettoyage des fixtures et des tests Kubernetes inutiles [#1365](https://github.com/proconnect-gouv/federation/issues/1365) et [#1364](https://github.com/proconnect-gouv/federation/issues/1364).
- Diverses mises à jour de dépendances.
