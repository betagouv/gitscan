## Changelog : recommandations-collaboratives (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des ressources, des projets et des documents, ainsi que sur la correction de bugs et l'optimisation des performances. Des améliorations significatives ont été apportées à l'interface utilisateur, notamment au niveau des filtres et des formulaires. Des corrections ont également été apportées concernant la gestion des RGPD et des notifications.

### Évolutions fonctionnelles
- Amélioration de la gestion des ressources : ajout de filtres par département et catégorie (#1830, #1861).
- Refonte du formulaire d'édition des ressources avec validation améliorée et gestion des organisations (#1870, #1875).
- Ajout d'un bouton pour créer une nouvelle ressource directement depuis la liste des ressources.
- Amélioration de l'affichage des projets dans la liste, avec une meilleure gestion du texte long.
- Ajout de la possibilité de supprimer les comptes utilisateurs avec une notification RGPD (#1891, #1896).
- Amélioration de l'affichage des titres et des informations des projets.
- Ajout d'une alerte de déconnexion pour éviter la perte de données en cas de fermeture de l'onglet (#1874).
- Suppression de l'ancien tutoriel.
- Mise à jour de l'affichage de la page d'accueil Sospont.
- Amélioration de la gestion des commentaires sur les tâches.
- Ajout de la possibilité de prévisualiser l'email du propriétaire avant de le soumettre.

### Évolutions techniques
- Refactorisation de l'API pour la gestion des ressources.
- Optimisation des performances de la recherche de ressources.
- Mise à jour des dépendances (sqlparse, cryptography, axios, nbconvert, wagtail).
- Amélioration de la gestion des erreurs et des validations dans les formulaires.
- Utilisation de Django forms pour le formulaire de ressources.
- Suppression du code obsolète lié au tagging des tâches.
- Amélioration de la gestion des erreurs Sentry.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Mise en place de tests unitaires et d'intégration.
- Optimisation de la gestion des données en cache.

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs dans l'interface utilisateur.
- Amélioration de la gestion des fichiers et des documents.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de la sécurité de l'application.
- Correction de problèmes de performance.
- Amélioration de la gestion des logs et du monitoring.
- Mise à jour des messages d'erreur pour une meilleure clarté.
- Amélioration de l'accessibilité de l'application.
