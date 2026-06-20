## Changelog : mcr (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la flexibilité de la plateforme MCR. Des corrections de bugs importantes ont été apportées, notamment concernant la gestion des erreurs et la génération de rapports. De nouvelles fonctionnalités ont été implémentées, comme l'export des rapports vers Google Drive et l'ajout de liens directs vers les documents sur Drive. L'architecture a été revue pour faciliter la maintenance et l'ajout de nouvelles fonctionnalités, avec une migration vers une architecture basée sur des cas d'utilisation (use cases).

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les rapports vers Google Drive via l'API. [#393](https://github.com/IA-Generative/mcr/pull/393)
- Ajout d'un bouton "Afficher sur Drive" pour accéder directement aux rapports sur Google Drive. [#687](https://github.com/IA-Generative/mcr/pull/687)
- Amélioration de la gestion des erreurs et ajout de rapports d'erreurs plus détaillés via Sentry.
- Correction d'un bug empêchant la génération de rapports personnalisés lorsque d'autres rapports étaient déjà générés. [#706](https://github.com/IA-Generative/mcr/pull/706)
- Correction d'un problème où les transcriptions pouvaient échouer en raison de la suppression de la réunion. [#807](https://github.com/IA-Generative/mcr/pull/807)
- Ajout de la possibilité de relancer la génération d'un rapport. [#720](https://github.com/IA-Generative/mcr/pull/720)
- Ajout de la possibilité de télécharger l'audio des réunions. [#757](https://github.com/IA-Generative/mcr/pull/757)
- Amélioration de la gestion des participants dans les transcriptions, évitant leur perte entre les segments. [#701](https://github.com/IA-Generative/mcr/pull/701)
- Ajout de suggestions de prompts personnalisés. [#710](https://github.com/IA-Generative/mcr/pull/710)

### Évolutions techniques
- Migration vers une architecture basée sur des cas d'utilisation (use cases) pour une meilleure organisation et maintenabilité du code.
- Refactorisation du code pour séparer les couches de logique métier, d'infrastructure et de présentation.
- Amélioration de la gestion des erreurs et ajout d'une journalisation plus détaillée.
- Mise en place d'un linter pour garantir la cohérence du code. [#814](https://github.com/IA-Generative/mcr/pull/814)
- Utilisation de `httpx` au lieu de `fastapi` pour les requêtes HTTP. [#854](https://github.com/IA-Generative/mcr/pull/854)
- Amélioration de la gestion des timeouts pour les tâches de transcription. [#846](https://github.com/IA-Generative/mcr/pull/846)
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour des dépendances et amélioration de la configuration de l'environnement de développement.
- Ajout d'une page de maintenance. [#799](https://github.com/IA-Generative/mcr/pull/799)
- Ajout d'un mécanisme de "fail-safe" pour l'initialisation de Sentry. [#836](https://github.com/IA-Generative/mcr/pull/836)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture. [#760](https://github.com/IA-Generative/mcr/pull/760)
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Amélioration de la lisibilité des logs. [#511](https://github.com/IA-Generative/mcr/pull/511)
- Suppression de certaines feature flags. [#770](https://github.com/IA-Generative/mcr/pull/770)
- Ajout d'un script pour faciliter la mise en place de l'environnement de développement local. [#834](https://github.com/IA-Generative/mcr/pull/834)
- Correction de fautes de frappe dans la documentation et le code. [#798](https://github.com/IA-Generative/mcr/pull/798)
