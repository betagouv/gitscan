## Changelog : federation (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité et de la flexibilité de la plateforme, notamment en permettant le blocage d'utilisateurs dans l'interface d'administration et en simplifiant la configuration de la base de données. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- Ajout de la possibilité de bloquer les utilisateurs via l'interface d'administration. [#1254](https://github.com/proconnect-gouv/federation/issues/1254)
- Amélioration de l'affichage de l'organisation de l'utilisateur dans les messages d'erreur Y500015. [#1231](https://github.com/proconnect-gouv/federation/issues/1231)
- Mise à jour des valeurs ACR (Attestation de Conformité Réussie) pour une meilleure intégration. [#1217](https://github.com/proconnect-gouv/federation/issues/1217)
- Alignement de la classification des services publics avec la définition légale actualisée. [#1215](https://github.com/proconnect-gouv/federation/issues/1215)
- Amélioration de l'autocomplétion Bitwarden pour le champ mot de passe. [#1244](https://github.com/proconnect-gouv/federation/issues/1244)
- Mise à jour de l'icône de l'application dans l'interface d'administration pour refléter la marque ProConnect. [#1228](https://github.com/proconnect-gouv/federation/issues/1228)

### Évolutions techniques
- Suppression de TLS pour la base de données MongoDB locale afin de simplifier la configuration en environnement de développement. [#1283](https://github.com/proconnect-gouv/federation/issues/1283)
- Suppression des configurations TLS obsolètes pour PostgreSQL et promotion de pg-admin dans la configuration partagée. [#1287](https://github.com/proconnect-gouv/federation/issues/1287)
- Suppression de Redis\_CACERT des fichiers d'environnement. [#1285](https://github.com/proconnect-gouv/federation/issues/1285)
- Suppression des certificats TLS orphelins du dossier `docker/volumes/ssl`. [#1286](https://github.com/proconnect-gouv/federation/issues/1286)
- Ajout d'un healthcheck et d'une passerelle pour le broker. [#1262](https://github.com/proconnect-gouv/federation/issues/1262)
- Suppression de PM2 des images de production Docker. [#1244](https://github.com/proconnect-gouv/federation/issues/1244)
- Ajout du support de Sentinel pour la configuration Redis. [#1265](https://github.com/proconnect-gouv/federation/issues/1265)
- Configuration de MongoDB TLS via une variable d'environnement. [#1266](https://github.com/proconnect-gouv/federation/issues/1266)
- Refactorisation du service de provider OIDC. [#1288](https://github.com/proconnect-gouv/federation/issues/1288)
- Publication de l'image core-fca-low-migrator sur GHCR. [#1195](https://github.com/proconnect-gouv/federation/issues/1195)
- Mise à jour vers Node 24.16 dans l'administration. [#1187](https://github.com/proconnect-gouv/federation/issues/1187)
- Utilisation de `fetch` au lieu de `axios` dans certains composants. [#1069](https://github.com/proconnect-gouv/federation/issues/1069)

### Autres changements
- Correction de typage dans les fichiers de configuration. [#1291](https://github.com/proconnect-gouv/federation/issues/1291)
- Mise à jour de diverses dépendances (Cypress, Jest, prettier, etc.).
- Mise à jour des actions GitHub (checkout, labeler, etc.).
- Mise à jour des versions des images Docker (nginx, postgres, redis, mongo).
- Ajout de la configuration pour dependabot afin de surveiller le Dockerfile mongodb. [#1232](https://github.com/proconnect-gouv/federation/issues/1232)
- Inline de la version de MongoDB pour dependabot. [#1216](https://github.com/proconnect-gouv/federation/issues/1216)
