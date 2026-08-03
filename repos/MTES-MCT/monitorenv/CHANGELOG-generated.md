## Changelog : monitorenv (30 derniers jours, au 30 juillet 2026)

### Résumé
Les récentes mises à jour de monitorenv se concentrent sur l'amélioration de la gestion des missions, des données cartographiques et des rapports, avec des corrections de bugs et des optimisations pour une meilleure expérience utilisateur. Des améliorations ont également été apportées à la gestion des navires et des zones réglementaires.

### Évolutions fonctionnelles
- Correction de l'affichage des dates dans les rapports et la liste des missions.
- Amélioration de la gestion des points sur la carte : correction du calcul des coordonnées lors de la création d'un point via un clic sur la carte [#30382aa](https://github.com/MTES-MCT/monitorenv/issues/30382aa).
- Possibilité pour les agents du CACEM de mettre à jour les missions à partir des rapports de navigation [#40bbc44](https://github.com/MTES-MCT/monitorenv/issues/40bbc44).
- Ajout de la possibilité d'ajouter des informations et des fichiers supplémentaires aux navires.
- Correction d'un bug empêchant la sélection multiple de la même unité de contrôle dans une mission [#f5215a6](https://github.com/MTES-MCT/monitorenv/issues/f5215a6).
- Amélioration de l'API pour renvoyer le nom distinct de la façade maritime [#5440c30](https://github.com/MTES-MCT/monitorenv/issues/5440c30).
- Correction du flux de mise à jour des zones réglementaires du CACEM [#7291203](https://github.com/MTES-MCT/monitorenv/issues/7291203).

### Évolutions techniques
- Refactorisation du code pour utiliser l'API facade pour récupérer les informations sur les façades maritimes au lieu d'énumérations [#09be83a](https://github.com/MTES-MCT/monitorenv/issues/09be83a).
- Utilisation de `ST_MakeValid` pour améliorer la validité géométrique des façades maritimes [#89726c5](https://github.com/MTES-MCT/monitorenv/issues/89726c5).
- Mise à jour de l'uploader de fichiers pour utiliser le composant `FileUploader` de `monitor-ui` [#6ad6960](https://github.com/MTES-MCT/monitorenv/issues/6ad6960).
- Correction de l'utilisation de données externes modifiées dans les missions sauvegardées [#d658689](https://github.com/MTES-MCT/monitorenv/issues/d658689).
- Corrections et améliorations suite aux revues de code de Claire Dagan [#96011bb](https://github.com/MTES-MCT/monitorenv/issues/96011bb), [#458d8a5](https://github.com/MTES-MCT/monitorenv/issues/458d8a5).
- Correction de tests unitaires et E2E [#e95b614](https://github.com/MTES-MCT/monitorenv/issues/e95b614), [#67b51dc](https://github.com/MTES-MCT/monitorenv/issues/67b51dc), [#3e49492](https://github.com/MTES-MCT/monitorenv/issues/3e49492), [#ef6baef](https://github.com/MTES-MCT/monitorenv/issues/ef6baef).

### Autres changements
- Correction de typos et amélioration de la lisibilité du code [#e8155bb](https://github.com/MTES-MCT/monitorenv/issues/e8155bb).
- Correction du comportement de la saisie du nombre de personnes pour la sensibilisation [#f960ff6](https://github.com/MTES-MCT/monitorenv/issues/f960ff6).
- Mise à jour des dépendances frontend (prettier, eslint-plugin-prettier, svgo, systeminformation, fast-uri) [#92018d6](https://github.com/MTES-MCT/monitorenv/issues/92018d6), [#31daea2](https://github.com/MTES-MCT/monitorenv/issues/31daea2), [#1e3ec39](https://github.com/MTES-MCT/monitorenv/issues/1e3ec39), [#4aedf7a](https://github.com/MTES-MCT/monitorenv/issues/4aedf7a), [#b568216](https://github.com/MTES-MCT/monitorenv/issues/b568216).
