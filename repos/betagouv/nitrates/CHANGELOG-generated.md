## Changelog : nitrates (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'importation et l'affichage de nouvelles données (zones vulnérables et zones protégées), ainsi que sur des améliorations de l'interface utilisateur et de la gestion des configurations pour les haies. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Importation des données de zones vulnérables (ZV) et de zones protégées (RPG) avec remplacement des labels codés en dur par une recherche serveur. [#17](https://github.com/betagouv/nitrates/pull/17)
- Affichage des contrôles de couches, des superpositions ZV+RPG et des couleurs ZV par bassin. [#2d965a30](https://github.com/betagouv/nitrates/commit/2d965a30)
- Ajout d'une vue de débogage de bout en bout (carte + cartouche + tests e2e). [#89317698](https://github.com/betagouv/nitrates/commit/89317698)
- Ajout de la possibilité de configurer l'affichage des informations de contact pour les haies.
- Amélioration du fallback pour l'affichage des informations de contact.
- Ajout d'une validation de la longueur maximale des haies, avec un message d'erreur configurable.
- Ajout d'une limite configurable de longueur maximale de haies (backend et frontend).
- Amélioration de l'affichage des résultats de la densité.
- Ajout de filtres et d'une barre de recherche pour la page de configuration.
- Ajout d'un bouton pour retirer une pièce jointe lors de l'upload.
- Correction de l'affichage du périmètre dans certaines vues.
- Ajout d'un indicateur visuel pour les zones sans contacts.

### Évolutions techniques
- Refactorisation du code pour la gestion des données Natura 2000 Haie, incluant l'ajout de tests et la simplification de la logique.
- Mise en place d'une infrastructure de tests e2e plus complète.
- Amélioration des performances des requêtes de densité.
- Optimisation du code pour éviter les calculs inutiles.
- Mise à jour de la configuration Docker pour l'architecture ARM64.
- Mise à jour des dépendances et correction de problèmes liés à l'environnement de développement.
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des configurations et des paramètres.

### Autres changements
- Mise à jour de la documentation.
- Correction de coquilles et d'erreurs de typographie.
- Amélioration de la sécurité (correction d'une potentielle vulnérabilité XSS).
- Suppression de code inutile et nettoyage du code.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des messages d'erreur pour une meilleure clarté.
- Migration de la FAQ utilisateur vers Gitbook.
- Ajout de métriques d'analytics pour suivre l'utilisation de l'application.
- Amélioration de la gestion des erreurs Sentry.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
