## Changelog : ocr-api (30 derniers jours, au 22 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la sécurisation de l'infrastructure et l'optimisation des processus de déploiement automatique. L'accent a été mis sur la robustesse du système et l'amélioration de la visibilité technique pour garantir une meilleure stabilité opérationnelle.

### Évolutions techniques
- **Observabilité :** Amélioration du suivi des tâches via Langfuse pour assurer une traçabilité précise de chaque opération et une gestion propre des erreurs d'authentification ([c2b9637](https://github.com/IA-Generative/ocr-api/commit/c2b9637a0ee7946e2fba9b513cd56b42b7ae560b), [157ba89](https://github.com/IA-Generative/ocr-api/commit/157ba89a4fc5c21794744c92214872d4008665b3)).
- **Infrastructure & Sécurité :**
  - Durcissement de la sécurité des conteneurs (système de fichiers en lecture seule, gestion des GID) et des composants critiques via Helm (Postgres, Redis, RustFS).
  - Intégration directe du chart Helm dans le dépôt pour simplifier la gestion de l'infrastructure.
- **CI/CD :**
  - Modernisation des pipelines de déploiement via l'adoption de workflows réutilisables et l'utilisation de runners GitHub-hosted.
  - Renforcement de la sécurité des processus (verrouillage des versions d'actions, intégration des résultats de scan de sécurité et gestion des faux positifs Gitleaks).

### Autres changements
- Publication de la version 0.19.11.
