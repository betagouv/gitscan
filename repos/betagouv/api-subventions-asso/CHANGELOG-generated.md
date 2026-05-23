## Changelog : api-subventions-asso (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration et l'amélioration des données Osiris, avec un effort important de refactoring pour une meilleure structure et maintenabilité du code. Des corrections et des améliorations ont également été apportées à l'API et à l'interface utilisateur pour une expérience plus fluide.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les actions Osiris sans intitulé. [#3840](https://github.com/betagouv/api-subventions-asso/issues/3840)
- Affichage des actions Osiris dans le modal de détail des subventions. [#3841](https://github.com/betagouv/api-subventions-asso/issues/3841)
- Ajout de nouvelles DTO (Data Transfer Objects) pour l'association et les détails des subventions Osiris. [#3913](https://github.com/betagouv/api-subventions-asso/issues/3913) et [#3908](https://github.com/betagouv/api-subventions-asso/issues/3908)
- Ajout d'une route cachée pour les subventions et Osiris, ainsi qu'un use case pour récupérer les détails. [#3840](https://github.com/betagouv/api-subventions-asso/issues/3840)
- Script pour supprimer les fichiers vides des téléchargements Osiris. [#3919](https://github.com/betagouv/api-subventions-asso/issues/3919)

### Évolutions techniques
- Refactoring important de la gestion des données Osiris, incluant la refactorisation des entités, des mappers et des parsers pour stocker les données brutes imbriquées. [#3887](https://github.com/betagouv/api-subventions-asso/issues/3887) et [#3904](https://github.com/betagouv/api-subventions-asso/issues/3904)
- Migration du service API "asso" vers une architecture basée sur des adaptateurs et des ports. [#3549](https://github.com/betagouv/api-subventions-asso/issues/3549)
- Remplacement de Lerna par pnpm workspaces pour la gestion des dépendances. [#3916](https://github.com/betagouv/api-subventions-asso/issues/3916)
- Suppression de code obsolète et de validations inutiles dans le code lié à Osiris. [#3904](https://github.com/betagouv/api-subventions-asso/issues/3904)
- Amélioration des tests unitaires et d'intégration pour les nouvelles fonctionnalités et les refactorings.
- Mise à jour des dépendances vers les dernières versions mineures. [#3924](https://github.com/betagouv/api-subventions-asso/issues/3924)

### Autres changements
- Documentation mise à jour pour le script de suppression des fichiers vides Osiris. [#3920](https://github.com/betagouv/api-subventions-asso/issues/3920)
- Dépréciation des routes de valeurs de provider. [#3911](https://github.com/betagouv/api-subventions-asso/issues/3911)
