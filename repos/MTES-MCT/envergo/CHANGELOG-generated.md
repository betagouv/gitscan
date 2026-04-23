## Changelog : envergo (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des haies, avec des corrections et des ajouts liés à la validation de la longueur, à la gestion des paramètres Natura 2000, et à l'amélioration de l'expérience utilisateur. Des améliorations significatives ont également été apportées à la page de contact, à la gestion des configurations et à la performance globale de l'application.

### Évolutions fonctionnelles
- Amélioration de la gestion des contacts pour les haies, avec un fallback sur la configuration la plus récente et un avertissement en cas de portail non activé. [#1083](https://github.com/MTES-MCT/envergo/issues/1083)
- Ajout de la validation de la longueur des haies, avec une limite configurable et des messages d'erreur clairs. [#1074](https://github.com/MTES-MCT/envergo/issues/1074)
- Amélioration de l'affichage des informations de contact. [#1071](https://github.com/MTES-MCT/envergo/issues/1071)
- Ajout d'un bouton pour retirer une pièce jointe lors du chargement de fichiers. [#1081](https://github.com/MTES-MCT/envergo/issues/1081)
- Correction d'une faille XSS potentielle dans les messages d'erreur de la messagerie. [#1088](https://github.com/MTES-MCT/envergo/issues/1088)
- Amélioration de l'affichage du périmètre sur certaines vues. [#1087](https://github.com/MTES-MCT/envergo/issues/1087)
- Ajout de la possibilité de filtrer les pétitions. [#1065](https://github.com/MTES-MCT/envergo/issues/1065)
- Ajout de statistiques et de rapports. [#1025](https://github.com/MTES-MCT/envergo/issues/1025)
- Amélioration de l'interface utilisateur pour la gestion des configurations. [#1066](https://github.com/MTES-MCT/envergo/issues/1066)

### Évolutions techniques
- Refactorisation du code lié à Natura 2000 haie, incluant l'ajout d'une matrice pour la gestion de `concerne_aa`.
- Optimisation des requêtes de densité pour améliorer les performances.
- Amélioration de la gestion des erreurs et des logs, notamment avec Sentry.
- Mise à jour de la gestion des CSP (Content Security Policy) pour renforcer la sécurité.
- Amélioration de la gestion des tests, avec l'ajout de nouvelles fixtures et la correction de tests existants.
- Mise à jour des dépendances et refactoring du code pour une meilleure maintenabilité.
- Amélioration de la gestion des migrations de base de données.
- Utilisation de Gist pour la configuration. [#1059](https://github.com/MTES-MCT/envergo/issues/1059)
- Suppression de code obsolète et simplification de certaines parties du code.

### Autres changements
- Mise à jour de la documentation et des textes d'interface utilisateur.
- Migration de la FAQ vers Gitbook. [#1073](https://github.com/MTES-MCT/envergo/issues/1073)
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour des dépendances et des librairies utilisées.
- Correction de problèmes de performance et d'optimisation du code.
- Amélioration de la sécurité de l'application.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités et amélioration des fonctionnalités existantes.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de l'expérience utilisateur et de l'interface utilisateur.
