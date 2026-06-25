## Changelog : mon-service-securise (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'administration des utilisateurs et des organisations, avec l'ajout de nouvelles fonctionnalités pour les administrateurs et superviseurs, ainsi que des améliorations de l'accessibilité et de la sécurité. Des corrections et optimisations techniques ont également été apportées pour améliorer la stabilité et la performance du service.

### Évolutions fonctionnelles
- Ajout d'une page dédiée à la gestion des administrateurs et superviseurs, accessible via un nouveau menu dans l'interface.
- Possibilité pour un administrateur de nommer d'autres administrateurs sur des entités spécifiques, avec gestion des permissions et des rôles.
- Affichage des entités sur lesquelles un utilisateur est administrateur ou superviseur.
- Amélioration de l'affichage des risques v2 avec un tiroir permettant de modifier la gravité.
- Ajout d'une recherche sur les pages d'administration.
- Affichage des statistiques de supervision.
- Possibilité de surcharger la gravité d'un risque général V2 via l'API.
- Ajout de tableaux par thématique pour une meilleure organisation des informations.
- Affichage du récapitulatif des modifications lors de l'attribution de rôles.
- Ajout d'une page listant les utilisateurs administrés.
- Amélioration de l'affichage des informations sur les services et les entités.

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Vitest, Playwright, Prettier, Knex, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Renforcement de la sécurité avec la mise à jour de Vite et de Multer, corrigeant des vulnérabilités.
- Amélioration de la configuration Knex pour éviter les duplications.
- Ajout de tests d'accessibilité pour les pages d'administration et les tiroirs.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests unitaires et d'intégration.
- Utilisation de zizmor pour valider la configuration.
- Implémentation d'un adaptateur de persistance mémoire pour les tests d'accessibilité.
- Ajout de logs d'audit pour les actions d'administration (attribution de rôles, suppression d'accès).
- Amélioration du tracking Matomo pour une meilleure analyse de l'utilisation du service.

### Autres changements
- Suppression de code obsolète et de configurations inutiles.
- Amélioration de la documentation.
- Correction de problèmes d'accessibilité (couleurs, contrastes, labels).
- Ajout d'un fichier `robots.txt` et mise à jour du sitemap.
- Suppression de la page "activation".
- Ajout de règles ESLint pour améliorer la qualité du code.
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
- Suppression de l'attribut `setGenerationTimeMs`.
- Suppression du fil d'Ariane sur la page de statistiques de supervision.
- Ajout de titres cohérents sur les pages connectées.
