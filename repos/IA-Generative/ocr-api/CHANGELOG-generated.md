## Changelog : ocr-api (30 derniers jours, au 22 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la stabilisation des fonctionnalités d'intelligence artificielle et le renforcement de la sécurité de l'infrastructure. Les corrections apportées améliorent la fiabilité de l'extraction visuelle et de la gestion des accès, tandis que les processus de déploiement et de surveillance ont été modernisés pour garantir un environnement plus robuste et sécurisé.

### Évolutions fonctionnelles
- **Intelligence Artificielle :** Résolution de problèmes affectant le traitement par LLM et les capacités de vision (OCR).
- **Sécurité des accès :** Correction du système de gestion des clés API.

### Évolutions techniques
- **Infrastructure & Déploiement (Helm) :**
  - Intégration directe du chart Helm dans le dépôt pour une meilleure gestion.
  - Renforcement de la sécurité des conteneurs (système de fichiers racine en lecture seule, gestion des GID) et des sous-composants (PostgreSQL, Redis, RustFS).
- **CI/CD & Sécurité :**
  - Modernisation des pipelines de déploiement via l'adoption de workflows réutilisables et l'utilisation de runners GitHub-hosted.
  - Amélioration de la détection de secrets et de la gestion des scans de sécurité (Gitleaks, Strix).
  - Automatisation et fiabilisation du processus de publication des versions (release-please).
- **Observabilité :** Optimisation du traçage des tâches avec Langfuse pour un suivi plus précis des opérations.
- **Système :** Corrections sur le mécanisme de secours (fallback) de la base de données et sur la journalisation (logging).
