## Changelog : matrix-authentication-service (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions du service d'authentification Matrix se concentrent sur l'amélioration de l'expérience administrateur, la correction de bugs liés à l'intégration avec le serveur d'identité, et la mise à jour de plusieurs dépendances pour renforcer la sécurité et la stabilité. Une nouvelle version (v1.16.0) a été publiée avec des correctifs de traduction et des mises à jour de sécurité.

### Évolutions fonctionnelles
- Les administrateurs peuvent désormais définir le nom d'affichage d'un utilisateur lors de sa création via l'API Admin. [#128](https://github.com/tchapgouv/matrix-authentication-service/issues/128)
- Amélioration de la gestion des erreurs provenant du serveur d'identité, notamment pour les cas d'erreur `identity_server` et `wrong_server`. [#125](https://github.com/tchapgouv/matrix-authentication-service/issues/125)
- Extension des liens profonds (deeplinks) autorisés dans la politique OIDC pour une meilleure intégration avec Tchap. [#123](https://github.com/tchapgouv/matrix-authentication-service/issues/123)
- Les emails de vérification ont été mis à jour avec de nouveaux labels.
- Mise à jour des traductions pour la version 1.16. [#5656](https://github.com/tchapgouv/matrix-authentication-service/issues/5656)

### Évolutions techniques
- Mise à jour de `rustls-webpki` vers la version 0.103.13.
- Mise à jour de `opa-wasm` vers la version 0.2.0 et de `wasmtime` pour corriger des vulnérabilités de sécurité. [#5630](https://github.com/tchapgouv/matrix-authentication-service/issues/5630)
- Mise à jour de la librairie `rand` vers la version 0.9.4.
- Refonte de la construction de la configuration de MAS en utilisant des templates Jinja2. [#118](https://github.com/tchapgouv/matrix-authentication-service/issues/118)
- Suppression d'un patch obsolète pour `org.matrix.msc3824.action`.
- Correction de conflits de merge lors de l'intégration de la version 1.15.0.
- Amélioration de la gestion des erreurs de merge.
- Correction de problèmes de build en rétrogradant `gouvfr-lasuite/integration`.
- Correction de warnings clippy.

### Autres changements
- Ajout d'un TODO concernant l'implémentation des liens profonds.
- Mise à jour de la liste de skip dans le fichier `deny.toml`.
- Publication des versions 1.16.0, 1.16.0-rc.0 et 1.15.0.
- Mise à jour des traductions.
