## Changelog : ComparIA (30 derniers jours)

### Résumé
Ce mois-ci, ComparIA a connu une refonte majeure de son architecture backend, avec une migration vers FastAPI et Pydantic pour une meilleure structure et validation des données. De nombreuses améliorations ont été apportées à la gestion des modèles, des données et des sessions, ainsi qu'à la robustesse et à la journalisation du code. L'interface utilisateur a également été optimisée et des corrections de bugs ont été implémentées. Plusieurs nouveaux modèles de langage ont été ajoutés et les données ont été mises à jour.

### Évolutions fonctionnelles
- Ajout des modèles Ordbogen Odin (odin-large, odin-medium) pour le portail danois. [#303](https://github.com/betagouv/ComparIA/pull/303)
- Ajout des modèles Qwen 3.5 397B et MiniMax M2.5, et archivage des modèles plus anciens.
- Ajout des modèles Claude Sonnet 4.6 et Gemini 3.1 pro.
- Mise à jour des données des modèles et ajout de nouveaux modèles (Arcee Trinity Large, Kimi K2.5, Qwen3-Coder-Next). [#287](https://github.com/betagouv/ComparIA/pull/287), [#302](https://github.com/betagouv/ComparIA/pull/302), [#291](https://github.com/betagouv/ComparIA/pull/291)
- Correction de l'URL de Kimi. [#291](https://github.com/betagouv/ComparIA/pull/291)
- Ajout d'un lien vers le tableau de bord Matrice d'impact dans le footer. [#310](https://github.com/betagouv/ComparIA/pull/310), [#311](https://github.com/betagouv/ComparIA/pull/311)
- Ajout d'un popup Tally pour recueillir des commentaires sur les pages françaises. [#311](https://github.com/betagouv/ComparIA/pull/311)

### Évolutions techniques
- Refonte complète du backend avec migration vers FastAPI et Pydantic pour une meilleure structure et validation des données.
- Amélioration de la gestion des sessions et des conversations.
- Optimisation de la gestion des erreurs et ajout de la journalisation avec Sentry.
- Amélioration de la gestion des dépendances et des fichiers de configuration.
- Mise en place d'un système de build plus robuste avec Docker Bake.
- Amélioration des tests et de la couverture de code.
- Utilisation de Redis pour la mise en cache et la gestion des sessions.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de types et de validations Pydantic pour une meilleure robustesse du code.
- Amélioration de la gestion des logs et ajout d'un logger configurable.
- Mise à jour des dépendances et des outils de développement.

### Autres changements
- Mise à jour des traductions pour le norvégien Bokmål et le norvégien Nynorsk via Weblate. [#333](https://github.com/betagouv/ComparIA/pull/333), [#247](https://github.com/betagouv/ComparIA/pull/247)
- Mise à jour des données générées.
- Ajout de documentation et de commentaires dans le code.
- Nettoyage du code et suppression du code obsolète.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Mise à jour des modèles de licence.
- Ajout de fichiers de contribution (CONTRIBUTING.md).
- Amélioration des scripts de build et de déploiement.
