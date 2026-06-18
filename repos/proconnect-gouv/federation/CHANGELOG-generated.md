## Changelog : federation (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité et de la stabilité de la plateforme, notamment par la mise à jour des dépendances et la suppression de composants obsolètes. Des améliorations ont également été apportées à la gestion des rôles et des organisations, ainsi qu'à la compatibilité avec les dernières versions de Node.js et Python.

### Évolutions fonctionnelles
- Amélioration de l'affichage de l'organisation de l'utilisateur dans les messages d'erreur Y500015. [#1231](https://github.com/proconnect-gouv/federation/issues/1231)
- Ajout de l'étiquette d'organisation par défaut lors de la création d'un prestataire de services. [#1188](https://github.com/proconnect-gouv/federation/issues/1188)
- Alignement de la classification des services publics avec la définition légale mise à jour. [#1215](https://github.com/proconnect-gouv/federation/issues/1215)
- Amélioration de l'autocomplétion Bitwarden pour le champ mot de passe. [#1244](https://github.com/proconnect-gouv/federation/pulls/1244)
- Ajout des scopes, rôles et étiquettes d'organisation par défaut dans l'API pcdb. [#1200](https://github.com/proconnect-gouv/federation/issues/1200)

### Évolutions techniques
- Suppression de PM2 des images de production pour simplifier la configuration et améliorer la fiabilité. [#1261](https://github.com/proconnect-gouv/federation/pulls/1261)
- Suppression de l'application BridgeHttpProxyRie. [#1198](https://github.com/proconnect-gouv/federation/pulls/1198)
- Suppression des rôles de base de données. [#1184](https://github.com/proconnect-gouv/federation/pulls/1184)
- Mise à jour de Node.js en version 24.16 pour l'application admin. [#1186](https://github.com/proconnect-gouv/federation/pulls/1186) et [#1187](https://github.com/proconnect-gouv/federation/pulls/1187)
- Mise à jour de Python et des dépendances de l'API pcdb. [#1182](https://github.com/proconnect-gouv/federation/issues/1182), [#1178](https://github.com/proconnect-gouv/federation/issues/1178), [#1183](https://github.com/proconnect-gouv/federation/issues/1183)
- Ajout d'un healthcheck `readyz` pour améliorer la surveillance de l'application. [#1261](https://github.com/proconnect-gouv/federation/pulls/1261)
- Publication de l'image `core-fca-low-migrator` sur GHCR. [#1195](https://github.com/proconnect-gouv/federation/pulls/1195)

### Autres changements
- Mise à jour des dépendances (axe-core, @simonsmith/cypress-image-snapshot, @nestjs/testing, ts-jest, ruff, prettier, etc.)
- Configuration de Dependabot pour surveiller le Dockerfile MongoDB. [#1232](https://github.com/proconnect-gouv/federation/issues/1232)
- Inclusion de la version de MongoDB dans la configuration Docker. [#1216](https://github.com/proconnect-gouv/federation/issues/1216)
- Utilisation de `fetch` au lieu de `axios`. [#1069](https://github.com/proconnect-gouv/federation/pulls/1069) et [#790d7c9](https://github.com/proconnect-gouv/federation/commit/790d7c9)
