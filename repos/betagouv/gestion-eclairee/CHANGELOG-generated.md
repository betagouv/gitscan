## Changelog : gestion-eclairee (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du pipeline de traitement des fichiers CSV, notamment pour l'importation des données CPRO. Des refactorings importants ont été effectués pour optimiser la gestion des données et la validation des informations financières. L'initialisation d'une application Django marque le début d'une nouvelle phase de développement.

### Évolutions fonctionnelles
- Amélioration de l'importation des fichiers CSV : le pipeline a été refactoré pour une meilleure gestion des colonnes et du suivi des sources de données.
- Validation des données CPRO : des contrôles plus robustes ont été ajoutés pour la validation des montants et des codes EJ, avec une gestion améliorée des erreurs et des arrondis.
- Téléchargement des données CPRO : implémentation de la fonctionnalité de téléchargement des données CPRO.
- Prise en charge des fichiers CSV avec ou sans indication du service.

### Évolutions techniques
- Refactoring du modèle `User` : la clé primaire du modèle `User` a été modifiée de UUID à BigAutoField, simplifiant ainsi la gestion des identifiants utilisateurs.
- Initialisation d'une application Django : mise en place de la structure de base d'une application Django, ouvrant la voie à de nouvelles fonctionnalités et à une architecture plus moderne.
- Utilisation de Ruff : intégration de l'outil Ruff pour le linting et la vérification du code, améliorant ainsi la qualité et la cohérence du code.
- Refactoring général du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Ajout des dépendances nécessaires au projet, notamment Django et ses composants associés.
- Premier commit du dépôt, initialisant le projet.
