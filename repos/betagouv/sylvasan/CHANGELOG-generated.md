## Changelog : sylvasan (30 derniers jours, au 22 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application mobile, notamment des corrections de bugs, l'ajout de nouvelles fonctionnalités comme la géolocalisation et la gestion des images, ainsi que des optimisations de l'interface utilisateur. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et des corrections de validation.

### Évolutions fonctionnelles
- **Application mobile :**
    - Ajout de la géolocalisation native sur iOS et Android, permettant une localisation précise des observations.
    - Amélioration de la gestion des images : ajout d'une galerie de visualisation, compression des images et stockage local.
    - Correction de bugs liés à la validation des champs, notamment pour les champs conditionnels et les sous-champs.
    - Ajout d'indicateurs visuels (spinners) pour améliorer l'expérience utilisateur lors des chargements.
    - Possibilité de supprimer des observations non sauvegardées.
    - Amélioration de la gestion des erreurs et des messages d'information.
    - Ajout de la synchronisation des données avec une notification visuelle.
- **Interface utilisateur :**
    - Ajustements de l'interface pour une meilleure lisibilité et ergonomie, notamment pour les noms longs et les champs image.
    - Ajout de boutons de synchronisation.
    - Ajout d'un modal de confirmation pour la déconnexion.
    - Correction de bugs d'affichage sur iOS.
- **Fonctionnalités :**
    - Ajout de la possibilité de filtrer les réponses par enquête.
    - Ajout de la gestion des vocabulaires pour les champs de sélection.
    - Ajout de la possibilité de créer des pôles.
    - Ajout de la gestion de l'affichage des labels pour les vocabulaires.
    - Ajout de la possibilité de supprimer une page.

### Évolutions techniques
- **Architecture et infrastructure :**
    - Mise en place de Django Storages pour la gestion du stockage des fichiers.
    - Refactorisation du code pour améliorer la maintenabilité et la performance.
    - Mise à jour des dépendances (Django, React, Node.js, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- **Développement :**
    - Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
    - Amélioration du processus de CI/CD pour automatiser les déploiements.
    - Utilisation de TypeScript pour améliorer la robustesse du code.
    - Ajout de linters (Ruff) pour garantir la cohérence du code.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de code mort.
- Correction de coquilles et d'erreurs mineures.
- Ajout de commentaires pour améliorer la lisibilité du code.
- Mise à jour des icônes de l'application.
- Ajout de la gestion des erreurs Oauth.
