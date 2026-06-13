## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de performance, des corrections de sécurité, des refactorings importants pour préparer l'évolution de l'application, et des améliorations de l'expérience utilisateur, notamment au niveau de l'administration et de la gestion des procédures. L'intégration de ProConnect a également été avancée.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter des sauts de page dans l'éditeur d'attestations v2.
- Amélioration de l'affichage des informations sur les champs dans l'exportation des données.
- Amélioration de l'expérience utilisateur pour les opérations en lot (batch) dans l'interface administrateur, avec affichage des messages d'erreur et une meilleure gestion des alertes.
- Ajout d'un bouton ProConnect pour les professionnels lors de la connexion.
- Amélioration de l'affichage des informations sur les procédures dans l'interface administrateur.
- Possibilité de filtrer les instructeurs par statut.
- Correction d'un bug empêchant l'affichage correct des champs de type "liste déroulante multiple".
- Amélioration de la gestion des erreurs lors de l'importation de fichiers CSV.
- Correction d'un problème d'affichage des commentaires sur la page "Mon Avis".
- Ajout d'une indication visuelle pour les champs modifiés dans l'éditeur administrateur.
- Amélioration de la gestion des erreurs lors de la soumission de formulaires.
- Correction d'un bug lié à l'expiration des dossiers en construction.

### Évolutions techniques
- Refactorings importants pour migrer vers API Entreprise v4, incluant la gestion des données d'établissement et l'extraction du NAF 2025.
- Mise à jour de nombreuses dépendances, incluant Puma, rubocop, et diverses bibliothèques Ruby.
- Amélioration de la performance des requêtes, notamment pour l'affichage des procédures et des avis.
- Optimisation du code pour réduire les requêtes N+1.
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Mise en place de tests plus complets et fiables.
- Utilisation de monades `Dry::Monads` pour une meilleure gestion des erreurs dans l'API Entreprise.
- Migration de composants HAML vers ERB pour une meilleure maintenabilité.
- Amélioration de la gestion des configurations OIDC pour FranceConnect et ProConnect.
- Refactorisation du code pour une meilleure séparation des préoccupations et une plus grande modularité.
- Amélioration de la gestion des tâches asynchrones avec Sidekiq.
- Ajout de circuit breakers pour l'API Entreprise.
- Mise en place de tâches de maintenance pour la suppression des dossiers abandonnés.

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Correction de problèmes de linting et de style de code.
- Mise à jour des traductions.
- Amélioration de la sécurité de l'application, notamment en corrigeant des vulnérabilités potentielles.
- Ajout de tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Amélioration de la gestion des logs et du monitoring.
- Suppression de code obsolète.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes de performance.
- Amélioration de la sécurité de l'application.
- Mise à jour de la documentation.
- Amélioration de la lisibilité et de la maintenabilité du code.
