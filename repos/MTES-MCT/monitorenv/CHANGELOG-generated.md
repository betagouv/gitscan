## Changelog : monitorenv (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des missions, des données réglementaires et des cartes, ainsi que des corrections de bugs et des optimisations de l'interface utilisateur. Les agents du CACEM bénéficieront d'une expérience plus fluide et précise dans leurs tâches quotidiennes.

### Évolutions fonctionnelles
- **Cartographie :** Correction du calcul des coordonnées lors du clic sur la carte pour créer un point [#30382aa](https://github.com/MTES-MCT/monitorenv/issues/30382aa).
- **Rapports & Missions :** Correction de l'affichage des dates dans les rapports et la liste des missions. [#98131b9](https://github.com/MTES-MCT/monitorenv/issues/98131b9), [#8da9a9c](https://github.com/MTES-MCT/monitorenv/issues/8da9a9c), [#d96c8ad](https://github.com/MTES-MCT/monitorenv/issues/d96c8ad), [#535ef99](https://github.com/MTES-MCT/monitorenv/issues/535ef99).
- **Missions :**
    - Empêche la sélection multiple de la même unité de contrôle dans une mission [#f5215a6](https://github.com/MTES-MCT/monitorenv/issues/f5215a6).
    - Empêche la mise à jour du nombre de personnes concernées lors de la modification de la valeur de l'input [#f960ff6](https://github.com/MTES-MCT/monitorenv/issues/f960ff6).
- **Données réglementaires :** Correction du flux de mise à jour des zones réglementaires du CACEM et des données `regulatory_areas_open_data`. [#7291203](https://github.com/MTES-MCT/monitorenv/issues/7291203), [#43554f4](https://github.com/MTES-MCT/monitorenv/issues/43554f4).
- **Navires :** Ajout de la possibilité d'ajouter des informations supplémentaires et des fichiers aux navires. [#653e528](https://github.com/MTES-MCT/monitorenv/issues/653e528).
- **Facades maritimes :** L'API des facades maritimes renvoie maintenant le nom distinct de la facade. [#5440c30](https://github.com/MTES-MCT/monitorenv/issues/5440c30). Correction de l'utilisation de `ST_MakeValid` pour le calcul des facades maritimes. [#89726c5](https://github.com/MTES-MCT/monitorenv/issues/89726c5). Utilisation de l'API facades pour récupérer les facades au lieu d'un enum. [#09be83a](https://github.com/MTES-MCT/monitorenv/issues/09be83a). Affichage du label de la facade au lieu de sa valeur dans le panel. [#49a52cd](https://github.com/MTES-MCT/monitorenv/issues/49a52cd).

### Évolutions techniques
- **Tests :** Corrections de plusieurs tests unitaires et E2E. [#e95b614](https://github.com/MTES-MCT/monitorenv/issues/e95b614), [#67b51dc](https://github.com/MTES-MCT/monitorenv/issues/67b51dc), [#3e49492](https://github.com/MTES-MCT/monitorenv/issues/3e49492), [#ef6baef](https://github.com/MTES-MCT/monitorenv/issues/ef6baef), [#96011bb](https://github.com/MTES-MCT/monitorenv/issues/96011bb).
- **Frontend :** Mise à jour de Prettier et correction des erreurs de linting. [#92018d6](https://github.com/MTES-MCT/monitorenv/issues/92018d6), [#19c277a](https://github.com/MTES-MCT/monitorenv/issues/19c277a).
- **Architecture :** Refactoring pour utiliser le composant `FileUploader` de `monitor-ui`. [#6ad6960](https://github.com/MTES-MCT/monitorenv/issues/6ad6960).
- **Missions :** Utilisation de `savedMission` pour conserver les données externes modifiées lors de la mise à jour d'une mission. [#d658689](https://github.com/MTES-MCT/monitorenv/issues/d658689).

### Autres changements
- Correction d'une faute de frappe dans le titre des zones en bord de mer. [#e8155bb](https://github.com/MTES-MCT/monitorenv/issues/e8155bb).
- Correction permettant au CACEM de mettre à jour une mission à partir d'un rapport de navigation. [#40bbc44](https://github.com/MTES-MCT/monitorenv/issues/40bbc44).
