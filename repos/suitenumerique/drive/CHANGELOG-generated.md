## Changelog : drive (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment l'ajout d'un système de notes de version intégré, la synchronisation automatique de la langue de l'interface, et des améliorations de la navigation et de la gestion des fichiers. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Un nouveau système de mirroring de fichiers sur S3 a été implémenté pour une meilleure gestion du stockage.

### Évolutions fonctionnelles
- Ajout d'un système de notes de version avec suivi de la version lue par l'utilisateur (#9161e31).
- Synchronisation automatique de la langue de l'interface utilisateur avec la langue du navigateur lors de la connexion (#35c6c19).
- Amélioration de l'interface utilisateur de l'explorateur de fichiers, incluant des améliorations visuelles et fonctionnelles (#a98a5d7, #5bbf11d, #3070460).
- Possibilité de rediriger vers une page d'accueil externe configurable (#201d728, #a965203).
- Ajout de la gestion des fichiers avec des caractères spéciaux dans leur nom (#0823972).
- Amélioration de la navigation avec affichage de la page racine dans l'arborescence de navigation (#179e4c1).
- Filtrage des éléments récents pour n'afficher que les fichiers (#15bff8c).
- Ajout de tests E2E pour les nouvelles fonctionnalités, notamment la synchronisation de la langue et la gestion des partages (#1f9edce, #6eb1813).
- Ajout de la possibilité de déplacer des éléments vers la racine (#8251464).

### Évolutions techniques
- Ajout du support de la plateforme ARM64 pour les images Docker (#f43c8a4).
- Mise à jour de Playwright de 1.56.1 à 1.58.2 (#edc8d2c).
- Refactorisation de composants frontend pour une meilleure réutilisabilité (#e3527a3, #25043bd).
- Amélioration de la gestion des accès et des rôles, avec une meilleure synchronisation des permissions (#f696568, #dca39e3, #a094dfc).
- Implémentation d'un système de mirroring de fichiers vers S3, incluant une gestion des erreurs et une configuration flexible (#e2d6d4e, #7817cda, #af6bd44, #123f3de, #0b4326a, #5bd9859, #b706b54).
- Optimisation des requêtes en base de données pour améliorer la performance (#7b18daf, #8cfa413).
- Mise à jour de plusieurs dépendances, notamment Django, Pillow et cryptography (#50e19c9, #aa5efc3).
- Amélioration de la configuration Nginx (#5b3ab40, #24a336b).
- Refactorisation du code pour une meilleure maintenabilité et lisibilité.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités (#7d37ec8).
- Suppression de la prise en charge de Scalingo pgdump (#abd055a).
- Correction de problèmes liés aux cookies Keycloak pour le silent login (#ecf7d74).
- Suppression de la notion de workspace (#ff831e0).
- Mise à jour de la version de release à 0.13.0 (#7c7c0d7, #9b6298b).
- Ajout de tests E2E pour les nouvelles fonctionnalités (#158296c, #c169d9a).
- Suppression de l'utilisation de transactions atomiques pour la création d'éléments (#5e16aa9).
- Correction de bugs mineurs et améliorations de la qualité du code.
