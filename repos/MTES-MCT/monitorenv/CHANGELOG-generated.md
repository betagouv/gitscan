## Changelog : monitorenv (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des missions, des données réglementaires et des cartes, ainsi que des corrections de bugs pour une meilleure expérience utilisateur. Des optimisations ont également été apportées à l'API et à l'interface utilisateur.

### Évolutions fonctionnelles
- **Cartographie :** Correction du calcul des coordonnées lors du clic sur la carte pour créer un point.
- **Missions :**
    - Correction de l'affichage des dates des missions dans la liste et dans les rapports.
    - Impossible de sélectionner la même unité de contrôle plusieurs fois dans une mission.
    - Empêche la mise à jour du nombre de personnes concernées lors de la modification de la valeur.
    - Possibilité pour le CACEM de mettre à jour les missions à partir de rapportnav [#40bbc44](https://github.com/MTES-MCT/monitorenv/commit/40bbc44).
- **Données réglementaires :** Correction du flux de mise à jour des zones réglementaires du CACEM et de `regulatory_areas_open_data`.
- **Vaisseaux :** Ajout d'informations supplémentaires et de fichiers aux vaisseaux [#030f5c2](https://github.com/MTES-MCT/monitorenv/commit/030f5c2).
- **Facades maritimes :** L'API des facades maritimes renvoie maintenant le nom distinct de la facade [#5440c30](https://github.com/MTES-MCT/monitorenv/commit/5440c30).
- **Tags de mission :** Correction du filtrage des tags de mission en fonction de la date de début de la mission ou de l'action [#5ca7cd9](https://github.com/MTES-MCT/monitorenv/commit/5ca7cd9).

### Évolutions techniques
- **API :** Utilisation de l'API des facades maritimes au lieu d'un enum pour récupérer les facades [#09be83a](https://github.com/MTES-MCT/monitorenv/commit/09be83a).
- **Refactoring :** Renommage de "facade" en "seafront" pour plus de clarté [#3037a3a](https://github.com/MTES-MCT/monitorenv/commit/3037a3a).
- **Géospatial :** Ajout de `ST_MakeValid` pour les facades maritimes calculées [#89726c5](https://github.com/MTES-MCT/monitorenv/commit/89726c5).
- **Composants UI :** Utilisation du composant `FileUploader` de `monitor-ui` [#6ad6960](https://github.com/MTES-MCT/monitorenv/commit/6ad6960).
- **Gestion des données :** Utilisation de `savedMission` pour conserver les données externes modifiées (ex: calcul de la facade d'action environnementale) [#d658689](https://github.com/MTES-MCT/monitorenv/commit/d658689).

### Autres changements
- Correction de typos [#e8155bb](https://github.com/MTES-MCT/monitorenv/commit/e8155bb).
- Améliorations et corrections de tests (Cypress, Pytest) [#67b51dc](https://github.com/MTES-MCT/monitorenv/commit/67b51dc), [#3e49492](https://github.com/MTES-MCT/monitorenv/commit/3e49492), [#514d0b3](https://github.com/MTES-MCT/monitorenv/commit/514d0b3), [#ef6baef](https://github.com/MTES-MCT/monitorenv/commit/ef6baef).
- Corrections de bugs UX mineurs [#4be2665](https://github.com/MTES-MCT/monitorenv/commit/4be2665).
- Corrections suite aux revues de code [#458d8a5](https://github.com/MTES-MCT/monitorenv/commit/458d8a5), [#96011bb](https://github.com/MTES-MCT/monitorenv/commit/96011bb), [#653e528](https://github.com/MTES-MCT/monitorenv/commit/653e528).
