## Changelog : portail (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité et la gestion dynamique des backends. L'ajout de logs structurés facilite le débogage et le monitoring, tandis que la possibilité de mettre à jour les backends à la volée offre une plus grande flexibilité de configuration. Des améliorations de la robustesse et des tests ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC. [#1234](https://github.com/cloud-gouv/portail/issues/1234)
- Introduction d'une commande `update-dynamic-backend` en CLI pour gérer les backends dynamiques.
- Amélioration des informations retournées par l'API `ListBackends` pour une meilleure visibilité sur les backends configurés.
- Possibilité de définir un backend par défaut nul via l'API RPC.
- Ajout d'un test pour vérifier le timeout de la connexion HTTP.
- Ajout d'un test pour vérifier le timeout de la connexion HTTP.

### Évolutions techniques
- Implémentation de logs structurés dans de nombreux composants : proxy SOCKS5, proxy HTTP, RPC, daemon, et contexte du proxy.
- Ajout de trace IDs dans les contextes du proxy pour faciliter le suivi des requêtes.
- Refactorisation de la configuration des règles ACL pour utiliser une structure basée sur des attributs.
- Amélioration de la gestion des erreurs RPC avec des messages plus clairs.
- Refactorisation du code pour supporter les backends dynamiques dans le proxy.
- Fan-out de tous les jobs dans les workflows GitHub Actions pour accélérer l'exécution des tests.
- Mise à jour de l'action `actions/checkout` en version 6.
- Amélioration de la gestion des types de pointeurs pour une meilleure compatibilité multiplateforme.
- Introduction d'une variable `route.local` dans la configuration du proxy ACL.

### Autres changements
- Mise à jour des dépendances : `insta`, `rand`, `toml`, `rustls-pki-types`, `zlink`.
- Correction de fautes de frappe dans les messages d'erreur RPC.
- Suppression de dépendances inutilisées.
- Amélioration de la configuration des logs dans le module Nix.
- Suppression de la spécification de timeout dans les tests Nix pour `identity-aware`.
- Déplacement du socket RPC dans un répertoire plus approprié.
- Amélioration des logs de démarrage et de synchronisation du daemon.
