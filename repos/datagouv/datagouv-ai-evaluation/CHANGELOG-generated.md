## Changelog : datagouv-ai-evaluation (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, le projet datagouv-ai-evaluation a connu une refonte significative, axée sur l'amélioration de la qualité du code, la documentation et l'introduction d'une nouvelle couche sémantique pour faciliter l'évaluation des modèles d'IA. Des corrections de bugs et des améliorations de la robustesse ont également été apportées, notamment concernant la gestion des tâches et des métriques.

### Évolutions fonctionnelles
- Ajout d'une nouvelle logique "action" vs "tool" pour une meilleure catégorisation des évaluations. [#3](https://github.com/datagouv/datagouv-ai-evaluation/pulls/3)
- Possibilité de choisir un modèle "juge" spécifique pour l'évaluation.
- Prise en charge de l'API Albert pour les modèles.
- Amélioration de la gestion des erreurs et de l'anonymisation des requêtes de support. [#11](https://github.com/datagouv/datagouv-ai-evaluation/pulls/11)
- Ajout du calcul de la latence réseau (net_latency_ms) pour identifier les problèmes de performance.
- Introduction d'une couche sémantique, une modification majeure qui améliore la structure et l'extensibilité du projet et nécessite une mise à jour vers Opik 2. [#11](https://github.com/datagouv/datagouv-ai-evaluation/pulls/11)
- Amélioration de la gestion des spans pour le suivi des temps de traitement, notamment pour la "pensée" du modèle.

### Évolutions techniques
- Refonte de la configuration de pytest et consolidation dans `pyproject.toml`. [#7](https://github.com/datagouv/datagouv-ai-evaluation/pulls/7)
- Adoption de l'outil de linting et de formatage Ruff pour améliorer la qualité du code. [#12](https://github.com/datagouv/datagouv-ai-evaluation/pulls/12)
- Automatisation du versionnement avec `setuptools-scm` et un script dédié. [#11](https://github.com/datagouv/datagouv-ai-evaluation/pulls/11)
- Mise à jour de la documentation et ajout de règles de contribution. [#8](https://github.com/datagouv/datagouv-ai-evaluation/pulls/8), [#9](https://github.com/datagouv/datagouv-ai-evaluation/pulls/9)
- Suppression de code inutilisé et de fichiers vides. [#10](https://github.com/datagouv/datagouv-ai-evaluation/pulls/10), [#16](https://github.com/datagouv/datagouv-ai-evaluation/pulls/16), [#17](https://github.com/datagouv/datagouv-ai-evaluation/pulls/17)
- Amélioration de la structure du projet et des noms de fichiers.

### Autres changements
- Mise à jour de la documentation README pour une meilleure clarté et une description plus précise des capacités d'évaluation.
- Correction de plusieurs erreurs mineures et amélioration de la lisibilité du code.
- Simplification de la configuration des tâches dans le fichier YAML.
- Mise à jour de la version du dataset.
- Correction de noms de services incorrects dans les tâches.
- Ajout de notes et de commentaires dans la documentation.
