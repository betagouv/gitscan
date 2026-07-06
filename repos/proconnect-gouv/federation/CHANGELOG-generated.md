## Changelog : federation (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des utilisateurs et des clients OIDC, la simplification de l'infrastructure et la mise à jour des dépendances. Des corrections ont été apportées pour améliorer la compatibilité avec Bitwarden et l'affichage d'informations utilisateur.

### Évolutions fonctionnelles
- Ajout de la gestion des collaborateurs pour les clients OIDC [#1312](https://github.com/proconnect-gouv/federation/issues/1312).
- Possibilité de rechercher des utilisateurs fédérés par email dans l'interface d'administration [#1307](https://github.com/proconnect-gouv/federation/issues/1307).
- Ajout de la possibilité de bloquer des utilisateurs dans l'interface d'administration [#1254](https://github.com/proconnect-gouv/federation/issues/1254).
- Amélioration de la compatibilité avec l'autocomplétion de mots de passe Bitwarden [#8f0d36d](https://github.com/proconnect-gouv/federation/commit/8f0d36d).
- Mise à jour de la marque dans l'interface d'administration, passant de FranceConnect à ProConnect [#7ac7c45](https://github.com/proconnect-gouv/federation/commit/7ac7c45).
- Affichage de l'organisation de l'utilisateur dans les messages d'erreur Y500015 [#33d0722](https://github.com/proconnect-gouv/federation/commit/33d0722).

### Évolutions techniques
- Suppression de la configuration SSL MongoDB obsolète [#1323](https://github.com/proconnect-gouv/federation/issues/1323).
- Mise à jour de la version de PostgreSQL en local pour correspondre à la production [#1aa317c](https://github.com/proconnect-gouv/federation/commit/1aa317c).
- Suppression de PM2 des images de production pour simplifier le déploiement [#0f80b7c](https://github.com/proconnect-gouv/federation/commit/0f80b7c).
- Ajout du support Sentinel pour Redis [#7a84be7](https://github.com/proconnect-gouv/federation/commit/7a84be7).
- Configuration de MongoDB TLS via variable d'environnement [#cc04a2d](https://github.com/proconnect-gouv/federation/commit/cc04a2d).
- Ajout d'un healthcheck et d'une porte d'entrée pour le broker [#c684aeb](https://github.com/proconnect-gouv/federation/commit/c684aeb).
- Refonte du service de provider OIDC [#6c6e984](https://github.com/proconnect-gouv/federation/commit/6c6e984).
- Suppression des certificats TLS orphelins dans les volumes Docker [#dd3c72b](https://github.com/proconnect-gouv/federation/commit/dd3c72b).

### Autres changements
- Épingle de la version d'Alpine à 3.23.5 dans la stack fca-low [#1325](https://github.com/proconnect-gouv/federation/issues/1325).
- Suppression d'un test Kubernetes obsolète [#1337](https://github.com/proconnect-gouv/federation/issues/1337).
- Mise à jour de diverses dépendances (FastAPI, PostgreSQL, UUID, amqplib, etc.).
- Formatage du code avec Prettier [#73e4c1d](https://github.com/proconnect-gouv/federation/commit/73e4c1d).
- Suppression des champs `ipAddresses` inutilisés [#553a235](https://github.com/proconnect-gouv/federation/commit/553a235).
- Diverses corrections et améliorations de la configuration et de la documentation.
