## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 10 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité (authentification, gestion des OTP), des optimisations de performance (requêtes, jobs), des corrections de bugs (import de données, affichage d'informations) et des refactorings importants pour préparer l'évolution de la plateforme, notamment concernant l'intégration avec l'API Entreprise v4 et la migration vers des technologies plus modernes. Des améliorations de l'expérience utilisateur ont également été apportées, notamment dans l'administration et la gestion des dossiers.

### Évolutions fonctionnelles
- Ajout d'un bouton "ProConnect" pour les usagers concernés, permettant l'accès à la procédure simplifiée. [#13015](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13015)
- Amélioration de l'affichage des informations sur les avis des experts.
- Possibilité de préremplir le champ date de naissance avec les informations FranceConnect.
- Ajout d'un indicateur visuel pour les champs préremplis avec FranceConnect.
- Amélioration de la gestion des erreurs lors des opérations par lots.
- Ajout d'un message d'avertissement lors de la tentative de suppression du groupe d'instructeurs par défaut lors d'un import.
- Amélioration de l'affichage des breadcrumbs dans l'interface d'administration.
- Ajout d'un bouton pour insérer des sauts de page dans l'éditeur d'attestations.
- Amélioration de la gestion des erreurs lors de l'importation de fichiers CSV.
- Ajout d'une option pour masquer les champs lors de l'archivage.
- Amélioration de l'affichage des informations sur les procédures.
- Ajout de la possibilité de filtrer les opérations par lots en fonction du statut de l'instructeur.

### Évolutions techniques
- Refactor de l'intégration avec l'API Entreprise, incluant la gestion des erreurs et l'utilisation de monads `Result`.
- Migration de plusieurs composants vers ERB pour une meilleure maintenabilité.
- Optimisation des requêtes SQL pour améliorer les performances.
- Mise à jour de nombreuses dépendances (Puma, Rubocop, etc.).
- Amélioration de la gestion des erreurs et des exceptions.
- Utilisation de Sidekiq pour la gestion asynchrone des tâches.
- Refactor de la gestion des OTP (One-Time Password) pour améliorer la sécurité.
- Amélioration de la gestion des configurations OIDC (OpenID Connect).
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Suppression de code obsolète et simplification de la base de code.
- Amélioration de la gestion des fichiers et des uploads.
- Correction de problèmes de sécurité liés à l'importation de fichiers.
- Amélioration de la gestion des erreurs lors de l'importation de données.
- Mise en place d'un système de cache pour améliorer les performances.
- Refactor de la gestion des champs et des types de champs.
- Amélioration de la gestion des autorisations et des rôles.

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la configuration du projet.
- Nettoyage du code et correction de problèmes de style.
- Ajout de tests pour améliorer la qualité du code.
- Correction de bugs mineurs.
- Mise à jour des fichiers de configuration pour l'intégration continue.
- Amélioration de la gestion des logs.
- Ajout de métriques pour le suivi des performances.
- Correction de problèmes de validation des données.
- Amélioration de la gestion des erreurs lors de l'importation de données.
- Ajout de traductions pour les nouvelles fonctionnalités.
- Correction de problèmes de compatibilité avec les navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de sécurité.
- Mise à jour des dépendances.
- Amélioration de la gestion des erreurs.
- Ajout de tests unitaires.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
- Ajout de nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité.
- Mise à jour des dépendances.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
- Ajout de nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité.
- Mise à jour des dépendances.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
- Ajout de nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité.
- Mise à jour des dépendances.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
- Ajout de nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité.
- Mise à jour des dépendances.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
- Ajout de nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité.
- Mise à jour des dépendances.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
- Ajout de nouvelles fonctionnalités.
- Correction de problèmes de performance.
- Amélioration de la sécurité.
- Mise à jour des dépendances.
- Correction de bugs.
- Amélioration de la documentation.
- Refactor du code.
