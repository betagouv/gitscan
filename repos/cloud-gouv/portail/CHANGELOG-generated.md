## Changelog : portail (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout du support des groupes supplémentaires pour l'authentification RPC et la correction d'un test lié au multiplexage H2. Ces changements visent à renforcer la sécurité et la flexibilité du portail.

### Évolutions fonctionnelles
- Ajout du support des groupes supplémentaires pour l'authentification RPC, permettant une gestion plus fine des permissions. [#fa1ec87](https://github.com/cloud-gouv/portail/commit/fa1ec87)

### Évolutions techniques
- Correction d'un test non déterministe lié au multiplexage H2 en utilisant un client Rust minimal. [#d04beda](https://github.com/cloud-gouv/portail/commit/d04beda)
- Mise à jour de l'action `actions/checkout` vers la version 4.3.1. [#084f869](https://github.com/cloud-gouv/portail/commit/084f869)
- Mise à jour de la crate Rust `annotate-snippets` vers la version 0.12.15. [#55f3264](https://github.com/cloud-gouv/portail/commit/55f3264)
- Mise à jour de la crate Rust `tokio` vers la version 1.52.1. [#971469a](https://github.com/cloud-gouv/portail/commit/971469a)
- Mise à jour de la crate Rust `zlink` vers la version 0.4.2. [#205c595](https://github.com/cloud-gouv/portail/commit/205c595)
