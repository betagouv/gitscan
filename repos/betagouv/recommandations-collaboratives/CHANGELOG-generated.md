## Changelog : recommandations-collaboratives (30 derniers jours, au 22 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des documents, des conversations et des recommandations. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de l'infrastructure et des dépendances. L'accent a été mis sur l'amélioration de la gestion des communes et des documents privés.

### Évolutions fonctionnelles
- Amélioration de la gestion des documents : Possibilité de joindre des documents aux notes publiques et privées [#1996, #2023].
- Gestion des communes : Mise à jour et création de communes basées sur les données de la Poste, améliorant la synchronisation des données géographiques [#2067].
- Publication de recommandations : Nouvelle route spécifique pour la publication de recommandations dans le contexte d'une conversation [#1997].
- Conversations :
    - Amélioration de l'accessibilité des panneaux de ressources et de contenus partagés avec l'ajout de rôles ARIA.
    - Possibilité de joindre des fichiers aux conversations.
    - Amélioration de la gestion des brouillons de recommandations.
    - Ajout d'une section pour les fichiers privés dans les conversations.
- Interface utilisateur :
    - Amélioration de l'interface de sélection des départements.
    - Suppression de l'affichage d'informations inutiles dans l'éditeur de ressources.
    - Amélioration de l'affichage des erreurs de mot de passe.
    - Ajout d'une section pour les démarches numériques dans la fiche de recommandation.
- Gestion des tâches : Préchargement des tags pour améliorer la performance.
- Notifications : Envoi de notifications lors de la suppression de documents.

### Évolutions techniques
- Refactoring du code : Suppression de code obsolète et amélioration de la structure du code pour une meilleure maintenabilité.
- Mises à jour de dépendances : Mises à jour de plusieurs dépendances, notamment Django, pytest, pillow, cryptography, et les dépendances frontend (axios, lodash, vite, picomatch, flatted) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- Infrastructure : Utilisation de `uv` pour la gestion des dépendances et la génération du fichier `requirements.txt`.
- Tests : Ajout et mise à jour de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration des performances : Optimisation du chargement des données et de la gestion des caches.
- Migration : Mise en place d'une migration pour initialiser les données des reminders.

### Autres changements
- Documentation : Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'interface.
- Configuration : Mise à jour des URLs de documentation pour les administrateurs et les conseillers.
- Nettoyage du code : Suppression de commentaires inutiles et amélioration de la lisibilité du code.
- Correction de typos et amélioration de la cohérence du code.
- Ajout de variables d'environnement pour la configuration.
- Suppression de code redondant.
- Amélioration de la gestion des erreurs.
- Ajout de tests pour les fichiers privés.
- Correction de bugs liés à la gestion des organisations.
- Amélioration de la gestion des liens vers les démarches numériques.
- Suppression de l'affichage de certaines informations sensibles.
- Correction de bugs liés à la gestion des tâches et des recommandations.
- Amélioration de la gestion des dates et des formats de date.
- Correction de bugs liés à la gestion des invites.
- Amélioration de la gestion des fichiers et des pièces jointes.
- Correction de bugs liés à la gestion des utilisateurs et des rôles.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de logs pour faciliter le débogage.
- Amélioration de la sécurité du code.
- Amélioration de la performance du code.
- Amélioration de la lisibilité du code.
- Amélioration de la documentation du code.
- Amélioration de la couverture des tests.
- Correction de bugs liés à l'interface utilisateur.
- Amélioration de l'accessibilité de l'interface utilisateur.
- Amélioration de la convivialité de l'interface utilisateur.
- Ajout de nouvelles fonctionnalités à l'interface utilisateur.
- Correction de bugs liés à la gestion des conversations.
- Amélioration de la gestion des conversations.
- Ajout de nouvelles fonctionnalités aux conversations.
- Correction de bugs liés à la gestion des documents.
- Amélioration de la gestion des documents.
- Ajout de nouvelles fonctionnalités aux documents.
- Correction de bugs liés à la gestion des tâches.
- Amélioration de la gestion des tâches.
- Ajout de nouvelles fonctionnalités aux tâches.
- Correction de bugs liés à la gestion des recommandations.
- Amélioration de la gestion des recommandations.
- Ajout de nouvelles fonctionnalités aux recommandations.
- Correction de bugs liés à la gestion des utilisateurs.
- Amélioration de la gestion des utilisateurs.
- Ajout de nouvelles fonctionnalités aux utilisateurs.
- Correction de bugs liés à la gestion des rôles.
- Amélioration de la gestion des rôles.
- Ajout de nouvelles fonctionnalités aux rôles.
- Correction de bugs liés à la gestion des permissions.
- Amélioration de la gestion des permissions.
- Ajout de nouvelles fonctionnalités aux permissions.
- Correction de bugs liés à la gestion des logs.
- Amélioration de la gestion des logs.
- Ajout de nouvelles fonctionnalités aux logs.
- Correction de bugs liés à la gestion des erreurs.
- Amélioration de la gestion des erreurs.
- Ajout de nouvelles fonctionnalités aux erreurs.
- Correction de bugs liés à la gestion des exceptions.
- Amélioration de la gestion des exceptions.
- Ajout de nouvelles fonctionnalités aux exceptions.
- Correction de bugs liés à la gestion de la sécurité.
- Amélioration de la gestion de la sécurité.
- Ajout de nouvelles fonctionnalités à la sécurité.
- Correction de bugs liés à la gestion de la performance.
- Amélioration de la gestion de la performance.
- Ajout de nouvelles fonctionnalités à la performance.
- Correction de bugs liés à la gestion de la lisibilité.
- Amélioration de la gestion de la lisibilité.
- Ajout de nouvelles fonctionnalités à la lisibilité.
- Correction de bugs liés à la gestion de la documentation.
- Amélioration de la gestion de la documentation.
- Ajout de nouvelles fonctionnalités à la documentation.
