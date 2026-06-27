## Changelog : mon-service-securise (30 derniers jours, au 26 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur et de l'expérience administrateur, notamment avec la refonte de la gestion des utilisateurs et des permissions. Des corrections d'accessibilité ont également été apportées, ainsi que des optimisations de sécurité et de maintenance technique. L'ajout de nouvelles fonctionnalités pour la gestion des risques v2 et l'amélioration du suivi des événements sont également notables.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des risques v2 : affichage des descriptions et exemples, modification du niveau de gravité, affichage cohérent en lecture seule.
- Ajout d'une page dédiée à la gestion des administrateurs et superviseurs, incluant la recherche, la gestion des permissions et l'attribution de rôles.
- Possibilité de nommer un administrateur sur un périmètre complet.
- Affichage des actions de suppression et d'attribution de rôles pour les utilisateurs administrés.
- Ajout d'une fonctionnalité permettant de retirer l'accès d'un utilisateur à des services.
- Amélioration de l'affichage des entités et des services associés à un utilisateur.
- Ajout d'un fil d'Ariane plus précis sur certaines pages.
- Affichage des statistiques de supervision.
- Ajout d'un tableau de bord spécifique pour les administrateurs et superviseurs.
- Affichage des badges d'administrateur sur la liste des utilisateurs.
- Amélioration de l'affichage des matrices de risque v2.
- Ajout d'une page "Conseils cyber" utilisant des composants DSFR.

### Évolutions techniques
- Mise à jour de nombreuses dépendances (axios, @tiptap, vite, svelte, etc.).
- Amélioration de la configuration Knex et simplification de la connexion à la base de données.
- Ajout de tests d'accessibilité et corrections associées.
- Implémentation d'un adaptateur de persistance mémoire pour les tests d'accessibilité.
- Ajout d'un système de journalisation des événements (audit) pour les actions d'administration.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Ajout de règles ESLint pour améliorer la qualité du code.
- Amélioration de la sécurité en désactivant les identifiants git dans les actions CI/CD et en mettant à jour des dépendances vulnérables (multer, vite, svelte).
- Ajout d'un fichier `robots.txt` et d'un sitemap pour améliorer le référencement.
- Utilisation de zizmor pour valider la configuration.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de contraste et d'accessibilité.
- Amélioration de l'affichage des messages et des infobulles.
- Suppression de code obsolète.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs.
- Suppression de code inutile.
- Uniformisation de certains composants et styles.
- Ajout de variables d'environnement pour la configuration.
- Amélioration de la gestion des secrets.
- Ajout de la possibilité de suivre la navigation dans la SPA avec Matomo.
