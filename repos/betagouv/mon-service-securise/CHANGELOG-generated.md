## Changelog : mon-service-securise (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des administrateurs et de leurs accès, notamment en introduisant un nouveau système pour la gestion des organisations et des superviseurs. Des corrections d'accessibilité et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de nommer un administrateur sur un périmètre complet.
- Implémentation de la suppression d'un administrateur et de ses accès.
- Ajout de la gestion des autorisations (rôles) pour les utilisateurs administrés.
- Amélioration de l'interface pour la sélection des entités administrées, avec la possibilité de sélectionner toutes les entités.
- Affichage du nombre de services et d'utilisateurs par entité supervisée.
- Ajout d'une action pour retirer les accès d'un utilisateur administré à des services.
- Possibilité d'attribuer un rôle à un utilisateur administré.
- Affichage d'une alerte si un administrateur est le seul propriétaire d'un service.
- Ajout d'une fonctionnalité permettant de vérifier l'adresse email d'un administrateur.
- Ajout d'un tiroir d'invitation d'administrateurs.
- Affichage des administrateurs du périmètre du superviseur.

### Évolutions techniques
- Refonte de la gestion des superviseurs avec un nouveau dépôt de données OO.
- Migration de la gestion des admins d'organisations vers un nouveau dépôt.
- Simplification de la configuration Knex avec un singleton.
- Amélioration de la gestion des erreurs et des types dans le code.
- Mise à jour de l'UI Kit.
- Utilisation de composants DSFR pour la page conseils cyber.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la gestion des événements sur le bus de messages.
- Suppression de code obsolète et simplification de la logique existante.
- Mise à jour de la dépendance `axios` vers la version 1.16.0.

### Autres changements
- Corrections d'accessibilité sur plusieurs pages (statistiques, CGU, mentions légales, activation, connexion, création de service, etc.).
- Amélioration de la documentation et des commentaires dans le code.
- Correction de problèmes de linting et de formatage du code.
- Ajout de rapports d'accessibilité pour les pages testées.
- Correction de liens et d'URLs incorrects.
- Ajout d'un script pour faciliter la mise à jour de l'UI Kit.
- Ajout d'un système de logs pour les événements importants.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'un mécanisme de cache pour améliorer les performances.
