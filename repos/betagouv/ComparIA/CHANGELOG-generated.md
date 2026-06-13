## Changelog : ComparIA (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de performance, de robustesse et de fonctionnalités. L'accent a été mis sur l'amélioration de l'export de données, l'intégration de nouveaux modèles de langage, la gestion des spams et des contenus inappropriés, ainsi que la refonte de l'interface utilisateur pour une meilleure expérience. Des corrections de bugs et des optimisations de la base de données ont également été apportées.

### Évolutions fonctionnelles
- **Web Search:** Intégration de la recherche web dans l'interface utilisateur, permettant d'afficher des liens de recherche contextuels dans les conversations. [#401](https://github.com/betagouv/ComparIA/pull/401)
- **Nouveaux modèles de langage:** Ajout des modèles Gemini 3.5 Flash et Grok 4.3, et mise à jour de Trinity Large Preview vers Trinity Large Thinking. [#480](https://github.com/betagouv/ComparIA/pull/480), [#481](https://github.com/betagouv/ComparIA/pull/481)
- **Vote et animations:** Amélioration de l'expérience utilisateur lors du vote avec des animations et des retours visuels plus clairs.
- **Interface utilisateur:** Refonte de l'interface utilisateur avec de nouveaux composants (SideSwitcher, VoteModal) et une meilleure organisation des éléments.
- **Gestion des spams et contenus inappropriés:** Amélioration de la détection et du blocage des spams et des tentatives de jailbreak. [#481](https://github.com/betagouv/ComparIA/pull/481)
- **Export de données:** Optimisation de l'export de données pour une meilleure performance, notamment en utilisant un cache basé sur des fichiers Parquet. [#516](https://github.com/betagouv/ComparIA/pull/516)

### Évolutions techniques
- **Base de données:** Refonte des tables de la base de données pour une meilleure structure et performance. Migration des données existantes. [#447](https://github.com/betagouv/ComparIA/pull/447)
- **Architecture:** Utilisation de SQLModel pour une meilleure gestion des modèles de données et des interactions avec la base de données.
- **Streaming:** Amélioration du streaming des réponses pour une expérience utilisateur plus réactive.
- **Cache:** Implémentation d'un cache pour les résultats de recherche web afin de réduire la charge sur l'API Linkup.
- **Logging:** Ajout de logs de performance pour identifier les goulots d'étranglement lors du démarrage de l'application.
- **Déploiement:** Amélioration du processus de migration de la base de données.
- **Dépendances:** Mises à jour de plusieurs dépendances (protobufjs, pip, npm).
- **Refactoring:** Refactorisation importante du code, notamment dans les parties liées à la gestion des messages, des conversations et de l'interface utilisateur.

### Autres changements
- **Documentation:** Mise à jour de la documentation et des exemples de configuration.
- **Traduction:** Ajout et mise à jour des traductions en danois et en italien.
- **Nettoyage de code:** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Tests:** Ajout de tests unitaires et d'intégration.
- **Configuration:** Ajout de variables d'environnement pour faciliter la configuration de l'application.
- **Suppression de code obsolète:** Suppression de code lié à des fonctionnalités abandonnées ou remplacées.
