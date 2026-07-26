## Changelog : federation (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, de la gestion des utilisateurs et de la stabilité de la plateforme. Des correctifs ont été apportés pour renforcer la conformité MFA, améliorer la gestion des clients OIDC et résoudre des problèmes liés à la configuration de la base de données. Des mises à jour de dépendances ont également été effectuées pour maintenir la plateforme à jour.

### Évolutions fonctionnelles
- Ajout de la possibilité de rechercher des utilisateurs fédérés par email dans l'interface d'administration. [#1307](https://github.com/proconnect-gouv/federation/issues/1307)
- Activation des tests MFA avec des alias d'email "+mfa". [#1348](https://github.com/proconnect-gouv/federation/issues/1348)
- Ajout d'un endpoint pour supprimer un client OIDC par son ID. [#1390](https://github.com/proconnect-gouv/federation/issues/1390)
- Ajout d'une bibliothèque de mailing (@fc/mailer) avec des adaptateurs SMTP/Brevo/noop. [#1343](https://github.com/proconnect-gouv/federation/issues/1343)
- Ajout d'un indicateur de conformité MFA pour les fournisseurs d'identité (IdP). [#1335](https://github.com/proconnect-gouv/federation/issues/1335)
- Gestion des collaborateurs pour les clients OIDC. [#1312](https://github.com/proconnect-gouv/federation/issues/1312)

### Évolutions techniques
- Mise en place de healthchecks livez/readyz pour l'application admin. [#1391](https://github.com/proconnect-gouv/federation/issues/1391)
- Refactorisation pour supprimer le champ "owner email" obsolète. [#1370](https://github.com/proconnect-gouv/federation/issues/1370)
- Amélioration des performances des requêtes MongoDB en utilisant une correspondance de chaînes de caractères exacte. [#1369](https://github.com/proconnect-gouv/federation/issues/1369)
- Suppression de la configuration SSL MongoDB non sécurisée. [#1323](https://github.com/proconnect-gouv/federation/issues/1323)
- Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/issues/1324)
- Mise à jour de la version de PostgreSQL en local pour correspondre à la production. [#1311](https://github.com/proconnect-gouv/federation/issues/1311)
- Application du formatage Prettier sur l'ensemble du projet. [#1389](https://github.com/proconnect-gouv/federation/issues/1389)
- Amélioration de la lisibilité des diagrammes dans la documentation back. [#1365](https://github.com/proconnect-gouv/federation/issues/1365)
- Suppression de l'autocomplétion sur le champ des collaborateurs. [#1372](https://github.com/proconnect-gouv/federation/issues/1372)

### Autres changements
- Documentation pour hyyyperbridge ajoutée. [#1392](https://github.com/proconnect-gouv/federation/issues/1392)
- Extraction du script de confirmation de déconnexion dans un fichier externe. [#1410](https://github.com/proconnect-gouv/federation/issues/1410)
- Correction d'un bug où l'IDP non conforme ACR était demandé. [#1340](https://github.com/proconnect-gouv/federation/issues/1340)
- Suppression de tests Kubernetes obsolètes. [#1337](https://github.com/proconnect-gouv/federation/issues/1337)
- Nettoyage des fixtures Cypress pour Kubernetes. [#1373](https://github.com/proconnect-gouv/federation/issues/1373) et [#1364](https://github.com/proconnect-gouv/federation/issues/1364)
- Ajout de règles d'ignorance pour les dépendances PostgreSQL. [#1325](https://github.com/proconnect-gouv/federation/issues/1325)
- Plusieurs mises à jour de dépendances (voir les commits dependabot).
