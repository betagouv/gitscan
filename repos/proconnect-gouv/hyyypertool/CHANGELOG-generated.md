## Changelog : hyyypertool (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, de l'expérience utilisateur et de la robustesse de Hyyypertool. Les principales améliorations incluent l'ajout d'un système de limitation du débit par adresse IP pour se protéger contre les abus, l'implémentation du tri des colonnes dans la liste des modérations pour une meilleure organisation des données, et l'introduction d'un mode sombre pour une utilisation plus confortable. Des corrections de bugs et des optimisations ont également été apportées.

### Évolutions fonctionnelles
- Ajout du tri des colonnes dans la liste des modérations, permettant de classer les données par différents critères.
- Implémentation d'un mode sombre pour une meilleure lisibilité et une expérience utilisateur plus agréable.
- Possibilité de filtrer les modérations par statut de décision (acceptées, rejetées, réouvertes).
- Ajout de la possibilité de supprimer les modèles de réponse directement depuis l'interface.
- Amélioration de l'interface utilisateur suite à la suppression de DSFR, notamment pour les menus et les boutons.
- Correction d'un bug qui affichait un message d'erreur incorrect en cas de jeton API expiré.
- Correction de l'affichage du menu "trois points" en mode sombre.
- Suppression de l'affichage du nom et prénom dans les emails de rejet.

### Évolutions techniques
- Implémentation d'une limitation du débit par adresse IP pour protéger l'application contre les attaques et les abus.
- Remplacement des mocks basés sur MockServer par des routes Hono pour simplifier le développement et les tests.
- Clarification de l'ordre de tri par défaut dans la recherche de modérations.
- Amélioration de la gestion du nonce pour la sécurité des requêtes.
- Mise à jour et correction de plusieurs dépendances.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités.
- Nettoyage du code et suppression de code obsolète.
- Amélioration de la configuration et des scripts de déploiement.
- Correction de bugs mineurs et améliorations de la stabilité.
