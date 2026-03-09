## Changelog : benefriches (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur une refonte significative de l'expérience utilisateur pour la création de projets, notamment pour les projets urbains et photovoltaïques. Des améliorations ont été apportées à l'interface, à la logique de création, et à la gestion des erreurs. Des efforts ont également été déployés pour améliorer la qualité du code, la documentation et l'infrastructure de test.

### Évolutions fonctionnelles
- Ajout d'une intégration avec un chat d'assistance (Crisp) pour aider les utilisateurs rencontrant des problèmes d'authentification. [#84f110f](https://github.com/incubateur-ademe/benefriches/commit/84f110f)
- Amélioration de la recherche d'adresse avec une mise en cache des résultats pour éviter les problèmes de concurrence. [#d2bc5e3](https://github.com/incubateur-ademe/benefriches/commit/d2bc5e3)
- Ajout de pictogrammes pour les différents types d'usages dans la création de projets urbains. [#9c399c9](https://github.com/incubateur-ademe/benefriches/commit/9c399c9)
- Possibilité de supprimer des projets depuis les listes et la page d'impacts. [#bef2355](https://github.com/incubateur-ademe/benefriches/commit/bef2355)
- Ajout de dialogues de blocage de navigation lors de la création de sites et de projets pour éviter les pertes de données. [#7f91806](https://github.com/incubateur-ademe/benefriches/commit/7f91806)
- Mise à jour de l'affichage des types de sols pour assurer une cohérence dans les vues avec les diagrammes circulaires. [#86dbd6d](https://github.com/incubateur-ademe/benefriches/commit/86dbd6d)
- Ajout de la possibilité de créer des projets agricoles et des friches personnalisés via les tests E2E. [#9f15613](https://github.com/incubateur-ademe/benefriches/commit/9f15613) et [#7cc2d58](https://github.com/incubateur-ademe/benefriches/commit/7cc2d58)
- Amélioration de l'affichage des données dans les formulaires de surface au sol des projets urbains. [#1ab513a](https://github.com/incubateur-ademe/benefriches/commit/1ab513a)
- Ajout de la possibilité d'archiver un projet de reconversion via l'API. [#d8b3adb](https://github.com/incubateur-ademe/benefriches/commit/d8b3adb)

### Évolutions techniques
- Refactorisation importante du code de création de projets urbains pour une meilleure organisation et maintenabilité.
- Déplacement des factories de création de sites vers l'API pour une meilleure séparation des préoccupations. [#34d7f51](https://github.com/incubateur-ademe/benefriches/commit/34d7f51)
- Utilisation du pattern ViewData pour simplifier la gestion des données dans les composants web.
- Amélioration des tests unitaires et E2E pour une meilleure couverture et fiabilité.
- Mise en place d'un pattern de gateway pour l'intégration de services tiers (analytics, Crisp chat).
- Refactorisation de la structure des dossiers pour une meilleure organisation du code.
- Amélioration de l'installation des dépendances dans le script `create-worktree.sh`.
- Mise à jour des dépendances (oxlint, prettier, etc.). [#52bae42](https://github.com/incubateur-ademe/benefriches/commit/52bae42)

### Autres changements
- Ajout de documentation sur les décisions architecturales (ADR).
- Mise à jour de la documentation CLAUDE.md pour refléter les changements et les bonnes pratiques.
- Amélioration des scripts d'outils pour faciliter le développement et la revue de code.
- Correction de plusieurs erreurs mineures et améliorations de la qualité du code.
- Clarification des messages et des libellés dans l'interface utilisateur.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
