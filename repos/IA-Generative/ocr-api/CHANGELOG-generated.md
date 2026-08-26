## Changelog : ocr-api (30 derniers jours, au 22 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la stabilisation des capacités de traitement (vision, LLM) et sur un renforcement significatif de la sécurité et de l'automatisation de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- Correction de bugs impactant les modules de vision et de traitement par LLM.
- Fiabilisation du système d'authentification via les clés API.

### Évolutions techniques
- **Infrastructure & Déploiement :** Intégration du chart Helm directement dans le dépôt et durcissement de la sécurité des conteneurs (implémentation de systèmes de fichiers en lecture seule et sécurisation des contextes pour PostgreSQL, Redis et RustFS).
- **CI/CD & Sécurité :** Optimisation des pipelines GitHub Actions (utilisation de runners hébergés, adoption de workflows réutilisables, validation des messages de commit) et amélioration de la visibilité des scans de sécurité.
- **Observabilité :** Amélioration de la précision du tracing via Langfuse (création d'observations réelles pour chaque tâche) et gestion plus robuste des échecs d'authentification du client.
- **Maintenance système :** Corrections apportées à la gestion de la base de données (fallback) et au système de logging.

### Autres changements
- Mise à jour de la configuration de gestion automatique des versions (release-please).
