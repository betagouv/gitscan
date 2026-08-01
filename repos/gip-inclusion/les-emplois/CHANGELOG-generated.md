## Changelog : les-emplois (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'expérience utilisateur, notamment dans le parcours d'insertion et la gestion des utilisateurs. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'intégration avec Dora a été renforcée pour une meilleure synchronisation des données.

### Évolutions fonctionnelles
- Possibilité de rechercher un utilisateur par email directement.
- Synchronisation des statuts d'orientation depuis Dora via une tâche planifiée.
- Correction du filtre de recherche de demandeurs d'emploi dans l'interface d'insertion.
- Un utilisateur inactif ne peut plus être affecté comme dernier conseiller.
- Amélioration des performances de récupération du dernier conseiller.
- Suppression du formatage des prérequis pour les services DI.
- Nettoyage d'une méthode inutilisée dans l'application web.
- Limitation de la date de début de contrat pour les GEIQ, avec ajout d'explications.
- Ouverture automatique de l'info-bulle sur les dates de contrat pour les GEIQ.
- Correction de requêtes N+1 dans la liste des demandeurs d'emploi.
- Ajout de support pour le rendu de markdown en ligne dans les templates.
- Affichage du dernier accompagnateur connu au lieu du référent GPS.
- Ajout de boutons pour afficher les informations de contact du dernier accompagnateur.
- Ajout d'une action "auto-affectation" pour les conseillers.
- Correction de l'affichage des communes dans l'application ASP.
- Ajout d'un mécanisme de demande de rôle administrateur par email.
- Ajout d'un email automatique pour les nouveaux administrateurs d'organisation.
- Amélioration de l'affichage des pourcentages dans le formulaire.
- Ajout de la possibilité de s'auto-affecter comme conseiller.
- Ajout d'une nouvelle colonne pour les applications d'emploi dans le pilotage.
- Ajout d'une fonctionnalité pour désactiver automatiquement les candidatures spontanées après 90 jours.
- Ajout d'un modèle d'email pour la désactivation des candidatures spontanées.
- Ajout d'une tâche cron pour désactiver les candidatures spontanées dans les entreprises inactives.
- Correction de l'affichage des heures d'ouverture.
- Mise à jour des liens de déclaration d'accessibilité.
- Amélioration des messages d'avertissement pour l'activation de l'authentification à deux facteurs.
- Correction de l'affichage des messages globaux lors de la configuration de l'authentification à deux facteurs.
- Ajout d'exemples d'applications d'authentification à deux facteurs.
- Suppression des URL obsolètes de déconnexion de FranceConnect.
- Amélioration du flux de déconnexion de FranceConnect.
- Suppression des autorisations de contournement pour les URL pro_connect.
- Simplification des autorisations.
- Suppression d'une redirection pour la connexion administrateur.
- Ajout de la prise en charge des orientations dans l'interface d'administration des utilisateurs.
- Ajout de la possibilité de lier l'iMER d'origine à l'orientation créée.
- Ajout d'une commande pour importer les orientations depuis un fichier d'export Dora.
- Ajout d'une fonctionnalité pour enregistrer les événements de mobilisation lors de l'orientation.

### Évolutions techniques
- Refactor de la synchronisation des statuts d'orientation depuis Dora.
- Utilisation de NamedTuple pour améliorer la lisibilité du code.
- Correction de bugs liés à la synchronisation des statuts d'orientation depuis Dora.
- Mise à jour de la version de Huey.
- Mise à jour de plusieurs dépendances (Django, Pandas, etc.).
- Correction de problèmes de cache dans les actions CI/CD.
- Amélioration de la configuration des buckets MinIO.
- Correction de tests flaky.
- Ajout de tests unitaires.
- Amélioration de la gestion des erreurs.
- Suppression de code mort.
- Refactor de la gestion des autorisations.

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes de frappe dans les messages utilisateur.
- Amélioration des logs.
- Correction de problèmes de compatibilité avec différentes versions de Python.
- Suppression de configurations obsolètes.
- Ajout de commentaires pour améliorer la lisibilité du code.
- Mise à jour des URLs SIRENE.
- Suppression de l'affichage en liste des résultats.
- Correction de la configuration des tâches cron.
- Amélioration de la gestion des erreurs dans les tests.
