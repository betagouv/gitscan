## Changelog : portail (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout du support des groupes supplémentaires pour l'authentification RPC et la correction d'un test lié au multiplexage H2. Ces changements visent à renforcer la flexibilité et la fiabilité du portail.

### Évolutions fonctionnelles
- Ajout du support des groupes supplémentaires pour l'authentification RPC, permettant une gestion plus fine des permissions. [#1234](https://github.com/cloud-gouv/portail/issues/1234) (implémentation liée au commit fa1ec87)

### Évolutions techniques
- Correction d'un test non déterministe lié au multiplexage H2 en utilisant un client Rust minimal. (d04beda)
- Mise à jour des dépendances Rust :
    - `tokio` vers la version 1.52.1
    - `annotate-snippets` vers la version 0.12.15
    - `zlink` vers la version 0.4.2
- Mise à jour de l'action `actions/checkout` vers la version 4.3.1.
