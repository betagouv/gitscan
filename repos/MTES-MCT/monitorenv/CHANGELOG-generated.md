## Changelog : monitorenv (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des missions, des données réglementaires et de la cartographie. Des corrections ont été apportées pour assurer la cohérence des dates, la sélection des unités de contrôle et la gestion des données des navires. L'interface utilisateur a également été améliorée avec l'ajout de fonctionnalités de téléchargement de fichiers et d'informations supplémentaires sur les navires.

### Évolutions fonctionnelles
- Amélioration de la gestion des missions :
  - Correction de l'affichage des dates dans la liste des missions et les rapports. [#98131b9](https://github.com/MTES-MCT/monitorenv/commit/98131b9)
  - Possibilité de sélectionner une unité de contrôle une seule fois dans une mission. [#f5215a6](https://github.com/MTES-MCT/monitorenv/commit/f5215a6)
  - Empêche la mise à jour du nombre de personnes concernées lors d'un changement de valeur. [#f960ff6](https://github.com/MTES-MCT/monitorenv/commit/f960ff6)
- Amélioration de la gestion des données :
  - Correction du flux de mise à jour des zones réglementaires CACEM. [#7291203](https://github.com/MTES-MCT/monitorenv/commit/7291203)
  - Correction des données `regulatory_areas_open_data`. [#43554f4](https://github.com/MTES-MCT/monitorenv/commit/43554f4)
- Amélioration de la cartographie :
  - Correction du calcul des coordonnées lors du clic sur la carte pour créer un point. [#30382aa](https://github.com/MTES-MCT/monitorenv/commit/30382aa)
- Ajout d'informations supplémentaires et de fichiers aux navires. [#030f5c2](https://github.com/MTES-MCT/monitorenv/commit/030f5c2)
- Le CACEM peut maintenant mettre à jour une mission à partir d'un rapport de navigation. [#40bbc44](https://github.com/MTES-MCT/monitorenv/commit/40bbc44)

### Évolutions techniques
- Refactorisation du code lié aux façades (maintenant appelées "seafront") pour utiliser l'API dédiée et éviter les énumérations. [#3037a3a](https://github.com/MTES-MCT/monitorenv/commit/3037a3a), [#09be83a](https://github.com/MTES-MCT/monitorenv/commit/09be83a)
- Utilisation du composant `FileUploader` de `monitor-ui` pour le téléchargement de fichiers. [#6ad6960](https://github.com/MTES-MCT/monitorenv/commit/6ad6960)
- Ajout de `ST_MakeValid` pour les façades calculées. [#89726c5](https://github.com/MTES-MCT/monitorenv/commit/89726c5)
- Correction pour conserver les données externes modifiées dans les missions sauvegardées. [#d658689](https://github.com/MTES-MCT/monitorenv/commit/d658689)
- Correction de l'API seafront pour retourner le nom distinct de la façade. [#5440c30](https://github.com/MTES-MCT/monitorenv/commit/5440c30)

### Autres changements
- Correction de typos. [#e8155bb](https://github.com/MTES-MCT/monitorenv/commit/e8155bb)
- Diverses corrections de tests (E2E et unitaires). [#67b51dc](https://github.com/MTES-MCT/monitorenv/commit/67b51dc), [#3e49492](https://github.com/MTES-MCT/monitorenv/commit/3e49492), [#ef6baef](https://github.com/MTES-MCT/monitorenv/commit/ef6baef)
- Corrections suite aux revues de code. [#458d8a5](https://github.com/MTES-MCT/monitorenv/commit/458d8a5), [#96011bb](https://github.com/MTES-MCT/monitorenv/commit/96011bb), [#653e528](https://github.com/MTES-MCT/monitorenv/commit/653e528)
