## Changelog : portail (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité et la robustesse du proxy. L'ajout de logs structurés et l'amélioration de la gestion des erreurs permettent un diagnostic plus facile et une meilleure réactivité en cas de problème. Des corrections ont également été apportées pour améliorer la gestion des requêtes locales et la compatibilité avec certains protocoles.

### Évolutions fonctionnelles
- Correction d'un problème empêchant l'évaluation des ACLs pour les connexions UDP ASSOCIATE. [#issue - lien non disponible]
- Amélioration de la gestion des erreurs lors des connexions HTTP : les erreurs du backend sont maintenant enrichies et renvoyées au client.
- Les requêtes vers `route.local` sont maintenant correctement revalidées pour les proxies HTTP et SOCKS5.
- Amélioration de la gestion des timeouts pour les connexions HTTP, avec l'utilisation de `request-timeout` pour les tentatives de connexion et de backend. [#issue - lien non disponible]
- Ajout d'un test pour vérifier le timeout des connexions HTTP. [#issue - lien non disponible]

### Évolutions techniques
- Implémentation de logs structurés (JSON) pour plusieurs composants : proxy (HTTP, SOCKS5), serveur RPC, et daemon.
- Introduction de trace IDs dans les contextes pour faciliter le suivi des requêtes.
- Refactorisation de la gestion des contextes pour une meilleure clarté et maintenabilité.
- Amélioration de la configuration des règles ACL dans le module Nix, en passant à une approche basée sur des ensembles d'attributs.
- Optimisation de l'exécution des jobs dans les workflows GitHub Actions (GHA) en les parallélisant.
- Déplacement du socket RPC dans un répertoire plus approprié.

### Autres changements
- Mise à jour de plusieurs dépendances Rust (anyhow, bytes, regex, rustls-pki-types, uuid).
- Mise à jour de l'action GitHub Actions `actions/checkout` vers la version 7 et 6.
- Amélioration de la documentation et des messages de log pour une meilleure lisibilité.
- Nettoyage et refactoring de code divers pour améliorer la qualité globale du projet.
