## Changelog : ocr-api (30 derniers jours, au 22 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la sécurisation de l'infrastructure et l'optimisation des processus de déploiement automatisés. L'accent a été mis sur une meilleure observabilité des tâches et un renforcement de la sécurité des conteneurs pour garantir un environnement de production plus robuste.

### Évolutions techniques
- **Observabilité**
  - Amélioration du suivi des tâches via Langfuse : ouverture systématique d'observations pour chaque tâche et gestion propre de la fermeture du client en cas d'échec d'authentification.
- **Infrastructure & Sécurité**
  - Migration du chart Helm directement au sein du dépôt pour une meilleure gestion.
  - Renforcement de la sécurité des conteneurs et des services (Postgres, Redis, RustFS) via l'application de contextes de sécurité et l'utilisation d'un système de fichiers en lecture seule.
- **CI/CD**
  - Optimisation des pipelines de déploiement : publication des charts via Cloud π Native, utilisation de runners GitHub-hosted et verrouillage des versions des actions pour plus de stabilité.
  - Amélioration de la qualité et de la sécurité du code : intégration de contrôles de conformité des messages de commit (commitlint) et automatisation des scans de sécurité avec remontée des résultats dans l'interface GitHub.
