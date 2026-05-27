## Changelog : portail (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la prise en charge des groupes supplémentaires pour l'authentification RPC et la correction d'un test lié au multiplexage H2. Ces changements visent à renforcer la sécurité et la flexibilité du portail.

### Évolutions fonctionnelles
- Ajout de la prise en charge des groupes supplémentaires pour l'authentification RPC, permettant une gestion plus fine des permissions.  [#fa1ec87](https://github.com/cloud-gouv/portail/commit/fa1ec87)

### Évolutions techniques
- Correction d'un test non déterministe lié au multiplexage H2 en utilisant un client Rust minimal. [#d04beda](https://github.com/cloud-gouv/portail/commit/d04beda)
- Mise à jour de dépendances :
    - `actions/checkout` vers la version 4.3.1
    - `annotate-snippets` vers la version 0.12.15
    - `tokio` vers la version 1.52.1
    - `zlink` vers la version 0.4.2
