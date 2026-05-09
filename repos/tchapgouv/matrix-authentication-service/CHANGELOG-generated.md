## Changelog : matrix-authentication-service (30 derniers jours, au 7 mai 2026)

### Résumé
Ce changelog couvre les dernières améliorations apportées au service d'authentification Matrix, notamment des corrections pour la gestion des erreurs liées à l'identité, l'ajout de la possibilité de définir le nom d'affichage lors de la création d'utilisateurs via l'API admin, et des mises à jour de sécurité et de dépendances. Des améliorations de la documentation et des outils de débogage ont également été intégrées.

### Évolutions fonctionnelles
- Ajout de la possibilité de définir le nom d'affichage (displayname) lors de l'ajout d'un utilisateur via l'API Admin. [#128](https://github.com/tchapgouv/matrix-authentication-service/issues/128)
- Amélioration de la gestion des erreurs d'identité et de serveur incorrect lors de l'authentification. [#125](https://github.com/tchapgouv/matrix-authentication-service/issues/125)
- Ajout de la prise en charge de liens profonds (deeplinks) Tchap supplémentaires dans la politique OIDC. [#123](https://github.com/tchapgouv/matrix-authentication-service/issues/123)
- Amélioration des labels dans les emails de vérification.
- Ajout de documentation pour faciliter le débogage des politiques. [#5620](https://github.com/tchapgouv/matrix-authentication-service/issues/5620)

### Évolutions techniques
- Mise à jour de `opa-wasm` et `wasmtime` pour corriger des vulnérabilités de sécurité. [#5630](https://github.com/tchapgouv/matrix-authentication-service/issues/5630)
- Mise à jour de `rand` vers la version 0.9.4.
- Utilisation de templates Jinja pour la construction de la configuration du service MAS. [#118](https://github.com/tchapgouv/matrix-authentication-service/issues/118)
- Mise à jour des dépendances Docker et cargo-deny.
- Amélioration de la gestion des conflits de merge.
- Suppression d'un patch obsolète pour `org.matrix.msc3824.action`.
- Mise à jour de `rustls-webpki` vers la version 0.103.13.
- Mises à jour de plusieurs dépendances frontend (tanstack-query, tanstack-router, i18next, vitest, storybook).

### Autres changements
- Mise à jour des traductions. [#5656](https://github.com/tchapgouv/matrix-authentication-service/issues/5656), [#5632](https://github.com/tchapgouv/matrix-authentication-service/issues/5632), [#5624](https://github.com/tchapgouv/matrix-authentication-service/issues/5624), [#5623](https://github.com/tchapgouv/matrix-authentication-service/issues/5623), [#5617](https://github.com/tchapgouv/matrix-authentication-service/issues/5617), [#5597](https://github.com/tchapgouv/matrix-authentication-service/issues/5597), [#5596](https://github.com/tchapgouv/matrix-authentication-service/issues/5596), [#5595](https://github.com/tchapgouv/matrix-authentication-service/issues/5595), [#5594](https://github.com/tchapgouv/matrix-authentication-service/issues/5594)
- Ajout d'un TODO pour l'implémentation des liens profonds.
- Correction de problèmes de build liés à `gouvfr-lasuite/integration`.
- Correction de warnings clippy.
- Mise à jour de la liste de skip list dans `deny.toml`.
- Conversion des emails en minuscules lors de la requête au serveur d'identité.
