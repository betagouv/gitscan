## Changelog : drive (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des fonctionnalités de conversion de fichiers, notamment en ajoutant la prise en charge de la conversion de documents Office via OnlyOffice. De nouvelles options d'exportation de dossiers ont été implémentées, et des améliorations ont été apportées à la gestion des comptes utilisateurs, avec l'ajout d'un processus de réconciliation. Des corrections de bugs et des optimisations diverses ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité de convertir des fichiers hérités (legacy) au format Office via OnlyOffice. Un modal de conversion a été ajouté à l'interface utilisateur.
- Implémentation de l'exportation de dossiers en format ZIP. Une nouvelle action a été ajoutée pour permettre cette fonctionnalité.
- Ajout de la gestion de la réconciliation des comptes utilisateurs, incluant une interface d'administration et la possibilité d'importer des données via un fichier CSV.
- Amélioration des CTA (Call To Action) sur les fichiers et dossiers publics, avec des composants dédiés pour les utilisateurs anonymes et authentifiés.
- Prise en charge du téléchargement de fichiers Grist.

### Évolutions techniques
- Amélioration de la gestion des requêtes WOPI (Web Office Protocol Interface) pour la conversion de fichiers, notamment en utilisant des JWT (JSON Web Tokens) pour la signature.
- Normalisation de la recherche d'extensions WOPI.
- Refonte de la gestion des états de conversion des fichiers, avec l'ajout d'un état "en cours de conversion".
- Utilisation de `zipstream-ng` pour l'exportation de dossiers.
- Amélioration de la gestion des erreurs et des transactions lors de la duplication de fichiers.
- Suppression des colonnes `numchild` obsolètes de la table `item`.
- Ajout d'un endpoint de streaming pour l'exportation de dossiers.
- Ajout d'une méthode générique `send_email` sur le modèle utilisateur.

### Autres changements
- Documentation de la réconciliation des comptes utilisateurs.
- Correction de bugs liés à l'affichage des fichiers et dossiers, notamment la gestion des barres obliques dans les noms de fichiers et des problèmes de responsive design.
- Mise à jour de la bibliothèque d'interface utilisateur `ui-kit` vers la version 0.22.0.
- Amélioration de la gestion des tests, avec l'ajout de tests E2E pour le flux de conversion.
- Correction de problèmes liés à la gestion des autorisations et des accès aux fichiers.
