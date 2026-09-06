## Changelog : ocr-api (30 derniers jours, au 22 août 2026)

### Résumé
Les récentes évolutions se concentrent sur la robustesse de l'infrastructure et la fiabilité des processus de déploiement. L'accent a été mis sur le renforcement de la sécurité des conteneurs, l'optimisation des pipelines d'intégration continue (CI) et l'amélioration de la visibilité technique sur l'exécution des tâches via un meilleur traçage.

### Évolutions techniques
- **Observabilité** : 
    - Amélioration du traçage avec Langfuse pour garantir une observation réelle et précise pour chaque tâche.
    - Correction de la gestion du client Langfuse pour assurer une fermeture propre en cas d'échec d'authentification.
- **Infrastructure & Déploiement (Helm)** :
    - Intégration directe du chart Helm au sein du dépôt.
    - Renforcement de la sécurité des sous-charts (Postgres, Redis, Rustfs) et durcissement de la configuration des conteneurs (système de fichiers en lecture seule, gestion des GID).
- **CI/CD** :
    - Modernisation des pipelines de CI via l'adoption de workflows réutilisables et l'utilisation de runners hébergés par GitHub.
    - Sécurisation des processus de build (fixation des versions d'actions et amélioration de la gestion des scans de sécurité/Gitleaks).
    - Optimisation de la configuration de publication des charts et des processus de release.
