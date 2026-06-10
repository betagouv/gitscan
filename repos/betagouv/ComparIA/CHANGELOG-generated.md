## Changelog : ComparIA (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de performance, de stabilité et de fonctionnalités. L'export de données a été optimisé pour gérer de plus gros volumes, et l'intégration de la recherche web a été améliorée. Des corrections de bugs et des refactorings importants ont également été effectués, notamment au niveau de la base de données et de l'interface utilisateur. L'ajout de nouveaux modèles de langage et la gestion des traductions ont également été réalisés.

### Évolutions fonctionnelles
- **Recherche Web :** Intégration de la recherche web dans l'interface utilisateur, affichant les liens de recherche dans les messages utilisateur [#401](https://github.com/betagouv/ComparIA/issues/401).
- **Export de données :** Optimisation de l'export de données pour améliorer les performances et réduire la consommation de mémoire [#516](https://github.com/betagouv/ComparIA/issues/516).
- **Nouveaux modèles :** Ajout des modèles Gemini 3.5 Flash et Grok 4.3, et archivage de plusieurs modèles obsolètes [#480](https://github.com/betagouv/ComparIA/issues/480), [#481](https://github.com/betagouv/ComparIA/issues/481).
- **Interface utilisateur :** Amélioration de l'interface utilisateur avec de nouvelles animations pour les votes et les choix, ainsi que des améliorations de la navigation et de l'affichage des messages.
- **Traductions :** Mise à jour des traductions en italien et en danois via Weblate.

### Évolutions techniques
- **Base de données :** Refactoring important des tables de la base de données, incluant la migration de champs, l'ajout d'index et l'amélioration de la gestion des données archivées [#447](https://github.com/betagouv/ComparIA/issues/447).
- **Cache :** Implémentation d'un cache pour les résultats de recherche web afin d'améliorer les performances.
- **Logging :** Amélioration du logging pour faciliter le débogage et le suivi des performances.
- **CI/CD :** Ajout d'une étape de test dans le Makefile.
- **Déploiement :** Simplification de la configuration des variables d'environnement pour les différentes instances.
- **Refactoring général :** Refactoring important du code, notamment au niveau de la gestion des messages, des modèles de données et des routes API.
- **Dépendances :** Mise à jour de certaines dépendances (litellm, typescript).

### Autres changements
- **Documentation :** Ajout de documentation sur les nouvelles fonctionnalités et les changements de configuration.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Gestion des modèles :** Mise en place d'un système pour retirer les modèles "new" après deux mois.
- **Configuration :** Ajout de la variable d'environnement `LINKUP_API_KEY` et mise à jour de la configuration par défaut de `SENTRY_SAMPLE_RATE`.
