## Changelog : monitorenv (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des corrections et améliorations concernant la gestion des missions, des données réglementaires, des cartes et des navires. L'interface utilisateur a été améliorée avec l'ajout de fonctionnalités de gestion de fichiers et d'informations supplémentaires sur les navires. Des corrections de dates et de calculs géographiques ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la gestion des missions :
  - Correction de l'affichage des dates dans la liste des missions et dans les rapports. [#98131b9](https://github.com/MTES-MCT/monitorenv/issues/98131b9)
  - Possibilité de ne pas sélectionner la même unité de contrôle plusieurs fois dans une mission. [#f5215a6](https://github.com/MTES-MCT/monitorenv/issues/f5215a6)
  - Empêche la mise à jour du champ "nombre de personnes" lors d'un changement de valeur. [#f960ff6](https://github.com/MTES-MCT/monitorenv/issues/f960ff6)
  - Possibilité pour le CACEM de mettre à jour une mission à partir d'un rapport de navigation. [#40bbc44](https://github.com/MTES-MCT/monitorenv/issues/40bbc44)
- Amélioration de la gestion des données :
  - Correction du flux de mise à jour des zones réglementaires du CACEM. [#7291203](https://github.com/MTES-MCT/monitorenv/issues/7291203)
  - Correction des données `regulatory_areas_open_data`. [#43554f4](https://github.com/MTES-MCT/monitorenv/issues/43554f4)
- Amélioration de la cartographie :
  - Correction du calcul des coordonnées lors du clic sur la carte pour créer un point. [#30382aa](https://github.com/MTES-MCT/monitorenv/issues/30382aa)
- Ajout d'informations supplémentaires et de fichiers aux navires. [#030f5c2](https://github.com/MTES-MCT/monitorenv/issues/030f5c2)
- L'API des façades renvoie maintenant le nom distinct de la façade. [#5440c30](https://github.com/MTES-MCT/monitorenv/issues/5440c30)
- Utilisation de l'API des façades pour récupérer les façades au lieu d'un enum. [#09be83a](https://github.com/MTES-MCT/monitorenv/issues/09be83a)
- Résolution du label au lieu de la valeur dans le panel. [#49a52cd](https://github.com/MTES-MCT/monitorenv/issues/49a52cd)

### Évolutions techniques
- Utilisation de `FileUploader` depuis `monitor-ui` pour la gestion des fichiers. [#6ad6960](https://github.com/MTES-MCT/monitorenv/issues/6ad6960)
- Ajout de `ST_MakeValid` pour le calcul des façades. [#89726c5](https://github.com/MTES-MCT/monitorenv/issues/89726c5)
- Correction de l'utilisation de `savedMission` pour conserver les données externes modifiées. [#d658689](https://github.com/MTES-MCT/monitorenv/issues/d658689)
- Refactoring : Renommage de "facade" en "seafront". [#3037a3a](https://github.com/MTES-MCT/monitorenv/issues/3037a3a)
- Corrections et modifications suite aux revues de code. [#458d8a5](https://github.com/MTES-MCT/monitorenv/issues/458d8a5), [#96011bb](https://github.com/MTES-MCT/monitorenv/issues/96011bb)

### Autres changements
- Correction d'une faute de frappe dans le titre "all seafronts". [#e8155bb](https://github.com/MTES-MCT/monitorenv/issues/e8155bb)
- Corrections de tests unitaires et E2E. [#67b51dc](https://github.com/MTES-MCT/monitorenv/issues/67b51dc), [#3e49492](https://github.com/MTES-MCT/monitorenv/issues/3e49492), [#6493bb8](https://github.com/MTES-MCT/monitorenv/issues/6493bb8), [#ef6baef](https://github.com/MTES-MCT/monitorenv/issues/ef6baef)
