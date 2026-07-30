## Changelog : les-emplois (30 derniers jours, au 2026-07-29)

### Résumé
Les dernières mises à jour de "les-emplois" se concentrent sur l'amélioration de l'expérience utilisateur lors de l'orientation des candidats, notamment en affinant la gestion des dates de contrat, en clarifiant les informations affichées et en corrigeant des problèmes de performance. Des améliorations significatives ont également été apportées à la sécurité, en particulier concernant l'authentification à deux facteurs (2FA) et la gestion des accès. Enfin, des corrections et des refactorisations techniques ont été effectuées pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration de l'interface de saisie des dates de contrat lors de l'application, avec des informations contextuelles et une validation plus précise.
- Affichage du dernier accompagnateur connu pour les demandeurs d'emploi, remplaçant l'ancien référent GPS.
- Ajout de boutons pour assigner un utilisateur à un accompagnement et afficher les informations de contact de l'accompagnateur.
- Amélioration de l'affichage des services et des structures lors de l'orientation, avec notamment l'ajout d'une carte pour visualiser les solutions recommandées (SPS).
- Correction de l'affichage des conditions d'orientation et des informations sur les services DI.
- Possibilité de rechercher des services directement via l'application, sans passer par l'API data-inclusion.
- Ajout d'un mécanisme de demande de rôle administrateur par email.
- Amélioration de la gestion des alertes et des messages d'information pour les utilisateurs.
- Ajout d'une commande pour importer les orientations depuis un fichier d'export Dora.

### Évolutions techniques
- Optimisation des requêtes SQL pour améliorer la performance de l'affichage des demandeurs d'emploi (correction de requêtes 1+N).
- Refactorisation du code lié à l'authentification FranceConnect et à la gestion des accès.
- Mise à jour de plusieurs dépendances, notamment Django, Django-HTMX, et les librairies de sécurité.
- Amélioration de la gestion des erreurs et des logs.
- Correction de tests unitaires et ajout de nouveaux tests pour garantir la qualité du code.
- Suppression de code obsolète et refactorisation de certaines parties du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la configuration des buckets MinIO pour les environnements de test et de développement.

### Autres changements
- Mise à jour de la documentation et des commentaires dans le code.
- Correction de liens et de références obsolètes.
- Amélioration de la gestion des configurations et des variables d'environnement.
- Correction de problèmes mineurs d'interface utilisateur et d'accessibilité.
- Mise à jour des URLs et des noms de modèles liés à l'ancien module PE Connect (Pole Emploi Connect).
