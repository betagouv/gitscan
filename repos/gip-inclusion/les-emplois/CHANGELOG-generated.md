## Changelog : les-emplois (30 derniers jours, au 2026-07-24)

### Résumé
Cette version apporte des améliorations significatives à la gestion de l'authentification FranceConnect et Pôle Emploi Connect, avec une refactorisation importante du code associé. Des corrections et des optimisations ont également été apportées à la gestion des fichiers, à l'interface utilisateur et aux tests. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur lors de la déconnexion avec FranceConnect, incluant un rappel de l'URL de retour.
- Ajout de la possibilité d'afficher les orientations dans l'interface d'administration des utilisateurs.
- Amélioration de l'affichage des informations de contact de l'accompagnateur pour les demandeurs d'emploi.
- Ajout de boutons pour assigner un conseiller ou s'auto-assigner à un demandeur d'emploi.
- Amélioration de l'affichage des heures d'ouverture et des prérequis des services.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Clarification des messages affichés après l'utilisation d'un code de récupération pour l'authentification à deux facteurs.
- Ajout d'un mécanisme de demande de rôle administrateur par email.
- Ajout d'un affichage des heures d'ouverture et des informations complémentaires des structures.
- Amélioration de la gestion des services et des structures lors de l'insertion.

### Évolutions techniques
- Refactorisation complète du code lié à Pôle Emploi Connect (renommage de variables, fonctions, modèles, templates, etc.) pour une meilleure cohérence et maintenabilité.
- Optimisation de la suppression des fichiers inutilisés en réduisant la taille des lots traités.
- Amélioration de la robustesse des tests et correction de tests flaky.
- Mise à jour de plusieurs dépendances, notamment `Django`, `pytest`, `MinIO`, `Docker`, `ruff`, `filelock`, `numpy`, et autres.
- Suppression de code obsolète et simplification de la logique dans certains modules.
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Mise à jour de la documentation et des liens d'accessibilité.
- Correction de bugs mineurs dans l'interface utilisateur.
- Amélioration de la gestion des configurations et des variables d'environnement.
- Suppression de code non utilisé.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Mise à jour des URLs SIRENE.
- Correction d'un bug dans le calcul du pourcentage d'attribution des évaluations GEIQ.
- Ajout d'une commande pour désactiver les offres d'emploi spontanées après une certaine période.
- Correction d'un bug lié à l'affichage des informations de contact des conseillers.
- Suppression d'une fonctionnalité de suppression des transferts d'enregistrements des employés.
- Correction d'un bug dans l'affichage des jours d'ouverture.
- Ajout de la possibilité de spécifier un identifiant URI pour le secteur d'activité dans FranceConnect.
- Ajout de la possibilité de définir le genre de l'utilisateur dans FranceConnect.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
- Ajout de la possibilité de définir des heures d'ouverture pour les structures.
- Correction d'un bug dans l'affichage des informations de contact des conseillers.
- Amélioration de la gestion des erreurs lors de la suppression de fichiers.
- Ajout de la possibilité de configurer des buckets MinIO distincts pour les tests et le développement.
- Ajout d'une gestion plus robuste des contraintes de validation des données.
- Ajout d'une alerte pour les utilisateurs professionnels concernant l'activation prochaine de l'authentification à deux facteurs.
- Correction d'un bug dans le test de l'ordre des périmètres de service.
