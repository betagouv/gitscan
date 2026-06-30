## Changelog : portail (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité et la flexibilité du portail. L'ajout de logs structurés facilite le débogage et le monitoring, tandis que la possibilité de gérer des backends dynamiques offre une plus grande adaptabilité aux environnements changeants. Des corrections et améliorations de la gestion des erreurs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC. [#b841bdc](https://github.com/cloud-gouv/portail/commit/b841bdc)
- Introduction d'une nouvelle commande `update-dynamic-backend` en CLI pour gérer les backends dynamiques. [#dac0437](https://github.com/cloud-gouv/portail/commit/dac0437)
- Amélioration des informations retournées par l'API `ListBackends` pour une meilleure visibilité sur les backends disponibles. [#98cf10c](https://github.com/cloud-gouv/portail/commit/98cf10c)
- Possibilité de définir un backend par défaut à `null` via l'API Varlink. [#260ea60](https://github.com/cloud-gouv/portail/commit/260ea60)
- Ajout d'un test pour vérifier le timeout de la connexion HTTP. [#f6e3dd0](https://github.com/cloud-gouv/portail/commit/f6e3dd0)
- Utilisation de `request-timeout` pour gérer les timeouts de connexion HTTP et les tentatives de backend. [#dd169c1](https://github.com/cloud-gouv/portail/commit/dd169c1)

### Évolutions techniques
- Implémentation de logs structurés (JSON) pour le proxy HTTP, SOCKS5, le serveur RPC et l'acceptor. [#7930872](https://github.com/cloud-gouv/portail/commit/7930872)
- Ajout d'identifiants de trace (trace IDs) dans les contextes pour faciliter le suivi des requêtes. [#b0c9b01](https://github.com/cloud-gouv/portail/commit/b0c9b01)
- Refactorisation de la configuration des règles ACL pour utiliser une structure basée sur des attributs. [#d9cf054](https://github.com/cloud-gouv/portail/commit/d9cf054)
- Amélioration de la gestion des erreurs de connexion upstream dans le proxy HTTP. [#29a2e96](https://github.com/cloud-gouv/portail/commit/29a2e96)
- Introduction d'une nouvelle constante `route.local` pour identifier les requêtes locales. [#d6bf086](https://github.com/cloud-gouv/portail/commit/d6bf086)
- Mise à jour des dépendances (insta, rand, toml, zlink, rustls-pki-types).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Amélioration des messages d'erreur pour les permissions refusées dans l'API RPC. [#f13f201](https://github.com/cloud-gouv/portail/commit/f13f201)
- Ajout de tests d'intégration pour la mise à jour dynamique des backends. [#e6c57eb](https://github.com/cloud-gouv/portail/commit/e6c57eb)
- Amélioration de la journalisation du démarrage et de la synchronisation du daemon. [#c7287f5](https://github.com/cloud-gouv/portail/commit/c7287f5)
- Fan-out de tous les jobs dans les workflows GitHub Actions pour accélérer l'exécution des tests. [#c2618a8](https://github.com/cloud-gouv/portail/commit/c2618a8)
- Correction de typos dans les messages d'erreur de l'API RPC. [#0423b18](https://github.com/cloud-gouv/portail/commit/0423b18)
- Correction d'un problème de type de pointeur pour assurer la compatibilité multiplateforme. [#a4e3901](https://github.com/cloud-gouv/portail/commit/a4e3901)
