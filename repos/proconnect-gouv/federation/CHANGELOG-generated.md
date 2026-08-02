## Changelog : federation (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la refactorisation de l'architecture pour une meilleure maintenabilité et la préparation du terrain pour de nouvelles fonctionnalités, notamment l'authentification multi-facteurs (MFA). Plusieurs microservices ont été extraits en applications autonomes pour simplifier le développement et le déploiement.

### Évolutions fonctionnelles
- Ajout d'un point de terminaison pour supprimer les clients OIDC via l'API. [#1390](https://github.com/proconnect-gouv/federation/issues/1390)
- Possibilité de tester l'authentification multi-facteurs (MFA) avec des alias d'e-mail "+mfa". [#1348](https://github.com/proconnect-gouv/federation/issues/1348)
- Implémentation d'un fallback par e-mail pour la MFA pour les fournisseurs d'identité non compatibles. [#1362](https://github.com/proconnect-gouv/federation/issues/1362)
- Ajout d'un indicateur de conformité MFA pour les fournisseurs d'identité. [#1335](https://github.com/proconnect-gouv/federation/issues/1335)
- Amélioration de la gestion des erreurs lors de la vérification de l'e-mail. [#1438](https://github.com/proconnect-gouv/federation/issues/1438)
- Possibilité de configurer un préfixe pour l'objet des e-mails. [#1437](https://github.com/proconnect-gouv/federation/issues/1437)

### Évolutions techniques
- Refactorisation de l'architecture : extraction de plusieurs microservices (mock-data-provider, mock-identity-provider, mock-service-provider, csmr-rie) en applications autonomes. [#1428](https://github.com/proconnect-gouv/federation/issues/1428), [#1424](https://github.com/proconnect-gouv/federation/issues/1424), [#1416](https://github.com/proconnect-gouv/federation/issues/1416), [#1413](https://github.com/proconnect-gouv/federation/issues/1413)
- Suppression du service pcdbapi. [#1427](https://github.com/proconnect-gouv/federation/issues/1427)
- Migration de la gestion des erreurs vers les filtres d'exception NestJS. [#1436](https://github.com/proconnect-gouv/federation/issues/1436)
- Refactorisation pour imposer un seul jeton de vérification d'e-mail par utilisateur. [#1446](https://github.com/proconnect-gouv/federation/issues/1446)
- Amélioration de la performance des requêtes MongoDB en utilisant des correspondances de chaînes exactes. [#1369](https://github.com/proconnect-gouv/federation/issues/1369)
- Ajout de healthchecks livez/readyz à l'application admin. [#1391](https://github.com/proconnect-gouv/federation/issues/1391)
- Mise en place d'une bibliothèque de gestion des e-mails (@fc/mailer) avec des adaptateurs SMTP/Brevo/noop. [#1343](https://github.com/proconnect-gouv/federation/issues/1343)
- Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/issues/1324)

### Autres changements
- Mise à jour de la documentation. [#1392](https://github.com/proconnect-gouv/federation/issues/1392), [#1411](https://github.com/proconnect-gouv/federation/issues/1411)
- Amélioration de la description du README. [#1448](https://github.com/proconnect-gouv/federation/issues/1448)
- Nettoyage du code et suppression de code obsolète.
- Diverses mises à jour de dépendances.
- Correction d'un bug dans la migration pour ajouter la valeur par défaut à isMfaCompliant. [#1446](https://github.com/proconnect-gouv/federation/issues/1446)
- Correction d'un bug où l'ID du client n'était pas pris en compte lors de la récupération par ID. [#1366](https://github.com/proconnect-gouv/federation/issues/1366)
- Suppression de l'autocomplétion sur le champ des collaborateurs. [#1370](https://github.com/proconnect-gouv/federation/issues/1370)
- Backfill des propriétaires d'applications en tant que collaborateurs. [#1344](https://github.com/proconnect-gouv/federation/issues/1344)
- Amélioration de la résilience du template EJS. [#1434](https://github.com/proconnect-gouv/federation/issues/1434)
- Correction d'un problème de sécurité lié à Content Security Policy. [#1362](https://github.com/proconnect-gouv/federation/issues/1362)
