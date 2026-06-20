## Changelog : federation (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité et de la stabilité de la plateforme, notamment en mettant à jour les dépendances et en simplifiant la configuration de l'infrastructure. Des améliorations ont également été apportées à l'expérience utilisateur, avec des corrections et des ajustements pour une meilleure compatibilité avec les outils d'autocomplétion et une mise à jour de l'identité visuelle.

### Évolutions fonctionnelles
- Mise à jour de l'identité visuelle de l'interface d'administration, remplaçant le branding FranceConnect par ProConnect. [#1228](https://github.com/proconnect-gouv/federation/pull/1228)
- Amélioration de l'autocomplétion des mots de passe avec Bitwarden. [#1244](https://github.com/proconnect-gouv/federation/pull/1244)
- Ajout de l'organisation de l'utilisateur dans les messages d'erreur Y500015 pour une meilleure clarté. [#1231](https://github.com/proconnect-gouv/federation/pull/1231)
- Ajout de l'étiquette d'organisation par défaut lors de la création d'un prestataire de services. [#1185](https://github.com/proconnect-gouv/federation/pull/1185)
- Alignement de la classification des services publics avec la définition légale actualisée. [#1215](https://github.com/proconnect-gouv/federation/pull/1215)

### Évolutions techniques
- Configuration de la prise en charge de Sentinel pour la configuration Redis. [#1265](https://github.com/proconnect-gouv/federation/pull/1265)
- Possibilité de configurer le TLS MongoDB via une variable d'environnement. [#1266](https://github.com/proconnect-gouv/federation/pull/1266)
- Suppression de PM2 des images de production pour simplifier le déploiement. [#1244](https://github.com/proconnect-gouv/federation/pull/1244)
- Suppression du proxy HTTP BridgeRie. [#1198](https://github.com/proconnect-gouv/federation/pull/1198)
- Mise à jour de la version de Node.js en version 24.16 pour l'application admin. [#1187](https://github.com/proconnect-gouv/federation/pull/1187) et [#1186](https://github.com/proconnect-gouv/federation/pull/1186)
- Ajout de healthchecks `readyz` pour le composant `base-core`. [#1261](https://github.com/proconnect-gouv/federation/pull/1261)
- Publication de l'image `core-fca-low-migrator` sur GHCR. [#1195](https://github.com/proconnect-gouv/federation/pull/1195)
- Suppression des rôles de base de données. [#1184](https://github.com/proconnect-gouv/federation/pull/1184)
- Utilisation de `fetch` au lieu de `axios` dans certaines parties du code. [#1069](https://github.com/proconnect-gouv/federation/pull/1069)

### Autres changements
- Mise à jour de nombreuses dépendances (cryptography, fastapi, ioredis, pydantic, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Mise à jour des actions CI/CD (docker/login-action, docker/build-push-action, actions/labeler, etc.).
- Diverses corrections et améliorations de la configuration et du code.
