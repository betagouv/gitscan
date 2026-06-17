## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 18 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité (désactivation de l'authentification OTP legacy pour les super-admins, correction d'une vulnérabilité), des optimisations de performance (optimisation des requêtes N+1, refactoring de l'API Entreprise avec gestion des erreurs améliorée), et des corrections de bugs (problèmes d'affichage, erreurs de validation, etc.). De nombreuses mises à jour de dépendances ont également été effectuées. Des améliorations de l'expérience utilisateur ont été apportées, notamment au niveau de l'éditeur de formulaire et des bannières d'information.

### Évolutions fonctionnelles
- Ajout de bannières d'information administrables avec une interface utilisateur dédiée.
- Amélioration de l'interface utilisateur pour la gestion des pièces justificatives (LDUP).
- Possibilité de préremplir des champs avec des données externes (adresse, civilité) via l'API.
- Ajout de la gestion du champ "naf_2025" pour les établissements.
- Amélioration de l'affichage des informations de contact dans l'interface d'administration.
- Ajout de la possibilité de masquer/afficher des champs en fonction de la valeur d'autres champs (conditions).
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout d'un système de gestion des notifications pour les administrateurs.
- Possibilité de publier ou de dépublier des démarches.
- Amélioration de la gestion des utilisateurs et des rôles.
- Ajout de la possibilité de transférer des dossiers.

### Évolutions techniques
- Refactoring de l'API Entreprise avec gestion des erreurs basée sur des monades `Dry::Monads Result`.
- Optimisation des requêtes SQL pour améliorer les performances.
- Mise à jour de nombreuses dépendances (RubyGems).
- Migration de composants HAML vers ERB pour une meilleure maintenabilité.
- Amélioration de la gestion des jobs asynchrones (Sidekiq).
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la sécurité en supprimant l'authentification OTP legacy pour les super-admins.
- Correction d'une vulnérabilité potentielle dans la gestion des champs de formulaire.
- Amélioration de la gestion des erreurs et des exceptions.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des configurations.
- Mise en place d'un système de cache pour améliorer les performances.
- Amélioration de la gestion des logs.
- Ajout de métriques pour le monitoring de l'application.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de linting et de style de code.
- Amélioration de la gestion des traductions.
- Suppression de code obsolète.
- Nettoyage du code.
- Amélioration de la gestion des tests.
- Correction de bugs mineurs.
- Ajout de commentaires pour améliorer la compréhension du code.
- Refactoring de certaines parties du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests pour les nouvelles fonctionnalités.
