## Changelog : mcr (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la robustesse de l'application, l'ajout de nouvelles fonctionnalités comme le téléchargement des rapports sur Google Drive, et l'amélioration de l'observabilité et de la gestion des erreurs. Une refonte architecturale est également en cours pour améliorer la maintenabilité et l'évolutivité du code, avec une migration vers une architecture basée sur des cas d'utilisation.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger les rapports générés sur Google Drive. [#865](https://github.com/IA-Generative/mcr/pull/865)
- Possibilité de télécharger les fichiers audio associés aux réunions. [#772](https://github.com/IA-Generative/mcr/pull/772)
- Amélioration de la gestion des URL de webinaires pour une meilleure reconnaissance. [#863](https://github.com/IA-Generative/mcr/pull/863)
- Ajout d'une page de maintenance. [#799](https://github.com/IA-Generative/mcr/pull/799)
- Amélioration de la gestion des erreurs et ajout d'une meilleure observabilité avec Sentry. [#793](https://github.com/IA-Generative/mcr/pull/793)
- Amélioration de la gestion des erreurs lors du téléchargement de fichiers. [#864](https://github.com/IA-Generative/mcr/pull/864)

### Évolutions techniques
- Refactorisation importante du code vers une architecture basée sur des cas d'utilisation pour une meilleure organisation et maintenabilité. (Plusieurs PRs : [#828](https://github.com/IA-Generative/mcr/pull/828), [#823](https://github.com/IA-Generative/mcr/pull/823), [#820](https://github.com/IA-Generative/mcr/pull/820), [#770](https://github.com/IA-Generative/mcr/pull/770), [#755](https://github.com/IA-Generative/mcr/pull/755), [#745](https://github.com/IA-Generative/mcr/pull/745))
- Mise en place de pre-commit hooks pour améliorer la qualité du code (linting, formatage, scan de secrets). [#874](https://github.com/IA-Generative/mcr/pull/874)
- Utilisation de `httpx` au lieu de `fastapi` pour la gestion des requêtes HTTP dans le client de réunion. [#854](https://github.com/IA-Generative/mcr/pull/854)
- Amélioration de la gestion des timeouts pour les tâches de transcription et les appels aux services externes. [#848](https://github.com/IA-Generative/mcr/pull/848)
- Amélioration de la robustesse de l'initialisation de Sentry. [#836](https://github.com/IA-Generative/mcr/pull/836)
- Amélioration de la gestion des erreurs liées aux bases de données. [#831](https://github.com/IA-Generative/mcr/pull/831)
- Migration vers un modèle LLM gptoss. [#785](https://github.com/IA-Generative/mcr/pull/785)

### Autres changements
- Mise à jour de la documentation pour la génération de comptes rendus. [#760](https://github.com/IA-Generative/mcr/pull/760)
- Ajout d'un skill de débogage pour faciliter le diagnostic des problèmes en production. [#792](https://github.com/IA-Generative/mcr/pull/792)
- Amélioration de la lisibilité des logs. [#745](https://github.com/IA-Generative/mcr/pull/745)
- Correction de bugs mineurs et améliorations de la stabilité.
- Mise à jour des dépendances et configuration de l'environnement de développement.
