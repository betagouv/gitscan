## Changelog : les-emplois (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'expérience utilisateur dans le parcours d'insertion, notamment concernant la recherche de services et la gestion des orientations. Des corrections et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. La sécurité a été renforcée avec des améliorations concernant l'authentification et la gestion des accès.

### Évolutions fonctionnelles
- Possibilité de rechercher un utilisateur par email directement.
- Synchronisation des statuts d'orientation depuis Dora via une tâche planifiée.
- Correction du filtre de recherche de demandeurs d'emploi dans le formulaire de sélection d'orientation.
- Un utilisateur inactif ne peut plus être affecté comme dernier accompagnateur.
- Amélioration des performances de récupération du dernier accompagnateur.
- Suppression du formatage des prérequis pour les services DI.
- Nettoyage d'une méthode inutilisée dans l'application web.
- Limitation de la date de début de contrat pour les GEIQ, avec ajout d'explications.
- Ouverture automatique des informations sur les dates de contrat pour les GEIQ.
- Le champ "date de début de contrat" est désormais obligatoire.
- Correction d'erreurs 1+N dans la liste des demandeurs d'emploi.
- Ajout du support du rendu Markdown en ligne dans les templates.
- Correction de l'affichage des pourcentages dans le formulaire.
- Mise à jour de la liste des demandeurs d'emploi.
- Ajout d'une nouvelle colonne pour les candidatures dans le pilotage.
- Possibilité de supprimer des fichiers inutilisés par lot.
- Amélioration du flux de déconnexion FranceConnect.
- Ajout d'un identifiant de secteur pour FranceConnect.
- Définition du genre de l'utilisateur pour FranceConnect.
- Suppression d'URL obsolètes pour FranceConnect.
- Simplification de la gestion des autorisations.
- Amélioration de la gestion des autorisations pour l'administration.
- Ajout de la gestion des orientations (modèle, admin, migration, synchronisation avec Dora).
- Possibilité d'assigner soi-même en tant que dernier accompagnateur.
- Ajout d'un message d'avertissement pour les utilisateurs professionnels concernant l'activation de l'authentification multi-facteurs.
- Amélioration de la clarté des messages liés à l'authentification multi-facteurs.
- Ajout de liens vers des exemples d'applications d'authentification.
- Suppression des URL obsolètes.
- Amélioration de la gestion des erreurs et des messages d'information.
- Renommage de l'application PE Connect en FranceConnect.
- Mise à jour des URLs et des templates liés à FranceConnect.
- Ajout de la possibilité de demander un rôle d'administrateur par email.
- Ajout d'un email automatique pour les nouveaux administrateurs d'organisation.

### Évolutions techniques
- Mise à jour de la version de Huey.
- Refactorisation du code de synchronisation des statuts d'orientation.
- Utilisation de NamedTuple pour améliorer la lisibilité du code.
- Correction d'une erreur de traduction.
- Déplacement de la tâche de synchronisation des statuts d'orientation.
- Correction d'un crash lors de la synchronisation des statuts d'orientation avec Dora.
- Correction d'un bug lié à l'affichage des heures d'ouverture.
- Amélioration de la gestion des fichiers.
- Mise à jour des dépendances (Django, djlint, etc.).
- Optimisation des requêtes SQL.
- Amélioration de la gestion des erreurs.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes de frappe.
- Ajout de commentaires.
- Amélioration des tests.
- Mise à jour des configurations.
- Suppression de code inutile.
