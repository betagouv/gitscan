## Changelog : monitorenv (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau des modales et des zones de vigilance, ainsi que sur l'ajout de nouvelles fonctionnalités pour la gestion des tags et des zones réglementaires. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Tags :** Ajout d'une fonctionnalité de gestion des tags dans l'interface backoffice, permettant de créer, modifier et afficher des tags associés aux données. [#98a148b](https://github.com/MTES-MCT/monitorenv/commit/98a148b)
- **Zones de vigilance :** Amélioration de l'affichage du planning des zones de vigilance en vue liste, avec l'ajout d'un tooltip pour la période. [#ea31756](https://github.com/MTES-MCT/monitorenv/commit/ea31756)
- **Zones réglementaires :** Correction du flux de données pour les zones réglementaires issues de l'open data. [#54092ee](https://github.com/MTES-MCT/monitorenv/commit/54092ee)
- **Tableaux de données :** Création d'un tableau de données éditable avec un formulaire associé et un rechargement des données lors de la sauvegarde. [#026cade](https://github.com/MTES-MCT/monitorenv/commit/026cade)
- **Focus :** Ajout d'un focus sur la ligne lors d'un clic sur une position. [#4df3916](https://github.com/MTES-MCT/monitorenv/commit/4df3916)
- **Filtres :** Correction du filtrage des ressources `controlUnit` par `missionsControlResources`. [#f23bc46](https://github.com/MTES-MCT/monitorenv/commit/f23bc46)
- **Améliorations UI :** Refonte et corrections diverses des modales (suppression, archive, rapport, mission) pour améliorer l'expérience utilisateur et l'accessibilité. [#c8dc840](https://github.com/MTES-MCT/monitorenv/commit/c8dc840), [#b9586e2](https://github.com/MTES-MCT/monitorenv/commit/b9586e2), [#6a5fab6](https://github.com/MTES-MCT/monitorenv/commit/6a5fab6), [#45681e1](https://github.com/MTES-MCT/monitorenv/commit/45681e1)

### Évolutions techniques
- **Node & NPM :** Mise à jour vers Node 24 et NPM 11, avec ajout de logs pour les tests RGAA. [#84ee855](https://github.com/MTES-MCT/monitorenv/commit/84ee855)
- **Refactoring :** Refactorisation de `MonthBox` et suppression de code inutile. [#f4e7cc7](https://github.com/MTES-MCT/monitorenv/commit/f4e7cc7)
- **Composants :** Renommage de certains composants pour une meilleure organisation. [#cdc3ca5](https://github.com/MTES-MCT/monitorenv/commit/cdc3ca5), [#0ae95aa](https://github.com/MTES-MCT/monitorenv/commit/0ae95aa)
- **Typage :** Correction de problèmes de typage suite à la mise à jour des dépendances. [#5b88cbb](https://github.com/MTES-MCT/monitorenv/commit/5b88cbb)

### Autres changements
- **Tests :** Corrections de tests unitaires et E2E, notamment pour les tags, les zones réglementaires et les modales. [#bb05e5b](https://github.com/MTES-MCT/monitorenv/commit/bb05e5b), [#9ca8ed3](https://github.com/MTES-MCT/monitorenv/commit/9ca8ed3), [#127dedd](https://github.com/MTES-MCT/monitorenv/commit/127dedd), [#d590634](https://github.com/MTES-MCT/monitorenv/commit/d590634)
- **Accessibilité :** Amélioration de l'accessibilité de la liste des périodes dans les zones de vigilance. [#83c688b](https://github.com/MTES-MCT/monitorenv/commit/83c688b)
- **Correction :** Suppression d'un patch inattendu. [#eba3cd9](https://github.com/MTES-MCT/monitorenv/commit/eba3cd9)
- **Release :** Ajout de `latest` lors de la création d'une release. [#334c957](https://github.com/MTES-MCT/monitorenv/commit/334c957)
