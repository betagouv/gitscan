## Changelog : portail (30 derniers jours, au 2026-06-10)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'API RPC et l'ajout de fonctionnalités pour une gestion plus flexible des backends. Une nouvelle option `route.local` a été introduite pour le proxy ACL, offrant un contrôle plus précis du routage.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité `ListBackends` à l'API RPC, permettant de lister les backends disponibles. [#8f6daae](https://github.com/cloud-gouv/portail/commit/8f6daae)
- La fonction `SetDefaultBackend` de l'API Varlink accepte désormais la valeur `null`, offrant plus de flexibilité dans la configuration des backends. [#260ea60](https://github.com/cloud-gouv/portail/commit/260ea60)
- Introduction de l'option `route.local` dans le proxy ACL, permettant de définir des routes locales. [#d6bf086](https://github.com/cloud-gouv/portail/commit/d6bf086)

### Évolutions techniques
- Mise à jour des dépendances `insta`, `rand`, `toml` et `zlink` vers des versions compatibles. (f38dd32, 7f511b4, 6c0e3e7, 34c1fd3, 15f951e)
- Relaxation des contraintes de version des dépendances pour une meilleure compatibilité. (15f951e)
- Migration vers `rustls-pki-types` pour une gestion améliorée des certificats. (47803ff)
- Suppression de la dépendance `peekable`. (6c0e3e7)
