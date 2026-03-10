## Changelog : hyyypertool (30 derniers jours)

### Résumé
Les dernières mises à jour de Hyyypertool se concentrent sur l'amélioration de la gestion des modérations, la correction de bugs et l'optimisation de la sécurité. Des améliorations ont été apportées à la gestion des notifications, à la vérification des domaines et à l'interface utilisateur, notamment au niveau des filtres et des composants. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout d'un lien vers les EHPAD dans les actions d'investigation [#1383](https://github.com/proconnect-gouv/hyyypertool/pull/1383).
- Automatisation de la vérification des domaines lors de l'ajout de domaines autorisés [#1433](https://github.com/proconnect-gouv/hyyypertool/pull/1433).
- Simplification des filtres de modération pour une meilleure lisibilité [#1434](https://github.com/proconnect-gouv/hyyypertool/pull/1434).
- Refonte du composant de sélection des membres et des domaines en un composant "island" unifié [#1432](https://github.com/proconnect-gouv/hyyypertool/pull/1432).
- Amélioration de l'accessibilité du tableau avec des liens d'ancrage corrects et une navigation au clavier [#1429](https://github.com/proconnect-gouv/hyyypertool/pull/1429).
- Envoi des notifications de modération traitées via Crisp [#1441](https://github.com/proconnect-gouv/hyyypertool/pull/1441).

### Évolutions techniques
- Suppression de la gestion des Row-Level Security (RLS) dans la base de données [#1475](https://github.com/proconnect-gouv/hyyypertool/pull/1475).
- Refactor de la configuration et de la structure des middlewares [#1474](https://github.com/proconnect-gouv/hyyypertool/pull/1474).
- Mise en place d'une double authentification via l'environnement et la base de données [#1476](https://github.com/proconnect-gouv/hyyypertool/pull/1476).
- Création d'une couche de données "hyperbase" pour une meilleure abstraction de la base de données [#867](https://github.com/proconnect-gouv/hyyypertool/pull/867).
- Suppression de l'intégration Zammad [#1445](https://github.com/proconnect-gouv/hyyypertool/pull/1445).
- Suppression du module `@~/core` [#1447](https://github.com/proconnect-gouv/hyyypertool/pull/1447).
- Mise en place de tests E2E plus robustes avec un mockserver [#1384](https://github.com/proconnect-gouv/hyyypertool/pull/1384).

### Autres changements
- Suppression d'une URL obsolète vers sirene.fr [#1450](https://github.com/proconnect-gouv/hyyypertool/pull/1450).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mises à jour de nombreuses dépendances (voir l'historique des commits pour plus de détails).
- Ajout de documentation et de commentaires pour améliorer la maintenabilité du code.
- Suppression de l'utilisation de `hx-include` pour les éléments DOM inexistants [#1431](https://github.com/proconnect-gouv/hyyypertool/pull/1431).
- Ajout de tests unitaires et E2E pour améliorer la couverture de test.
- Amélioration de la gestion des erreurs et des notifications.
- Ajout de profiling Sentry pour une meilleure analyse des performances [#1406](https://github.com/proconnect-gouv/hyyypertool/pull/1406).
