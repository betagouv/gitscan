## Changelog : monitorenv (30 derniers jours, au 9 juin 2026)

### Résumé
Les dernières mises à jour de monitorenv se concentrent sur l'amélioration de l'interface utilisateur, notamment des corrections et des refactorisations des dialogues et modales. De nouvelles fonctionnalités ont été ajoutées pour la gestion des tags et des zones de vigilance, ainsi que des améliorations de la réactivité et de l'accessibilité de l'application. Des optimisations techniques ont également été réalisées, incluant des mises à jour de l'environnement de développement.

### Évolutions fonctionnelles
- Ajout de la gestion des tags dans l'interface backoffice, permettant leur création et leur affichage [#98a148b](https://github.com/MTES-MCT/monitorenv/commit/98a148b).
- Correction de l'affichage de la source du `controlUnit` sur l'overlay des zones de vigilance [#4c8b7b3](https://github.com/MTES-MCT/monitorenv/commit/4c8b7b3).
- Amélioration du flux de données pour les zones réglementaires open data [#54092ee](https://github.com/MTES-MCT/monitorenv/commit/54092ee).
- Ajout d'un focus sur la ligne cliquée dans la table de position [#4df3916](https://github.com/MTES-MCT/monitorenv/commit/4df3916).
- Correction du filtrage des ressources `controlUnit` par `missionsControlResources` [#f23bc46](https://github.com/MTES-MCT/monitorenv/commit/f23bc46).
- Création d'une table éditable avec un formulaire et un rechargement des sous-tags lors de la sauvegarde du tag parent [#026cade](https://github.com/MTES-MCT/monitorenv/commit/026cade).

### Évolutions techniques
- Renommage de certains composants pour une meilleure organisation [#cdc3ca5](https://github.com/MTES-MCT/monitorenv/commit/cdc3ca5) et [#0ae95aa](https://github.com/MTES-MCT/monitorenv/commit/0ae95aa).
- Mise à jour de l'environnement de développement vers Node 24 et npm 11, avec ajout de logs pour les tests RGAA [#84ee855](https://github.com/MTES-MCT/monitorenv/commit/84ee855).
- Refactorisation et amélioration de la conception des dialogues (DeleteDialog, ArchiveModal, etc.) [#45681e1](https://github.com/MTES-MCT/monitorenv/commit/45681e1), [#6a5fab6](https://github.com/MTES-MCT/monitorenv/commit/6a5fab6), [#b9586e2](https://github.com/MTES-MCT/monitorenv/commit/b9586e2), [#81cf219](https://github.com/MTES-MCT/monitorenv/commit/81cf219).
- Correction de problèmes de typage après la mise à jour de certaines dépendances [#5b88cbb](https://github.com/MTES-MCT/monitorenv/commit/5b88cbb).
- Correction de noms de variables [#e1136b6](https://github.com/MTES-MCT/monitorenv/commit/e1136b6).

### Autres changements
- Ajout de tests RGAA pour les tags et les zones réglementaires [#9ca8ed3](https://github.com/MTES-MCT/monitorenv/commit/9ca8ed3).
- Correction de tests E2E [#bb05e5b](https://github.com/MTES-MCT/monitorenv/commit/bb05e5b) et [#127dedd](https://github.com/MTES-MCT/monitorenv/commit/127dedd).
- Suppression d'un patch inattendu [#eba3cd9](https://github.com/MTES-MCT/monitorenv/commit/eba3cd9).
- Ajout de `latest` lors d'une release [#334c957](https://github.com/MTES-MCT/monitorenv/commit/334c957).
