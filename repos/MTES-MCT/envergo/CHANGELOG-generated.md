## Changelog : envergo (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des haies, avec des ajouts de validations, de configurations et de tests. L'interface utilisateur a également été améliorée, notamment pour la page de contact et l'affichage des résultats. Des corrections de bugs et des optimisations de performance ont été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la validation de la longueur maximale des haies, configurable en backend et avec un message d'erreur associé. [#1074](https://github.com/MTES-MCT/envergo/issues/1074)
- Amélioration du formulaire de contact, avec la prise en compte de la configuration la plus récente et un fallback en cas d'absence de contacts. [#1085](https://github.com/MTES-MCT/envergo/issues/1085)
- Ajout d'un bouton pour retirer une pièce jointe lors de l'upload de fichiers. [#1081](https://github.com/MTES-MCT/envergo/issues/1081)
- Correction de l'affichage du périmètre sur certaines pages. [#1087](https://github.com/MTES-MCT/envergo/issues/1087)
- Ajout d'un paramètre "aa handling" pour gérer le cas échéant. [#1088](https://github.com/MTES-MCT/envergo/issues/1088)
- Amélioration de l'affichage des résultats et ajout de nouvelles options de configuration pour les réglementations. [#1070](https://github.com/MTES-MCT/envergo/issues/1070)
- Ajout de filtres et d'une interface utilisateur pour la gestion des projets. [#1065](https://github.com/MTES-MCT/envergo/issues/1065)
- Ajout d'une page de contact améliorée avec des informations pertinentes. [#1066](https://github.com/MTES-MCT/envergo/issues/1066)
- Migration de la FAQ utilisateur vers Gitbook. [#1073](https://github.com/MTES-MCT/envergo/issues/1073)

### Évolutions techniques
- Refactor de la gestion de `concerne_aa` pour Natura 2000 Haie, avec l'utilisation de migrations de données et de champs de choix.
- Optimisations de performance pour les requêtes de densité. [#1059](https://github.com/MTES-MCT/envergo/issues/1059)
- Mise à jour des dépendances et corrections de bugs liés à l'infrastructure de déploiement.
- Amélioration des tests unitaires et d'intégration, notamment pour les haies et les réglementations.
- Correction de problèmes de sécurité (XSS) dans l'affichage des messages d'erreur.
- Ajout de tests Playwright pour la couverture des tests E2E.
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs.
- Utilisation de Gist pour l'indexation des données. [#1078](https://github.com/MTES-MCT/envergo/issues/1078)

### Autres changements
- Mise à jour de la documentation et des textes de l'interface utilisateur.
- Correction de coquilles et amélioration de la lisibilité du code.
- Ajout de commentaires et de docstrings pour faciliter la maintenance.
- Suppression de code obsolète et nettoyage du code source.
- Ajout d'analytics pour suivre l'utilisation de l'application.
- Ajout de la gestion des erreurs Sentry.
- Amélioration de la gestion des configurations et des paramètres.
- Ajout de la gestion des événements d'accordéon.
- Ajout de la gestion des erreurs 429 et amélioration des messages d'erreur.
- Ajout de la gestion des erreurs de réseau.
- Ajout de la gestion des erreurs de timeout.
