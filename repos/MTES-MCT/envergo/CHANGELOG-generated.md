## Changelog : envergo (30 derniers jours)

### Résumé
Cette période a été marquée par une amélioration significative de la stabilité et de la fonctionnalité d'envergo. Les efforts se sont concentrés sur la correction de bugs, l'amélioration des tests, l'optimisation de l'interface utilisateur et l'ajout de nouvelles fonctionnalités, notamment concernant la gestion des configurations, la cartographie et l'intégration avec Pipedrive. Des améliorations ont également été apportées à la gestion des données Natura 2000 et à la sécurité.

### Évolutions fonctionnelles
- Correction d'un bug lié à l'affichage des liens dans les messages DS, qui étaient parfois mal interprétés par les navigateurs [#1033](https://github.com/MTES-MCT/envergo/issues/1033).
- Résolution d'un problème avec les réserves naturelles [#1032](https://github.com/MTES-MCT/envergo/issues/1032).
- Correction d'un problème lié à la synchronisation de Pipedrive [#1031](https://github.com/MTES-MCT/envergo/issues/1031).
- Amélioration de la gestion des dates de configuration, permettant un filtrage plus précis [#971](https://github.com/MTES-MCT/envergo/issues/971).
- Ajout de la possibilité de filtrer les départements par date sur la page d'accueil.
- Amélioration de l'affichage et de la gestion des configurations dans l'interface utilisateur.
- Ajout de champs de validité (date de début et de fin) aux configurations.
- Ajout de la possibilité de visualiser les réglementations Natura 2000.
- Ajout d'un bouton pour accéder à la documentation GPU.
- Ajout de la gestion des sites inscrits.
- Mise à jour du champ "PC" (probablement un champ spécifique à l'application).
- Ajout de boutons de copie pour les URLs courtes.
- Correction de problèmes liés à l'affichage des polygones et des données géospatiales.
- Amélioration de la gestion des densités de haies.

### Évolutions techniques
- Refactorisation et amélioration des tests unitaires et d'intégration, avec l'ajout de nouvelles méthodes de test et la correction de tests existants.
- Amélioration de la documentation des tests.
- Mise à jour de Django en 4.2.28.
- Amélioration de la gestion des erreurs et des exceptions.
- Optimisation du code pour éviter les requêtes redondantes.
- Amélioration de la gestion des migrations de base de données.
- Utilisation de contraintes de base de données pour valider l'absence de chevauchement des configurations.
- Amélioration de la sécurité en obscurcissant certaines étapes du processus.
- Suppression de code obsolète et nettoyage du code.
- Correction de problèmes de linting et de formatage du code.
- Amélioration de la gestion des identifiants uniques.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration de la lisibilité du code et de la documentation.
- Amélioration des messages d'erreur et des informations affichées à l'utilisateur.
- Précision des définitions de terrain et d'assiette.
- Mise à jour des noms de variables et de méthodes pour une meilleure clarté.
- Ajout de commentaires pour expliquer certaines décisions d'implémentation.
- Amélioration de la gestion des configurations et des paramètres de l'application.
