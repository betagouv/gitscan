## Changelog : federation (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité (ajout d'un indicateur de conformité MFA), la gestion des utilisateurs (gestion des collaborateurs pour les clients OIDC et blocage d'utilisateurs), et la maintenance technique (mises à jour de dépendances, suppression de configurations TLS obsolètes et simplification de l'infrastructure Docker). L'interface d'administration a également été mise à jour pour refléter le nouveau branding ProConnect.

### Évolutions fonctionnelles
- Ajout d'un indicateur de conformité MFA (Multi-Factor Authentication) pour les fournisseurs d'identité. [#1335](https://github.com/proconnect-gouv/federation/pull/1335)
- Possibilité de bloquer des utilisateurs dans l'interface d'administration. [#1254](https://github.com/proconnect-gouv/federation/pull/1254)
- Gestion des collaborateurs pour les clients OIDC, permettant de définir des utilisateurs ayant accès à la gestion du client. [#1292](https://github.com/proconnect-gouv/federation/pull/1292) et [#1312](https://github.com/proconnect-gouv/federation/pull/1312)
- Amélioration de l'autocomplétion Bitwarden pour le champ mot de passe. [#1244](https://github.com/proconnect-gouv/federation/pull/1244)
- Possibilité de rechercher des utilisateurs fédérés par adresse email dans l'interface d'administration. [#1307](https://github.com/proconnect-gouv/federation/pull/1307)
- Mise à jour du branding de l'interface d'administration pour refléter ProConnect. [#1228](https://github.com/proconnect-gouv/federation/pull/1228)
- Affichage de l'organisation de l'utilisateur dans les messages d'erreur Y500015. [#1331](https://github.com/proconnect-gouv/federation/pull/1331)

### Évolutions techniques
- Suppression de la configuration TLS inutile pour MongoDB et PostgreSQL. [#1266](https://github.com/proconnect-gouv/federation/pull/1266), [#1283](https://github.com/proconnect-gouv/federation/pull/1283), [#1285](https://github.com/proconnect-gouv/federation/pull/1285), [#1286](https://github.com/proconnect-gouv/federation/pull/1286)
- Simplification de l'infrastructure Docker et suppression de PM2. [#1244](https://github.com/proconnect-gouv/federation/pull/1244) et [#1265](https://github.com/proconnect-gouv/federation/pull/1265)
- Mise à jour de nombreuses dépendances (Node.js, TypeScript, Docker, PostgreSQL, MongoDB, Redis, etc.).
- Ajout du support Sentinel pour Redis. [#1265](https://github.com/proconnect-gouv/federation/pull/1265)
- Amélioration de la configuration et du typage. [#1288](https://github.com/proconnect-gouv/federation/pull/1288) et [#1291](https://github.com/proconnect-gouv/federation/pull/1291)
- Ajout de healthchecks pour le broker. [#1262](https://github.com/proconnect-gouv/federation/pull/1262)

### Autres changements
- Suppression de tests Kubernetes obsolètes. [#1337](https://github.com/proconnect-gouv/federation/pull/1337)
- Suppression du widget de chat Crisp. [#1324](https://github.com/proconnect-gouv/federation/pull/1324)
- Mise à jour de la documentation. [#1341](https://github.com/proconnect-gouv/federation/pull/1341) et [#1364](https://github.com/proconnect-gouv/federation/pull/1364)
- Nettoyage du code et refactoring.
- Backfill des propriétaires d'applications en tant que collaborateurs. [#1344](https://github.com/proconnect-gouv/federation/pull/1344)
- Correction d'un bug lié à la gestion des domaines sans enregistrements MX. [#1302](https://github.com/proconnect-gouv/federation/pull/1302)
- Correction d'un bug dans la migration pour la valeur par défaut de `isMfaCompliant`. [#1363](https://github.com/proconnect-gouv/federation/pull/1363)
