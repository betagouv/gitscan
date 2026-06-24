## Changelog : ComparIA (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de performance, de stabilité et de fonctionnalités. L'accent a été mis sur l'optimisation de l'export de données, l'ajout de nouvelles fonctionnalités pour l'analyse des données et l'amélioration de l'expérience utilisateur, notamment sur mobile. Des corrections de bugs et des mises à jour de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'une protection contre les contenus dangereux générés par les modèles de langage via un "content-safety guardrail" [#542](https://github.com/betagouv/ComparIA/pull/542).
- Intégration du modèle GLM 5.2 dans le catalogue de modèles disponibles [#540](https://github.com/betagouv/ComparIA/pull/540), [#531](https://github.com/betagouv/ComparIA/pull/531).
- Amélioration de la gestion des erreurs et du rafraîchissement des tokens Altcha pour une meilleure expérience utilisateur [#545](https://github.com/betagouv/ComparIA/pull/545), [#391](https://github.com/betagouv/ComparIA/pull/391), [#463](https://github.com/betagouv/ComparIA/pull/463).
- Ajout de la possibilité d'exporter des ensembles de données plus rapidement grâce à la mise en cache et à la simplification du processus [#524](https://github.com/betagouv/ComparIA/pull/524), [#516](https://github.com/betagouv/ComparIA/pull/516).
- Ajout de la fonctionnalité de recherche web et intégration des résultats dans l'interface utilisateur.
- Amélioration de l'interface utilisateur mobile, notamment pour les votes et la navigation.
- Ajout de traductions danoises pour les nouveaux modèles et fonctionnalités.
- Ajout de la possibilité de filtrer les comparaisons par présence de PII (informations personnellement identifiables) ou de spam.

### Évolutions techniques
- Refonte de l'architecture de la base de données pour améliorer la performance et la scalabilité.
- Migration vers de nouveaux modèles de données pour les messages, les tours et les comparaisons.
- Optimisation des requêtes de base de données pour l'export des données.
- Amélioration de la gestion des erreurs et de la journalisation.
- Mise à jour des dépendances du projet.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests unitaires et d'intégration.
- Amélioration du pipeline CI/CD.

### Autres changements
- Mise à jour de la documentation.
- Corrections de bugs mineurs.
- Amélioration de la configuration du projet.
- Nettoyage du code.
- Mise à jour des traductions pour plusieurs langues (espagnol, italien, danois, estonien, suédois, lituanien).
- Suppression de modèles obsolètes (GPT 5.4, GLM 5, MiniMax M2.5).
- Blacklisting du modèle Grok.
