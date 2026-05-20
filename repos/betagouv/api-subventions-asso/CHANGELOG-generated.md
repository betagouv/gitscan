## Changelog : api-subventions-asso (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration des données Osiris, avec une refonte de la gestion des entités brutes et l'ajout de nouveaux DTO. Des améliorations techniques ont été apportées pour moderniser l'infrastructure du projet, notamment le passage à pnpm workspaces et la suppression de code obsolète. L'interface utilisateur a également été mise à jour pour afficher les actions Osiris dans un modal.

### Évolutions fonctionnelles
- Ajout de l'affichage des actions Osiris dans un modal sur le front-end ([#3910](https://github.com/betagouv/api-subventions-asso/pull/3910)).
- Amélioration de l'affichage des informations relatives aux données Helios sur le front-end, incluant le nom de l'allocataire et l'ID de paiement.
- Correction d'un bug lié à la migration Proconnect ([#3898](https://github.com/betagouv/api-subventions-asso/issues/3898)).
- Correction d'un bug dans le test unitaire du parser Osiris pour la date de mise à jour.

### Évolutions techniques
- Refonte de la gestion des entités brutes Osiris pour stocker les données imbriquées, améliorant ainsi la flexibilité et la robustesse de l'API ([#3887](https://github.com/betagouv/api-subventions-asso/pull/3887), [#3904](https://github.com/betagouv/api-subventions-asso/pull/3904)).
- Création de nouveaux DTO et refactoring des mappings pour les providers et les détails Osiris ([#3908](https://github.com/betagouv/api-subventions-asso/pull/3908), [#3909](https://github.com/betagouv/api-subventions-asso/pull/3909)).
- Migration du projet vers pnpm workspaces, remplaçant Lerna pour une meilleure gestion des dépendances et des builds ([#3917](https://github.com/betagouv/api-subventions-asso/pull/3917)).
- Refactoring du code lié à l'analyse des données Osiris, incluant la suppression de code obsolète et l'amélioration des tests.
- Suppression de routes de provider obsolètes ([#3911](https://github.com/betagouv/api-subventions-asso/pull/3911)).
- Amélioration des tests et de la validation des données Osiris.

### Autres changements
- Ajout d'un README pour le script de scrapping LCA-OSIRIS ([#3901](https://github.com/betagouv/api-subventions-asso/pull/3901)).
- Suppression de code de validation inutilisé dans la CLI.
- Déplacement des fichiers de parsing Osiris vers le dossier `adapters/inputs/cli/osiris`.
- Mise à jour des versions du projet (v0.84.0, v0.84.1, v0.84.2, v0.84.3, v0.84.4, v0.84.5).
