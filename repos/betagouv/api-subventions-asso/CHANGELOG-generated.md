## Changelog : api-subventions-asso (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration et le traitement des données Helios, ainsi que sur des améliorations de l'automatisation et de la correction de bugs liés à l'importation des données Osiris et Proconnect. Des ajustements ont également été apportés à l'interface utilisateur pour une meilleure présentation des informations.

### Évolutions fonctionnelles
- Intégration et parsing des données Helios, permettant de nouvelles fonctionnalités liées à ces données (via [#3865](https://github.com/betagouv/api-subventions-asso/issues/3865) et [#3886](https://github.com/betagouv/api-subventions-asso/issues/3886)).
- Amélioration de l'affichage du nom de l'allocataire dans l'instructeur pour les données Helios.
- Correction d'un bug lié à la migration Proconnect ([#3898](https://github.com/betagouv/api-subventions-asso/issues/3898)).

### Évolutions techniques
- Refactorisation de la gestion des requêtes Osiris pour stocker les entités imbriquées brutes, améliorant ainsi la flexibilité et la maintenabilité du code.
- Déplacement des fichiers de parsing Osiris vers le dossier `adapters/inputs/cli/osiris` pour une meilleure organisation.
- Amélioration des tests unitaires pour le parsing Osiris, notamment pour la date de mise à jour.
- Suppression de code obsolète (méthode `validate` dans la CLI).
- Amélioration du mapping des champs et correction des tests liés à Osiris.

### Autres changements
- Ajout d'un README pour le script de récupération LCA-OSIRIS ([#3901](https://github.com/betagouv/api-subventions-asso/issues/3901)).
- Correction de l'indentation du fichier `pnpm-lock.yaml`.
- Mise à jour de la version de l'API à v0.84.5.
