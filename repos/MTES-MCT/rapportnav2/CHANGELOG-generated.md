## Changelog : rapportnav2 (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration des missions et des actions, notamment avec l'ajout d'une interface dédiée dans l'espace administrateur. Des corrections de performance et des ajustements de l'interface utilisateur ont également été apportés. L'intégration des données de pays via une API a été finalisée.

### Évolutions fonctionnelles
- Ajout d'une interface d'administration pour gérer les actions, incluant la possibilité de définir le propriétaire de l'action.
- Possibilité de rechercher les missions par ID et ID interne dans l'interface d'administration.
- Pré-remplissage de la table des missions et synchronisation avec les données environnementales.
- Intégration des données de pays via une API.
- Amélioration de l'interface PAM pour la gestion de l'équipage des missions.
- Correction de l'ordre des options dans les radios multiples (MultiRadio) pour les Fish [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033).
- Correction d'un bug empêchant la suppression d'une infraction sur les Fish Controls [#1461](https://github.com/MTES-MCT/rapportnav2/issues/1461).
- Correction d'un bug concernant la sauvegarde des données Sati.

### Évolutions techniques
- Optimisation des performances lors du calcul du statut des actions en utilisant les données en mémoire plutôt que des requêtes répétées à la base de données.
- Amélioration des performances des requêtes sur les infractions et les contrôles grâce à l'utilisation de `@BatchSize`.
- Mise à jour de la version de Spring Boot vers la 4.1.0.
- Utilisation de mocks dans les tests pour améliorer la fiabilité et la rapidité.
- Nettoyage de fichiers backend inutiles.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Correction de règles de validation.
- Correction de problèmes de dépendances.
- Prévention de la duplication des informations générales et des cibles.
- Mise à jour des librairies frontend.
- Intégration des modifications de la branche `main` dans les branches de fonctionnalités.
