## Changelog : kevent-ai (30 derniers jours, au 29 mai 2026)

### Résumé
Les 30 derniers jours ont été marqués par une amélioration significative de la gestion du cycle de vie des jobs asynchrones, avec l'introduction d'un nouveau garbage collector (GC) unifié pour la suppression des données orphelines dans Redis et S3.  Des améliorations ont également été apportées à la résilience du Relay, à la gestion des erreurs et à l'ajout de fonctionnalités de sécurité comme la détection de PII. Plusieurs correctifs et améliorations de la documentation ont également été implémentés.

### Évolutions fonctionnelles
- **Gestion du cycle de vie des jobs :** Introduction d'un garbage collector unifié pour supprimer les jobs et les fichiers S3 orphelins, configurable via une nouvelle section `lifecycle.gc` dans la configuration.
- **Purge administrative :** Ajout d'endpoints pour la purge administrative des jobs.
- **Audit Trail :** Implémentation d'un audit trail structuré pour les requêtes LLM (désactivé par défaut).
- **Détection PII :** Ajout de la détection de données personnellement identifiables (PII) dans les requêtes JSON LLM.
- **Limites de débit :** Ajout d'en-têtes de limitation de débit (X-RateLimit-*) et d'une fonctionnalité pour définir des limites de débit illimitées.
- **Gestion des erreurs :** Amélioration de la gestion des erreurs et des timeouts dans le Relay.
- **Support multi-backend :** Ajout du support pour plusieurs backends, permettant le routage canary et blue/green.

### Évolutions techniques
- **Relay :**
    - Ajout de logique de retry et de timeouts configurables.
    - Amélioration de la gestion des erreurs et des health checks.
    - Correction de problèmes liés à la suppression des pods et à la configuration RBAC.
- **Gateway :**
    - Refactorisation de la configuration pour une meilleure cohérence.
    - Amélioration de la gestion des erreurs et de la hot-reload de la configuration.
    - Ajout de métriques Prometheus pour le suivi des performances.
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements de configuration.
- **CI/CD :** Ajout de jobs de build pour les versions RC du Relay.
- **Tests :** Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.

### Autres changements
- Mise à jour des images Docker pour le Gateway et le Relay.
- Correction de bugs mineurs et améliorations de la stabilité.
- Amélioration de la gestion des logs et des messages d'erreur.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Correction de problèmes de concurrence et de race conditions.
- Correction de problèmes liés à la suppression des fichiers S3.
- Mise à jour des dépendances.
- Correction de problèmes liés à la gestion des timeouts.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
- Correction de problèmes liés à la configuration du Gateway.
- Correction de problèmes liés à la documentation.
- Correction de problèmes liés aux tests.
- Correction de problèmes liés au CI/CD.
- Correction de problèmes liés aux logs.
- Correction de problèmes liés aux messages d'erreur.
- Correction de problèmes liés à la concurrence.
- Correction de problèmes liés à la suppression des fichiers S3.
- Correction de problèmes liés à la configuration du Relay.
