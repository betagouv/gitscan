## Changelog : mcr (30 derniers jours, au 5 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application MCR, notamment l'ajout de nouvelles fonctionnalités pour la gestion des notes, la génération de rapports personnalisés et l'amélioration de la robustesse et de la flexibilité du système. Des efforts ont également été déployés pour améliorer la documentation, les tests et l'infrastructure du projet.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant de télécharger les fichiers audio des réunions [#757](https://github.com/IA-Generative/mcr/issues/757).
- Implémentation de la possibilité de relancer la génération d'un rapport en cas d'échec [#720](https://github.com/IA-Generative/mcr/issues/720).
- Ajout d'une page de maintenance pour signaler les interruptions de service [#798](https://github.com/IA-Generative/mcr/issues/798).
- Possibilité d'ajouter des notes personnalisées aux rapports, avec une intégration dans les différentes étapes du pipeline de génération [#755](https://github.com/IA-Generative/mcr/issues/755), [#727](https://github.com/IA-Generative/mcr/issues/727), [#637](https://github.com/IA-Generative/mcr/issues/637), [#638](https://github.com/IA-Generative/mcr/issues/638).
- Ajout d'une fonctionnalité pour générer des rapports au format DOCX [#625](https://github.com/IA-Generative/mcr/issues/625).
- Ajout d'un bouton "Voir dans Drive" pour accéder directement aux rapports générés sur Google Drive [#687](https://github.com/IA-Generative/mcr/issues/687).
- Amélioration de la gestion des participants et de leur identification dans les rapports [#639](https://github.com/IA-Generative/mcr/issues/639), [#640](https://github.com/IA-Generative/mcr/issues/640).

### Évolutions techniques
- Migration vers une organisation basée sur le "trunk-based development" pour une meilleure gestion des versions et des déploiements [#796](https://github.com/IA-Generative/mcr/issues/796).
- Refactorisation de l'architecture pour séparer les responsabilités et améliorer la maintenabilité du code.
- Amélioration de la gestion des erreurs et des exceptions, notamment lors de la génération de rapports.
- Mise à jour des dépendances et des outils de développement.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Amélioration des tests unitaires et d'intégration pour garantir la qualité du code.
- Utilisation de nouveaux modèles GPTOSS pour l'analyse du langage naturel [#761](https://github.com/IA-Generative/mcr/issues/761).
- Optimisation des performances et de la scalabilité du système.
- Amélioration de la journalisation et de la surveillance du système.
- Ajout de tests pour la gestion des états de la transcription et de la génération de rapports.
- Refonte de l'infrastructure Celery pour une meilleure gestion des tâches asynchrones.

### Autres changements
- Amélioration de la documentation du projet, notamment pour les nouvelles fonctionnalités et l'architecture du système [#756](https://github.com/IA-Generative/mcr/issues/756).
- Mise à jour des instructions de démarrage du projet dans le fichier README.
- Ajout d'un outil d'évaluation pour les rapports générés [#593](https://github.com/IA-Generative/mcr/issues/593).
- Ajout d'un glossaire avec 428 acronymes pour faciliter la compréhension des rapports [#642](https://github.com/IA-Generative/mcr/issues/642).
- Suppression des feature flags obsolètes [#712](https://github.com/IA-Generative/mcr/issues/712).
- Ajout d'un outil de linting pour garantir la qualité du code.
- Amélioration de la lisibilité des logs.
- Ajout d'une intégration avec Sentry pour la surveillance des erreurs.
- Ajout d'un nouveau membre à l'équipe Slack.
