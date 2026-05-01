## Changelog : monitorfish (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration de la gestion des signalements de pêche illégale, l'ajout de nouvelles catégories d'infractions, et des corrections pour une meilleure expérience utilisateur, notamment au niveau de l'affichage des informations sur les navires et des préavis. Des optimisations techniques ont également été apportées, notamment des mises à jour de dépendances et des améliorations de l'architecture frontend.

### Évolutions fonctionnelles
- Ajout de la possibilité de signaler plusieurs infractions en même temps ([#5061](https://github.com/MTES-MCT/monitorfish/issues/5061)).
- Ajout de trois nouvelles catégories d'infractions (NATINF) ([#4975](https://github.com/MTES-MCT/monitorfish/issues/4975)).
- Amélioration de l'affichage des signalements sur la carte, avec un cercle rouge uniquement pour les signalements en cours sur la marée ([#4967](https://github.com/MTES-MCT/monitorfish/issues/4967)).
- Possibilité de supprimer automatiquement les alertes paramétrables ([#5027](https://github.com/MTES-MCT/monitorfish/issues/5027)).
- Affichage des coordonnées lors de la modification d'un signalement ([#4946](https://github.com/MTES-MCT/monitorfish/issues/4946)).
- Amélioration de l'interface utilisateur pour les modalités de contact sur la fiche navire ([#5051](https://github.com/MTES-MCT/monitorfish/issues/5051)).
- Ajout d'une raison pour les préavis "à vérifier" ([#5033](https://github.com/MTES-MCT/monitorfish/issues/5033)).
- Filtrage des préavis par type "préavis 0" ([#5050](https://github.com/MTES-MCT/monitorfish/issues/5050)).
- Correction d'un bug empêchant l'affichage correct des alertes dans la fiche navire ([#5028](https://github.com/MTES-MCT/monitorfish/issues/5028)).
- Correction d'un problème d'affichage des champs bloquants pour les préavis d'accès aux services ([#4948](https://github.com/MTES-MCT/monitorfish/issues/4948)).
- Correction d'un bug où les signalements apparaissaient hors façade ([#5044](https://github.com/MTES-MCT/monitorfish/issues/5044)).
- Correction d'un problème de filtrage des dernières positions VMS ([#4979](https://github.com/MTES-MCT/monitorfish/issues/4979)).

### Évolutions techniques
- Refactoring du composant carte avec des hooks ([#5030](https://github.com/MTES-MCT/monitorfish/issues/5030)).
- Mise à jour de la librairie OpenLayers ([#5021](https://github.com/MTES-MCT/monitorfish/issues/5021)).
- Migration des infractions de reporting vers une liste.
- Amélioration de la gestion des tests Cypress.
- Mise à jour de plusieurs dépendances frontend (ora, basic-ftp, lodash, lodash-es, vite, got).
- Mise à jour des actions Docker pour le build et le login.
- Correction d'une race condition dans la fixture de la base de données des tests de pipeline.
- Correction de bugs et améliorations diverses dans le code backend.

### Autres changements
- Ajout de la façade Pacifique ([#5061](https://github.com/MTES-MCT/monitorfish/issues/5061)).
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour de la documentation.
- Ajout de commentaires et de tests unitaires.
- Configuration de Dependabot pour les mises à jour de dépendances.
- Correction d'un problème avec l'importation de la couche EEZ.
- Correction d'un bug dans le flow `risk_elements`.
- Suppression de la simplification de la géométrie pour améliorer les performances.
- Amélioration de la gestion des projections OpenLayers.
- Suppression de code mort.
- Correction de problèmes de build avec ReadTheDocs.
