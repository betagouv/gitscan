## Changelog : drive (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités d'exportation, l'ajout de mécanismes de réconciliation de comptes utilisateurs et des corrections pour l'intégration WOPI. Des améliorations de l'interface utilisateur, notamment via l'intégration de composants de la bibliothèque `ui-kit`, ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers sous forme d'archives ZIP. [#issue](https://github.com/suitenumerique/drive/issues/)
- Implémentation d'un processus de réconciliation de comptes utilisateurs, incluant une confirmation par email. [#issue](https://github.com/suitenumerique/drive/issues/)
- Amélioration de l'intégration WOPI en remplaçant `VersionId` par `Etag`. [#3293ce5](https://github.com/suitenumerique/drive/commit/3293ce5)
- Intégration de composants `ui-kit` pour les icônes de fichiers, les prévisualisations et les aperçus de fichiers.
- Ajout d'événements de suivi PostHog pour le duplication d'éléments et les modifications de type de colonne.
- Ajout d'un message de journal pour la taille maximale de fichier WOPI.

### Évolutions techniques
- Suppression des colonnes `numchild` obsolètes de la table `item`.
- Mise à jour de la dépendance Django vers la version 5.2.14 (correctif de sécurité).
- Mise à jour de la dépendance urllib3 vers la version 2.7.0 (correctif de sécurité).
- Refactoring du code pour déplacer les importations MIME vers `ui-kit`.
- Mise à jour de la version de `ui-kit`.
- Ajout d'une méthode générique `send_email` sur le modèle `User`.
- Ajout d'une dépendance `zipstream-ng` pour l'exportation des dossiers.

### Autres changements
- Documentation de la réconciliation des comptes utilisateurs.
- Mise à jour du fichier `CHANGELOG.md`.
- Ajout d'une commande de démonstration pour la réconciliation.
- Ajout d'une tâche CSV pour l'importation de la réconciliation des utilisateurs.
- Capture d'événements PostHog pour la duplication d'éléments et les changements de type de colonne.
