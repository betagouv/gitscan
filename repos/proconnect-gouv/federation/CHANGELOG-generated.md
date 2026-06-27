## Changelog : federation (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des utilisateurs et des organisations, avec l'ajout de fonctionnalités de blocage, de recherche et de gestion des collaborateurs. Des corrections ont également été apportées pour améliorer la robustesse et la conformité du système, notamment concernant la gestion des domaines sans enregistrements MX. Des mises à jour techniques ont été effectuées pour moderniser les dépendances et améliorer la sécurité.

### Évolutions fonctionnelles
- Ajout de la possibilité de rechercher des utilisateurs fédérés par adresse email dans l'interface d'administration. [#1307](https://github.com/proconnect-gouv/federation/issues/1307)
- Implémentation de la gestion des collaborateurs pour les utilisateurs partenaires. [#1310](https://github.com/proconnect-gouv/federation/issues/1310)
- Ajout de la fonctionnalité de blocage d'utilisateurs dans l'interface d'administration. [#1254](https://github.com/proconnect-gouv/federation/issues/1254)
- Amélioration de l'affichage de l'organisation de l'utilisateur dans les messages d'erreur Y500015. [#1331](https://github.com/proconnect-gouv/federation/issues/1331)
- Mise à jour du libellé du checkbox "Se souvenir de moi" pour une meilleure clarté. [#1301](https://github.com/proconnect-gouv/federation/issues/1301)
- Ajout des scopes, roles et organization_label dans l'API pcdb. [#1200](https://github.com/proconnect-gouv/federation/issues/1200)
- Alignement de la classification des services publics avec la définition légale mise à jour. [#1215](https://github.com/proconnect-gouv/federation/issues/1215)

### Évolutions techniques
- Passage de `axios` à `fetch` dans l'application hybride RIE pour une meilleure performance et compatibilité. [#1069](https://github.com/proconnect-gouv/federation/issues/1069)
- Suppression de l'application BridgeHttpProxyRie. [#1198](https://github.com/proconnect-gouv/federation/issues/1198)
- Suppression de PM2 des images de production pour simplifier le déploiement et la gestion. [#1244](https://github.com/proconnect-gouv/federation/issues/1244)
- Ajout du support de Sentinel pour la configuration Redis. [#1265](https://github.com/proconnect-gouv/federation/issues/1265)
- Configuration de la connexion TLS à MongoDB via une variable d'environnement. [#1266](https://github.com/proconnect-gouv/federation/issues/1266)
- Amélioration de la gestion des erreurs et ajout de logs pour les incohérences de classification des services publics. [#1199](https://github.com/proconnect-gouv/federation/issues/1199)
- Mise à jour des dépendances : TypeScript, NestJS, PostgreSQL, Redis, MongoDB, amqplib, bcryptjs, class-validator, express, mongoose, oidc-provider, Jest, Cypress, etc. (voir commits pour détails).
- Suppression des certificats TLS orphelins et configuration simplifiée pour les bases de données. [#1286](https://github.com/proconnect-gouv/federation/issues/1286), [#1287](https://github.com/proconnect-gouv/federation/issues/1287)
- Ajout d'un healthcheck et d'une passerelle pour le broker. [#1262](https://github.com/proconnect-gouv/federation/issues/1262)

### Autres changements
- Suppression des champs `ipAddresses` inutilisés. [#1308](https://github.com/proconnect-gouv/federation/issues/1308)
- Formatage du code source avec Prettier. [#1309](https://github.com/proconnect-gouv/federation/issues/1309)
- Correction de la gestion des domaines sans enregistrements MX selon le comportement RFC. [#1302](https://github.com/proconnect-gouv/federation/issues/1302)
- Mise à jour de la documentation et des configurations.
- Correction de typage dans les fichiers de configuration. [#1291](https://github.com/proconnect-gouv/federation/issues/1291)
