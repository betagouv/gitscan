## Changelog : portail (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la prise en charge des groupes supplémentaires pour le serveur RPC, permettant une gestion plus fine des autorisations. Des corrections ont également été apportées pour garantir la stabilité des tests.

### Évolutions fonctionnelles
- Le serveur RPC prend désormais en charge les groupes supplémentaires, offrant une granularité accrue dans la gestion des accès et des autorisations. [#1234](https://github.com/cloud-gouv/portail/issues/1234) (implémentation basée sur le commit fa1ec87)

### Évolutions techniques
- Correction d'un problème de non-déterminisme dans le test de multiplexage h2 en utilisant un client tiny rust. (d04beda)
- Mises à jour de dépendances pour les crates Rust `tokio`, `zlink` et `annotate-snippets`. (971469a, 205c595, 55f3264)
- Mise à jour de l'action `actions/checkout` à la version v4.3.1. (084f869)
