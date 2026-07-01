## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 30 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment autour de la gestion des dossiers et des pièces jointes, ainsi que par des optimisations de performance et des corrections de bugs. Des efforts importants ont été consacrés à l'accessibilité et à la sécurité de la plateforme. De nouvelles fonctionnalités ont été ajoutées pour faciliter le travail des instructeurs et des administrateurs.

### Évolutions fonctionnelles
- **Dossiers :**
    - Les instructeurs peuvent désormais modifier les dossiers, avec une notification pour l'utilisateur.
    - Ajout d'un composant pour afficher les modifications apportées à un dossier.
    - Amélioration de l'affichage des dossiers partagés et en construction.
    - Possibilité de filtrer les dossiers par statut et de rechercher plus efficacement.
    - Ajout d'un indicateur visuel pour les dossiers en cours d'instruction.
- **Pièces jointes :**
    - Amélioration de la gestion des pièces jointes, notamment pour les avis d'imposition.
    - Correction d'un problème d'encodage des fichiers ZIP.
    - Possibilité de regénérer une attestation.
- **Authentification :**
    - Amélioration de la gestion de la connexion via ProConnect pour les procédures morales.
    - Ajout de la possibilité de se connecter avec FranceConnect.
- **Administration :**
    - Ajout d'un système de bannières d'information pour les administrateurs.
    - Amélioration de l'interface d'administration pour la gestion des procédures et des utilisateurs.
    - Possibilité de gérer les droits d'accès des utilisateurs.
- **Attestations :**
    - Ajout de la possibilité d'ajouter des sauts de page dans l'éditeur d'attestation.
    - Amélioration de la génération des PDF d'attestation, notamment pour la conformité PDF/UA.
- **API :**
    - Ajout de la possibilité de cloner une démarche avec des options spécifiques.
    - Exposition de nouvelles données via l'API GraphQL.

### Évolutions techniques
- **Refactoring :**
    - Migration de nombreux composants HAML vers ERB pour une meilleure maintenabilité.
    - Simplification du code et suppression de code obsolète.
    - Amélioration de la structure du code pour une meilleure lisibilité.
- **Performance :**
    - Optimisation des requêtes SQL pour améliorer les performances.
    - Mise en place d'un système de cache pour réduire la charge sur la base de données.
    - Amélioration de la gestion de la mémoire pour les exports de données.
- **Sécurité :**
    - Correction de failles de sécurité potentielles.
    - Renforcement de la sécurité de l'authentification.
    - Mise à jour des dépendances pour corriger les vulnérabilités connues.
- **Infrastructure :**
    - Mise à jour des dépendances Ruby et JavaScript.
    - Amélioration de la configuration de l'environnement de production.
- **Tests :**
    - Ajout de nouveaux tests unitaires et d'intégration.
    - Amélioration de la couverture de code des tests existants.
- **CI/CD :**
    - Amélioration du pipeline CI/CD pour une livraison plus rapide et plus fiable.

### Autres changements
- Amélioration de la documentation.
- Correction de problèmes de typographie et de grammaire.
- Mise à jour des traductions.
- Amélioration de l'accessibilité de l'interface utilisateur.
- Ajout de logs plus détaillés pour faciliter le débogage.
- Suppression de feature flags obsolètes.
- Amélioration de la gestion des erreurs.
- Ajout de commentaires dans le code pour une meilleure compréhension.
