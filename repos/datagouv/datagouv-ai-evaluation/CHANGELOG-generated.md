## Changelog : datagouv-ai-evaluation (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, le projet datagouv-ai-evaluation a connu une refonte significative axée sur l'amélioration de la qualité du code, la documentation et l'ajout de nouvelles fonctionnalités clés. L'introduction d'une couche sémantique et la mise à niveau vers Opik 2 constituent des changements majeurs qui impacteront la manière dont les évaluations sont réalisées. Des améliorations ont également été apportées au suivi des performances et à la gestion des requêtes.

### Évolutions fonctionnelles
- Ajout d'une nouvelle logique "action" vs "tool" pour une meilleure distinction des capacités des agents IA [#326fdc6](https://github.com/datagouv/datagouv-ai-evaluation/commit/326fdc6).
- Possibilité de choisir un modèle "juge" spécifique pour les évaluations et d'utiliser l'API Albert [#4cbc1b7](https://github.com/datagouv/datagouv-ai-evaluation/commit/4cbc1b7).
- Introduction d'une couche sémantique, avec une mise à niveau vers Opik 2 (changement majeur) [#3a14deb](https://github.com/datagouv/datagouv-ai-evaluation/commit/3a14deb).
- Prise en charge de l'acceptation d'une liste de contenu comme réponse dans certaines évaluations [#e578b60](https://github.com/datagouv/datagouv-ai-evaluation/commit/e578b60).
- Calcul de la latence réseau nette (net_latency_ms) pour identifier les problèmes de performance et optimiser les requêtes [#b4a7916](https://github.com/datagouv/datagouv-ai-evaluation/commit/b4a7916).
- Amélioration de la gestion de l'anonymisation des requêtes de support [#1ed37e5](https://github.com/datagouv/datagouv-ai-evaluation/commit/1ed37e5).

### Évolutions techniques
- Adoption de l'outil de linting et de formatage de code `ruff` pour améliorer la qualité et la cohérence du code [#4b01af9](https://github.com/datagouv/datagouv-ai-evaluation/commit/4b01af9).
- Consolidation de la configuration de `pytest` dans le fichier `pyproject.toml` pour une meilleure organisation [#3c9eb22](https://github.com/datagouv/datagouv-ai-evaluation/commit/3c9eb22).
- Automatisation du versionnement avec `setuptools-scm` et un script dédié [#53f2847](https://github.com/datagouv/datagouv-ai-evaluation/commit/53f2847).
- Refactoring et renommage de certains répertoires et métriques pour une meilleure clarté et maintenabilité [#fc6f93f](https://github.com/datagouv/datagouv-ai-evaluation/commit/fc6f93f).

### Autres changements
- Amélioration de la documentation, notamment du fichier `README.md` avec des règles de contribution et une licence [#ecc209a](https://github.com/datagouv/datagouv-ai-evaluation/commit/ecc209a).
- Ajout de notes et réorganisation de la documentation pour une meilleure clarté [#8c3c6a3](https://github.com/datagouv/datagouv-ai-evaluation/commit/8c3c6a3).
- Simplification du fichier `tasks.yml` [#5a5bb5e](https://github.com/datagouv/datagouv-ai-evaluation/commit/5a5bb5e).
- Ajout de "spans" pour le suivi du temps de réflexion ("thinking span") [#88608f4](https://github.com/datagouv/datagouv-ai-evaluation/commit/88608f4).
- Amélioration de la documentation concernant le "thinking span" [#6e5a862](https://github.com/datagouv/datagouv-ai-evaluation/commit/6e5a862).
- Correction de diverses erreurs et améliorations mineures [#360072c](https://github.com/datagouv/datagouv-ai-evaluation/commit/360072c), [#de69cf6](https://github.com/datagouv/datagouv-ai-evaluation/commit/de69cf6), [#0fe12e4](https://github.com/datagouv/datagouv-ai-evaluation/commit/0fe12e4).
