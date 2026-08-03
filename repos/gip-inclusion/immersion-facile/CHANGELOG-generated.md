## Changelog : immersion-facile (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur les tableaux de bord bénéficiaire et établissement, avec l'ajout de nouvelles fonctionnalités de gestion des conventions et des discussions. Des corrections et des optimisations ont également été apportées à la gestion des agences, des utilisateurs et des notifications. Enfin, des efforts ont été faits pour améliorer la documentation et la qualité du code.

### Évolutions fonctionnelles
- **Tableau de bord Bénéficiaire :** Ajout d'une liste des conventions avec un affichage formaté et des badges d'état. Navigation améliorée et message de bienvenue personnalisé.
- **Tableau de bord Établissement :** Amélioration de l'interface utilisateur pour la gestion des discussions, avec affichage d'informations supplémentaires sur les établissements.
- **Gestion des conventions :**
    - Possibilité pour un établissement de créer une convention lorsqu'une discussion est acceptée.
    - Ajout d'un badge "à relancer" pour les conventions nécessitant une action.
    - Affichage du logo de l'agence sur les documents de convention (si disponible).
    - Possibilité de supprimer les droits d'accès d'un utilisateur à une agence.
    - Affichage de la date de naissance du bénéficiaire pour les administrateurs.
- **Notifications :**
    - Ajout de notifications pour les demandes d'enregistrement d'agence.
    - Amélioration des notifications concernant le bannissement d'un établissement.
    - Ajout de notifications pour les validateurs.
- **Gestion des utilisateurs :**
    - Amélioration de la gestion des droits d'accès des utilisateurs aux agences.
    - Suppression des utilisateurs FT Connect lors de la suppression d'une convention.
- **Recherche :** Ajout d'un bouton pour suivre l'intérêt d'un bénéficiaire.
- **Formulaire d'établissement :** Amélioration du formulaire avec des instructions plus claires et la suppression d'informations sur les webinaires.

### Évolutions techniques
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des erreurs et des notifications.
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration, notamment avec Playwright pour les tests E2E.
- **Architecture :**
    - Utilisation de "use case builders" pour simplifier la création et la gestion des cas d'utilisation.
    - Amélioration de la gestion des dépendances et des mises à jour de librairies.
    - Optimisation des requêtes SQL avec l'ajout d'index.
- **CI/CD :** Amélioration du pipeline CI/CD pour une meilleure gestion des builds et des déploiements.
- **Sécurité :** Mise à jour des dépendances pour corriger les vulnérabilités de sécurité.
- **Authentification :** Simplification de la récupération des informations utilisateur authentifié.

### Autres changements
- Mise à jour de la documentation et des mentions légales.
- Nettoyage du code et suppression de fichiers inutilisés.
- Amélioration des messages d'erreur et de l'expérience utilisateur globale.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Mise à jour des dépendances (libphonenumber, protobufjs, etc.).
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de problèmes de typage et de linting.
