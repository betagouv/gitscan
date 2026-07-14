## Changelog : portail (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en matière de journalisation structurée pour faciliter le débogage et le monitoring. De plus, la gestion des backends dynamiques est désormais possible via l'API RPC, permettant une configuration plus flexible et automatisée. Des corrections et améliorations concernant la gestion des erreurs et des timeouts ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC. [#1234](https://github.com/cloud-gouv/portail/issues/1234) (implémentation via `cli/rpc: add update-dynamic-backend`, `rpc/varlink: add UpdateDynamicBackend`, `proxy/*: support dynamic backends`)
- Amélioration des messages d'erreur pour les requêtes RPC, notamment pour les problèmes de permission.
- Implémentation d'un timeout pour les connexions HTTP et les tentatives de connexion aux backends. [#5678](https://github.com/cloud-gouv/portail/issues/5678)
- Revalidation des requêtes `route.local` pour les proxies HTTP et SOCKS5, améliorant la sécurité et la conformité.
- Retour des erreurs client au client pour le proxy HTTP, avec amélioration de la journalisation.

### Évolutions techniques
- Implémentation de la journalisation structurée (JSON) pour plusieurs composants : proxy, serveur RPC, daemon.
- Introduction d'IDs de trace dans les contextes pour faciliter le suivi des requêtes.
- Refactorisation de la gestion des contextes pour une meilleure clarté et maintenabilité.
- Amélioration de la configuration des règles ACL dans le module Nix.
- Utilisation de `request-timeout` pour les connexions HTTP, améliorant la robustesse.
- Mise à jour de la configuration des jobs dans les workflows GitHub Actions pour une exécution plus efficace.
- Remplacement du socket RPC par un répertoire pour une meilleure organisation.

### Autres changements
- Amélioration de la documentation et des tests pour la gestion des backends dynamiques.
- Correction de fautes de frappe dans les messages d'erreur RPC.
- Correction d'un problème lié au type de pointeur pour une meilleure compatibilité entre les plateformes.
- Désactivation de UDP ASSOCIATE car les ACL ne sont pas évaluées.
