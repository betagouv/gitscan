## Changelog : datagouv-ai-evaluation (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, le projet datagouv-ai-evaluation a bénéficié d'une refonte significative, incluant l'adoption de nouveaux outils de linting et de formatage du code (Ruff, isort), l'amélioration de la documentation et l'introduction d'une couche sémantique pour une meilleure organisation et évolutivité. Des améliorations ont également été apportées à la gestion des métriques, à l'intégration avec l'API Albert et à la gestion des délais de réponse.

### Évolutions fonctionnelles
- Ajout d'une couche sémantique, une évolution majeure qui impacte la structure du projet et la manière dont les évaluations sont définies et exécutées. [#3](https://github.com/datagouv/datagouv-ai-evaluation/pull/3)
- Possibilité de choisir un modèle spécifique pour le "judge" (évaluation).
- Intégration avec l'API Albert pour l'utilisation de modèles.
- Calcul du délai de réponse net (`net_latency_ms`) pour aider à identifier les problèmes de performance et à ajuster les stratégies de "backoff".
- Amélioration de la gestion des tâches d'évaluation pour éviter les doublons. [#12](https://github.com/datagouv/datagouv-ai-evaluation/pull/12)
- Prise en charge de listes de contenu en tant que réponse.
- Introduction d'une nouvelle logique "action" vs "tool" pour une meilleure organisation des fonctionnalités. [#326fdc6](https://github.com/datagouv/datagouv-ai-evaluation/commit/326fdc6)
- Ajout de la notion de "thinking span" pour mesurer le temps de réflexion des modèles. [#88608f4](https://github.com/datagouv/datagouv-ai-evaluation/commit/88608f4)

### Évolutions techniques
- Adoption de l'outil Ruff pour le linting et le formatage du code, améliorant la qualité et la cohérence du code. [#4b01af9](https://github.com/datagouv/datagouv-ai-evaluation/commit/4b01af9)
- Consolidation de la configuration de pytest dans `pyproject.toml`. [#7](https://github.com/datagouv/datagouv-ai-evaluation/pull/7)
- Automatisation du versionnement avec `setuptools-scm` et un script dédié. [#11](https://github.com/datagouv/datagouv-ai-evaluation/pull/11)
- Mise à jour vers Opik 2, nécessitant des changements importants dans l'implémentation. [#3a14deb](https://github.com/datagouv/datagouv-ai-evaluation/commit/3a14deb)
- Simplification du fichier `tasks.yml`. [#5a5bb5e](https://github.com/datagouv/datagouv-ai-evaluation/commit/5a5bb5e)
- Amélioration de la documentation et des exemples de configuration.

### Autres changements
- Amélioration de la documentation README avec des informations sur la contribution et la licence. [#9](https://github.com/datagouv/datagouv-ai-evaluation/pull/9)
- Ajout d'une section sur l'utilisation de pre-commit dans la documentation.
- Clarification de la documentation README concernant les capacités d'évaluation.
- Ajout de notes et de commentaires dans la documentation.
- Correction de liens et d'erreurs dans la documentation.
- Amélioration de la lisibilité et de l'organisation de la documentation.
- Ajout de notes sur les solutions aux problèmes rencontrés dans la documentation.
- Renommage du répertoire principal.
- Mise à jour des métriques pour une meilleure compréhension.
- Correction de problèmes mineurs et de "leftovers" dans le code.
- Anonymisation des requêtes de support.
- Amélioration du nommage des datasets et des expériences.
- Amélioration de la documentation de l'outil CLI.
