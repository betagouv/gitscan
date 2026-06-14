## Changelog : federation (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la gestion des accès, notamment via l'ajout d'informations sur l'organisation des utilisateurs et l'alignement avec les définitions légales des services publics. Des mises à jour techniques importantes ont également été effectuées pour moderniser l'infrastructure et les dépendances du projet.

### Évolutions fonctionnelles
- Amélioration de l'autocomplétion Bitwarden pour le champ mot de passe, corrigeant un problème d'utilisation. [#1231](https://github.com/proconnect-gouv/federation/issues/1231)
- Affichage de l'organisation de l'utilisateur dans les messages d'erreur Y500015, pour une meilleure clarté. [#1231](https://github.com/proconnect-gouv/federation/issues/1231)
- Ajout d'un label d'organisation par défaut lors de la création d'un fournisseur de services. [#1185](https://github.com/proconnect-gouv/federation/pulls/1185)
- Ajout du label d'organisation aux scopes retournés. [#1181](https://github.com/proconnect-gouv/federation/issues/1181)
- Alignement de la classification des services publics avec la définition légale actualisée. [#1195](https://github.com/proconnect-gouv/federation/issues/1195)
- Ajout de scopes, de rôles et d'un label d'organisation par défaut dans l'API PCDb. [#1200](https://github.com/proconnect-gouv/federation/issues/1200)

### Évolutions techniques
- Mise à jour de la version de Node.js à 24.16 pour l'application admin. [#1186](https://github.com/proconnect-gouv/federation/pulls/1186)
- Suppression des rôles de base de données dans l'application admin, simplifiant la gestion des accès. [#1184](https://github.com/proconnect-gouv/federation/pulls/1184)
- Suppression de l'application BridgeHttpProxyRie. [#1198](https://github.com/proconnect-gouv/federation/pulls/1198)
- Publication de l'image core-fca-low-migrator sur GHCR. [#1195](https://github.com/proconnect-gouv/federation/issues/1195)
- Utilisation de `fetch` au lieu de `axios` pour certaines requêtes. [#1069](https://github.com/proconnect-gouv/federation/pulls/1069)
- Mise à jour de nombreuses dépendances (Python, Docker, TypeScript, Jest, Cypress, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Configuration du watch pour le Dockerfile MongoDB afin de surveiller les mises à jour. [#1232](https://github.com/proconnect-gouv/federation/issues/1232)
- Inline de la version de MongoDB pour faciliter les mises à jour via Dependabot. [#1216](https://github.com/proconnect-gouv/federation/issues/1216)

### Autres changements
- Mise à jour de la marque de l'application admin de FranceConnect à ProConnect. [#1228](https://github.com/proconnect-gouv/federation/pulls/1228)
- Ajout de logs pour signaler les écarts entre l'ancienne et la nouvelle méthode de calcul des services publics. [#1199](https://github.com/proconnect-gouv/federation/issues/1199)
- Amélioration de la documentation et de la configuration du projet.
