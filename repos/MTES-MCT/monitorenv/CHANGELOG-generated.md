## Changelog : monitorenv (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des missions, notamment l'ajout de fonctionnalités pour les tags de mission, la gestion des informations et des fichiers associés aux navires, ainsi que des corrections pour améliorer la stabilité et l'expérience utilisateur. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des tags de mission dans l'interface back-office, permettant de catégoriser et filtrer les missions plus efficacement. [#b5d88fe](https://github.com/MTES-MCT/monitorenv/commit/b5d88fe)
- Possibilité d'ajouter des informations et des fichiers supplémentaires aux navires. [#030f5c2](https://github.com/MTES-MCT/monitorenv/commit/030f5c2)
- Les agents du CACEM peuvent désormais mettre à jour les missions directement depuis les rapports NAV. [#40bbc44](https://github.com/MTES-MCT/monitorenv/commit/40bbc44)
- Amélioration de la taille estimée des missions. [#a497eec](https://github.com/MTES-MCT/monitorenv/commit/a497eec)
- Ajout d'un défilement (debounce) au filtre de recherche des missions pour une meilleure performance. [#7eb7928](https://github.com/MTES-MCT/monitorenv/commit/7eb7928)

### Évolutions techniques
- Utilisation du composant `FileUploader` de `monitor-ui` pour la gestion des fichiers. [#6ad6960](https://github.com/MTES-MCT/monitorenv/commit/6ad6960)
- Correction pour assurer la conservation des données externes modifiées lors de la sauvegarde d'une mission. [#d658689](https://github.com/MTES-MCT/monitorenv/commit/d658689)
- Ajout d'un rechargement des données lors du changement d'onglet pour garantir l'affichage des informations les plus récentes. [#dde0e1b](https://github.com/MTES-MCT/monitorenv/commit/dde0e1b)
- Correction d'un bug lié à la création de tags fantômes lors de la mise à jour. [#852b591](https://github.com/MTES-MCT/monitorenv/commit/852b591)

### Autres changements
- Corrections de bugs et améliorations de l'expérience utilisateur (UX). [#4be2665](https://github.com/MTES-MCT/monitorenv/commit/4be2665)
- Corrections de tests E2E. [#514d0b3](https://github.com/MTES-MCT/monitorenv/commit/514d0b3) et [#ef6baef](https://github.com/MTES-MCT/monitorenv/commit/ef6baef)
- Correction pour ne pas filtrer les nouveaux tags. [#5ca7cd9](https://github.com/MTES-MCT/monitorenv/commit/5ca7cd9)
- Correction du filtre de tags de mission en fonction de la date de début de la mission ou de l'action. [#0c611a1](https://github.com/MTES-MCT/monitorenv/commit/0c611a1)
- Ajout des champs `isNoteworthy` et tags de mission à la liste et au formulaire des missions. [#03cea13](https://github.com/MTES-MCT/monitorenv/commit/03cea13)
