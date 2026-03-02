## Changelog : benefriches (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à benefriches au cours des 30 derniers jours. Les modifications incluent des refactorings importants pour améliorer la structure du code et sa maintenabilité, des corrections de bugs pour une meilleure expérience utilisateur, l'ajout de nouvelles fonctionnalités comme l'intégration d'un chat d'assistance, et des améliorations de la documentation pour faciliter la contribution et la compréhension du projet.

### Évolutions fonctionnelles
- Ajout d'un chat d'assistance Crisp pour aider les utilisateurs rencontrant des problèmes d'authentification [#8faf085](https://github.com/incubateur-ademe/benefriches/commit/8faf085).
- Amélioration de la gestion des types de sols dans les formulaires de projets urbains, avec des affichages plus clairs et des corrections de libellés [#95b6e9d](https://github.com/incubateur-ademe/benefriches/commit/95b6e9d).
- Ajout de pictogrammes pour les différents usages dans les projets urbains [#9c399c9](https://github.com/incubateur-ademe/benefriches/commit/9c399c9).
- Possibilité de supprimer des projets depuis les listes et les pages de détails [#bef2355](https://github.com/incubateur-ademe/benefriches/commit/bef2355).
- Ajout de dialogues de blocage de navigation sur les formulaires de création de site et de projet [#7f91806](https://github.com/incubateur-ademe/benefriches/commit/7f91806).
- Ajout de séparateurs de milliers pour les montants monétaires [#032146a](https://github.com/incubateur-ademe/benefriches/commit/032146a).
- Ajout de menus d'actions sur les tuiles de projets [#08f10e2](https://github.com/incubateur-ademe/benefriches/commit/08f10e2).

### Évolutions techniques
- Refactorings importants de l'architecture du frontend React, notamment l'application du pattern "ViewData" pour une meilleure gestion des données et des tests unitaires plus robustes [#4912b2e](https://github.com/incubateur-ademe/benefriches/commit/4912b2e), [#8cf0735](https://github.com/incubateur-ademe/benefriches/commit/8cf0735), [#26c1a30](https://github.com/incubateur-ademe/benefriches/commit/26c1a30).
- Simplification du processus de build Scalingo pour une meilleure efficacité [#1d47c9d](https://github.com/incubateur-ademe/benefriches/commit/1d47c9d).
- Amélioration de la gestion des erreurs et des validations dans les formulaires numériques [#4dcf4cf](https://github.com/incubateur-ademe/benefriches/commit/4dcf4cf).
- Migration vers `createReducer` pour une meilleure gestion de l'état avec Redux Toolkit [#649e03c](https://github.com/incubateur-ademe/benefriches/commit/649e03c).
- Mise à jour des dépendances (oxlint, prettier, etc.) [#52bae42](https://github.com/incubateur-ademe/benefriches/commit/52bae42).

### Autres changements
- Amélioration de la documentation (CLAUDE.md) pour clarifier les exigences de qualité, les définitions des types de sols et l'utilisation de Zod [#e953e04](https://github.com/incubateur-ademe/benefriches/commit/e953e04), [#3b9254d](https://github.com/incubateur-ademe/benefriches/commit/3b9254d), [#b541430](https://github.com/incubateur-ademe/benefriches/commit/b541430).
- Ajout de nouvelles entrées ADR (Architecture Decision Records) pour documenter les décisions architecturales clés [#cdc0db9](https://github.com/incubateur-ademe/benefriches/commit/cdc0db9), [#ff311a4](https://github.com/incubateur-ademe/benefriches/commit/ff311a4), [#f84ecef](https://github.com/incubateur-ademe/benefriches/commit/f84ecef).
- Ajout d'outils et de scripts pour améliorer la qualité du code et le processus de revue (code-reviewer, skills) [#c20f527](https://github.com/incubateur-ademe/benefriches/commit/c20f527), [#4e0e25a](https://github.com/incubateur-ademe/benefriches/commit/4e0e25a), [#076fc86](https://github.com/incubateur-ademe/benefriches/commit/076fc86).
- Corrections de typos et améliorations de la formulation dans la documentation et l'interface utilisateur [#83c58fa](https://github.com/incubateur-ademe/benefriches/commit/83c58fa).
- Suppression de code mort et nettoyage général du code [#f67cf21](https://github.com/incubateur-ademe/benefriches/commit/f67cf21), [#53b3b80](https://github.com/incubateur-ademe/benefriches/commit/53b3b80), [#20fd9d6](https://github.com/incubateur-ademe/benefriches/commit/20fd9d6).
