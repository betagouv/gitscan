## Changelog : recommandations-collaboratives (30 derniers jours, au 2026-03-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau de la gestion des ressources et des projets, ainsi que sur la correction de bugs et l'amélioration de la robustesse de l'application. Des améliorations ont également été apportées à la gestion des notifications et des traces, et à la sécurité (RGPD).

### Évolutions fonctionnelles
- Amélioration de l'affichage du nom du projet dans le menu supérieur.
- Ajout d'une fonctionnalité de duplication de ressources.
- Possibilité de promouvoir un membre en tant qu'advisor.
- Ajout d'un indicateur visuel pour les recommandations sans ressource associée.
- Amélioration de l'affichage des messages et des réponses dans les conversations.
- Ajout de la possibilité de filtrer les projets par date dans l'administration.
- Amélioration de la gestion des notifications et des traces, avec des informations plus précises sur les actions des utilisateurs.
- Correction d'un bug empêchant l'affichage correct des breadcrumbs.
- Ajout d'un bouton pour supprimer un filtre de temps sur les projets.
- Amélioration de la gestion des erreurs lors de la soumission du formulaire de ressource.
- Ajout d'un indicateur visuel pour les alertes de départ (on leave).

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Optimisation des performances de la liste des projets dans l'administration.
- Mise à jour des dépendances : Django Allauth, Wagtail, sqlparse, cryptography, axios, nbconvert, pillow.
- Amélioration du système de CI/CD pour séparer les étapes de build et de test.
- Correction de problèmes liés à la gestion des permissions et des groupes d'utilisateurs.
- Amélioration de la gestion des erreurs et des exceptions.
- Amélioration de la gestion des erreurs liées à l'envoi d'emails (RGPD).
- Mise en place d'un système de logging plus précis pour faciliter le débogage.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de code obsolète.
- Correction de typos et amélioration de la qualité du code.
- Amélioration des tests unitaires et d'intégration.
- Ajout de commentaires pour faciliter la compréhension du code.
- Correction de problèmes de style et d'accessibilité.
- Mise à jour de la configuration de l'application.
- Correction d'un problème lié à l'affichage des avatars (Gravatar).
- Amélioration de la gestion des erreurs Sentry.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de bugs mineurs.
