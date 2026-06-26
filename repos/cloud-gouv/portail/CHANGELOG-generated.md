## Changelog : portail (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité, la flexibilité et la gestion des backends. L'ajout de logs structurés facilite le débogage et le monitoring, tandis que la possibilité de configurer des backends dynamiques offre une plus grande adaptabilité. Des corrections et améliorations de la gestion des erreurs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC [#1234](https://github.com/cloud-gouv/portail/issues/1234).
- Amélioration des messages d'erreur pour les problèmes de permissions dans l'API RPC.
- Possibilité de définir des backends "locaux" via `route.local` pour des configurations spécifiques [#5678](https://github.com/cloud-gouv/portail/issues/5678).
- Implémentation de timeouts pour les connexions HTTP et les tentatives de connexion aux backends.
- Ajout de la commande `rpc update-dynamic-backend` pour mettre à jour les backends dynamiques.
- L'API RPC `ListBackends` fournit désormais des informations plus détaillées sur les backends.

### Évolutions techniques
- Implémentation de logs structurés au format JSON pour le proxy, le serveur RPC et l'acceptor, facilitant l'analyse et le monitoring.
- Ajout de trace IDs dans les contextes pour une meilleure traçabilité des requêtes.
- Refactorisation de la configuration des règles ACL pour utiliser une structure basée sur des attributs.
- Amélioration de la gestion des erreurs lors des connexions upstream (erreurs enrichies).
- Utilisation de `request-timeout` pour gérer les timeouts de connexion HTTP.
- Mise en place d'un système de fan-out pour tous les jobs dans les workflows GitHub Actions, améliorant la performance des tests.
- Migration vers `rustls-pki-types` pour une meilleure gestion des certificats.
- Amélioration de la gestion des erreurs et des logs dans le serveur RPC.
- Optimisation de la sélection des backends.

### Autres changements
- Mise à jour des dépendances (actions/checkout, toml, insta, rand, zlink).
- Amélioration de la documentation et des tests.
- Corrections de typos dans les messages d'erreur RPC.
- Ajustements de la configuration Nix.
- Suppression de dépendances inutiles.
