## Changelog : gestion-des-subventions-locales (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment sur les pages d'administration et de gestion des projets. Des corrections de bugs ont été implémentées pour améliorer la robustesse de l'application, en particulier lors de la mise à jour des données depuis la DN (Données Nationales) et de la gestion des simulations. De nouvelles fonctionnalités ont été ajoutées, comme la gestion des catégories DETR/DSIL et la possibilité de compléter les dossiers reportés sans pièces. La sécurité a également été renforcée avec l'ajout d'une protection contre les attaques par force brute.

### Évolutions fonctionnelles
- Ajout de la possibilité de compléter les dossiers reportés sans pièces (#496).
- Affichage du tag "Reporté" pour les projets issus d'une demande précédente (#484).
- Permettre de repasser un projet notifié en traitement (#480).
- Ajout des champs de détails des champs "Autre zonage local" et "Autre contrat local" (#481).
- Distinction dans l'affichage des infos ajoutées par le demandeur et celles ajoutées par l'instructeur sur la page projet (#482).
- Ajout du lien Tchap (#506).
- Ajout des catégories DETR/DSIL au formulaire dossier SANS pièces (#494).
- Ajout du nombre de projets dans les listes de projets (#495).
- Possibilité de modifier les données d'un Dossier via l'admin (#539).
- Ajout du code du département à la logique d'import d'Arrondissement (#541).
- Correction des erreurs 404 après actualisation DN ou changement dotation (#529).
- Ajout d'une tâche pour rafraichir tous les dossiers de toutes les démarches depuis DN (#538).
- Ajout d'une tâche pour rafraichir sur les dossiers d'une démarche depuis une date donnée (#533).
- Ajout des droits pour les utilisateurs "équipe" pour changer les périmètres des autres utilisateurs (#531).
- Ajout d'une protection contre les attaques par force brute (#524).
- Ajout de pages d'erreur 403, 404, 500 conformes au modèle DSFR (#528).
- Amélioration UI du formulaire de renseignement d'info pour un dossier reporté "sans" (#503).
- Ajout de colonnes dans la page liste des utilisateurs (BO) (#502).

### Évolutions techniques
- Refactorisation de la relation de Demarche, déplacée de DossierData vers Dossier (#536).
- Simplification de la modélisation : suppression de FieldMappingForHuman et nouveau nom de FieldMapping (#493).
- Utilisation de `django-axes` pour la protection contre les attaques par force brute (#523).
- Optimisation des performances des pages d'administration de Collegue et FieldMapping (#518).
- Optimisation des requêtes dans l'admin pour Collegue et FieldMapping (#518).
- Suppression de code mort (processModal.js) (#534, #11faeffb).
- Utilisation de `django-json-widget` (#66bca99a).
- Suppression de la connexion par username/mdp (#523).
- Suppression de colonnes inutiles sur la page Simulation (#517).
- Refactorisation de l'URL pour éviter les erreurs 404 (#539).
- Amélioration de la robustesse de l'algorithme de récupération des données d'un dossier DN (#501).
- Correction de la migration pour éviter les dépendances dupliquées (#520).
- Utilisation de `iterator()` pour optimiser la migration des dossiers (#488).
- Ajout de tests pour les fichiers générés (#520).
- Utilisation de `logger.exception` au lieu de `logger.error` (#520).

### Autres changements
- Correction du sélecteur de dotations dans la page simulation (#479).
- Correction d'un test (calcul de la taille d'un document généré) (#486).
- Renommage de l'onglet "Annotations" en "Notes" (#507).
- Correction pour accepter les taux supérieurs à 100% depuis les annotations DN (#513).
- Renommage des messages de succès des projets acceptés et refusés provisoirement (#516).
- Ajout d'une vidéo de démo sur la page d'aide (#526).
- Suppression de la suppression des dotations projets programmés (#521).
- Ajout de la récupération de l'assiette depuis DN peu importe le statut du dossier (#512).
- Correction de l'algo qui récupère les catégories DETR (#510).
- Ajout de la gestion des dossiers sans catégories DETR (#509).
- Empêcher de créer/supprimer/modifier les périmètres + faciliter la recherche d'un périmètre (#508).
- Ajout des dates de création et de modification sur Projet et DotationProjet (#504).
- MEP vendredi 06/02/26 (#514).
- Main backport (#490).
- Ajout d'une copie de la BDD de l'app parente pour la review app (#527).
- Suppression d'un historique de tab dans la section projet (#539).
- Redirection vers la liste des projets en cas de suppression de projet ou simulation (#539).
