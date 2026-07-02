## Changelog : portail (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité, la flexibilité et la gestion des backends. L'ajout de logs structurés facilite le débogage et le monitoring, tandis que la possibilité de mettre à jour dynamiquement les backends offre une plus grande agilité. Des corrections et améliorations ont également été apportées à la gestion des erreurs et aux tests.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC [#1234](https://github.com/cloud-gouv/portail/issues/1234).
- Introduction d'une nouvelle commande CLI `rpc update-dynamic-backend` pour gérer les backends dynamiques.
- Amélioration des messages d'erreur pour les problèmes de permission dans l'API RPC.
- Ajout d'un test pour le timeout de connexion HTTP.
- Implémentation du timeout pour les connexions HTTP et les tentatives de backend.
- Introduction d'une nouvelle route `route.local` pour le proxy ACL [#5678](https://github.com/cloud-gouv/portail/issues/5678).

### Évolutions techniques
- Ajout de logs structurés au niveau du proxy (HTTP, SOCKS5), du serveur RPC et de l'acceptor, facilitant l'observabilité et le débogage.
- Refonte de la configuration des règles ACL en utilisant une structure basée sur des attributs.
- Amélioration de la gestion des erreurs et des logs dans le contexte du proxy.
- Utilisation de `request-timeout` pour gérer les délais de connexion HTTP.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (insta, rand, toml, zlink, rustls-pki-types).
- Amélioration des tests d'intégration et E2E.
- Fan-out de tous les jobs dans les workflows GitHub Actions pour accélérer l'exécution des tests.

### Autres changements
- Déplacement du socket RPC dans un répertoire dédié.
- Correction de typos dans les messages d'erreur RPC.
- Amélioration de la documentation et des commentaires.
- Mise à jour de l'action `actions/checkout` dans les workflows GitHub Actions.
