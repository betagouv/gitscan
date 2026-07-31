## Changelog : federation (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la simplification de l'architecture et la préparation du projet pour de futures évolutions. Plusieurs microservices ont été isolés en applications autonomes, et des améliorations ont été apportées à la gestion des erreurs et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un indicateur de conformité MFA (Authentification Multi-Facteur) pour les fournisseurs d'identité. [#1335](https://github.com/proconnect-gouv/federation/pull/1335)
- Possibilité de tester le MFA avec des alias d'email "+mfa". [#1348](https://github.com/proconnect-gouv/federation/pull/1348)
- Ajout d'un point de terminaison pour supprimer un client OIDC par son ID. [#1390](https://github.com/proconnect-gouv/federation/pull/1390)
- Amélioration de la formulation des emails de vérification. [#1425](https://github.com/proconnect-gouv/federation/pull/1425)
- Implémentation d'un fallback par email pour le MFA lorsque le fournisseur d'identité ne le supporte pas. [#1372](https://github.com/proconnect-gouv/federation/pull/1372)

### Évolutions techniques
- Refactorisation importante : plusieurs services (csmr-rie, mock-service-provider-fca-low, mock-identity-provider-fca-low, mock-data-provider) ont été extraits en applications autonomes. [#1428](https://github.com/proconnect-gouv/federation/pull/1428), [#1424](https://github.com/proconnect-gouv/federation/pull/1424), [#1416](https://github.com/proconnect-gouv/federation/pull/1416), [#1413](https://github.com/proconnect-gouv/federation/pull/1413)
- Suppression du service pcdbapi. [#1427](https://github.com/proconnect-gouv/federation/pull/1427)
- Migration de la gestion des erreurs vers les filtres d'exception NestJS pour une meilleure centralisation et maintenabilité. [#1438](https://github.com/proconnect-gouv/federation/pull/1438), [#38ecea7](https://github.com/proconnect-gouv/federation/commit/38ecea7)
- Amélioration de la résilience du template EJS utilisé pour les emails. [#1434](https://github.com/proconnect-gouv/federation/pull/1434)
- Ajout de healthchecks livez/readyz à l'application admin. [#1391](https://github.com/proconnect-gouv/federation/pull/1391)
- Suppression de la configuration SSL MongoDB obsolète. (révertée)
- Amélioration des performances des requêtes MongoDB en utilisant des correspondances de chaînes exactes. [#1369](https://github.com/proconnect-gouv/federation/pull/1369)
- Ajout de la librairie @fc/mailer avec des adaptateurs SMTP/Brevo/noop. [#1343](https://github.com/proconnect-gouv/federation/pull/1343)

### Autres changements
- Mise à jour de la documentation du back-end. [#1392](https://github.com/proconnect-gouv/federation/pull/1392)
- Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/pull/1324)
- Suppression d'un test Kubernetes obsolète. [#1337](https://github.com/proconnect-gouv/federation/pull/1337)
- Nettoyage du code et suppression de fonctions inutilisées. [#7dda7e9](https://github.com/proconnect-gouv/federation/commit/7dda7e9)
- Diverses mises à jour de dépendances.
- Extraction du script de confirmation de déconnexion dans un fichier externe. [#1410](https://github.com/proconnect-gouv/federation/pull/1410)
- Correction d'un bug dans la migration `isMfaCompliant`. [#1411](https://github.com/proconnect-gouv/federation/pull/1411)
- Correction d'un bug où l'ID du client n'était pas pris en compte lors de la récupération par ID. [#1366](https://github.com/proconnect-gouv/federation/pull/1366)
- Ajout de gardes pour empêcher les requêtes ACR non conformes. [#1340](https://github.com/proconnect-gouv/federation/pull/1340)
- Suppression de l'autocomplétion sur le champ collaborateur. [#1370](https://github.com/proconnect-gouv/federation/pull/1370)
- Correction d'un bug empêchant l'ajout de collaborateurs existants. [#1367](https://github.com/proconnect-gouv/federation/pull/1367)
