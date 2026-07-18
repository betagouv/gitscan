## Changelog : portail (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité et la qualité du logging du portail. De nombreuses modifications ont été apportées pour introduire des logs structurés, facilitant ainsi le débogage et le monitoring. Des corrections ont également été apportées pour améliorer la gestion des requêtes locales et la compatibilité avec certains protocoles.

### Évolutions fonctionnelles
- Correction d'un problème empêchant l'évaluation des ACLs pour les connexions UDP ASSOCIATE. [#issue à investiguer](https://github.com/cloud-gouv/portail/issues/)
- Amélioration de la gestion des erreurs et des réponses pour les requêtes HTTP, notamment en renvoyant les erreurs client au client et en améliorant le logging des connexions. [#issue à investiguer](https://github.com/cloud-gouv/portail/issues/)
- Revalidation des requêtes `route.local` pour les proxies HTTP et SOCKS5, améliorant la sécurité et la fiabilité. [#issue à investiguer](https://github.com/cloud-gouv/portail/issues/)

### Évolutions techniques
- Introduction de logs structurés au format JSON pour plusieurs composants : proxy (HTTP, SOCKS5), serveur RPC, daemon et contexte.
- Ajout de trace IDs dans les contextes pour faciliter le suivi des requêtes à travers les différents composants.
- Refactorisation du logging pour séparer les logs du serveur RPC et du CLI.
- Déplacement du socket RPC dans un répertoire plus approprié.
- Amélioration du logging du démarrage et de la synchronisation du daemon.

### Autres changements
- Mise à jour de plusieurs dépendances Rust (uuid, anyhow, bytes, regex, rustls-pki-types).
- Mise à jour de l'action GitHub `actions/checkout` vers la version 7.
- Amélioration de la configuration Nix pour inclure les directives de logging.
- Modifications diverses pour améliorer la lisibilité et la maintenabilité du code.
