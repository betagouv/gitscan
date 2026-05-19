## Changelog : portail (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la prise en charge des groupes supplémentaires pour le serveur RPC, permettant une gestion plus fine des autorisations. Un correctif a également été apporté pour rendre les tests de multiplexage H2 plus fiables.

### Évolutions fonctionnelles
- Le serveur RPC prend désormais en charge les groupes supplémentaires, offrant une granularité accrue dans la gestion des accès et des autorisations. [#1234](https://github.com/cloud-gouv/portail/issues/1234) (implémentation liée à la prise en charge des groupes)

### Évolutions techniques
- Correction d'un problème de non-déterminisme dans les tests de multiplexage H2 en utilisant un client Rust minimal.
- Mises à jour des dépendances :
    - `actions/checkout` vers la version 4.3.1
    - `annotate-snippets` vers la version 0.12.15
    - `tokio` vers la version 1.52.1
    - `zlink` vers la version 0.4.2
