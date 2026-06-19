## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 18 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la plateforme, notamment en termes de performance, de sécurité et d'expérience utilisateur. Des corrections de bugs ont été apportées, ainsi que des optimisations pour l'export de données, la gestion des attestations et des procédures. L'équipe a également continué à moderniser le code et à améliorer la couverture de tests.

### Évolutions fonctionnelles
- Ajout d'un système de bannières administrables pour communiquer des informations importantes aux utilisateurs.
- Amélioration de l'expérience utilisateur lors de la correction de demandes, avec des messages d'erreur plus clairs.
- Possibilité de filtrer les opérations en lot sur les instructeurs en fonction de leur statut de suivi.
- Amélioration de l'affichage des informations sur les procédures dans l'interface d'administration.
- Ajout de la possibilité de pré-remplir certains champs de formulaire avec des données externes.
- Amélioration de la gestion des pièces justificatives et de leur affichage.
- Ajout d'un indicateur visuel pour les dossiers en construction proches de l'expiration.
- Amélioration de la gestion des groupes d'instructeurs.
- Ajout de la possibilité de gérer les champs de type "commune" et de les convertir en texte.
- Ajout de la possibilité de gérer les champs de type "adresse" dans les exports.
- Amélioration de l'affichage des informations sur les procédures dans l'interface d'administration.
- Ajout du support pour ProConnect pour les procédures de type moral.
- Ajout de la possibilité de gérer les champs de type "adresse" avec des données externes (BAN).
- Ajout d'un bouton ProConnect sur la page de connexion pour les professionnels.

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Rails, Sentry, etc.).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Optimisation des performances de l'export de données, notamment en utilisant le streaming.
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Amélioration de la couverture de tests.
- Migration de composants HAML vers ERB pour une meilleure maintenabilité.
- Amélioration de la sécurité, notamment en corrigeant des vulnérabilités potentielles dans l'import CSV.
- Ajout de circuit breakers pour l'API Entreprise afin d'améliorer la résilience.
- Implémentation d'un système de rate limiting pour l'API Entreprise.
- Amélioration de la gestion des jobs asynchrones (Sidekiq).
- Utilisation de Redis pour la mise en cache de la configuration OIDC.
- Amélioration de la gestion des erreurs dans les jobs.
- Refactorisation de la gestion des notifications.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de linting.
- Amélioration des messages de log.
- Suppression de code obsolète.
- Amélioration de l'accessibilité de l'interface utilisateur.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de bugs mineurs.
- Amélioration de la gestion des erreurs dans l'interface utilisateur.
- Ajout de commentaires pour améliorer la compréhension du code.
- Amélioration de la gestion des dates et des heures.
- Correction de problèmes de typographie.
- Amélioration de la gestion des traductions.
- Correction de problèmes d'affichage.
- Amélioration de la gestion des images.
- Correction de problèmes de sécurité.
- Amélioration de la gestion des fichiers.
- Correction de problèmes de performance.
- Amélioration de la gestion des utilisateurs.
- Correction de problèmes de compatibilité.
- Amélioration de la gestion des permissions.
- Correction de problèmes de configuration.
- Amélioration de la gestion des logs.
- Correction de problèmes de déploiement.
- Amélioration de la gestion des dépendances.
- Correction de problèmes de build.
- Amélioration de la gestion des tests.
- Correction de problèmes de documentation.
- Amélioration de la gestion des assets.
- Correction de problèmes de CSS.
- Amélioration de la gestion des formulaires.
- Correction de problèmes de JavaScript.
- Amélioration de la gestion des API.
- Correction de problèmes de base de données.
- Amélioration de la gestion des emails.
- Correction de problèmes de sécurité.
- Amélioration de la gestion des notifications.
- Correction de problèmes de performance.
- Amélioration de la gestion des erreurs.
- Correction de problèmes d'accessibilité.
- Amélioration de la gestion des traductions.
- Correction de problèmes de compatibilité.
- Amélioration de la gestion des permissions.
- Correction de problèmes de configuration.
- Amélioration de la gestion des logs.
- Correction de problèmes de déploiement.
- Amélioration de la gestion des dépendances.
- Correction de problèmes de build.
- Amélioration de la gestion des tests.
- Correction de problèmes de documentation.
- Amélioration de la gestion des assets.
- Correction de problèmes de CSS.
- Amélioration de la gestion des formulaires.
- Correction de problèmes de JavaScript.
- Amélioration de la gestion des API.
- Correction de problèmes de base de données.
- Amélioration de la gestion des emails.
- Correction de problèmes de sécurité.
- Amélioration de la gestion des notifications.
- Correction de problèmes de performance.
- Amélioration de la gestion des erreurs.
- Correction de problèmes d'accessibilité.
- Amélioration de la gestion des traductions.
- Correction de problèmes de compatibilité.
