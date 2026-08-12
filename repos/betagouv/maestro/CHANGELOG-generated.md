## Changelog : maestro (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la précision des données et de l'expérience utilisateur. De nouvelles fonctionnalités ont été ajoutées, notamment des statistiques sur le tableau de bord et de nouveaux filtres de recherche. Plusieurs corrections ont également été apportées pour fiabiliser l'intégration des données provenant de différents laboratoires et partenaires.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
  - Ajout de statistiques sur le tableau de bord [#949](https://github.com/betagouv/maestro/issues/949).
  - Ajout d'un filtre par date d'envoi pour les prélèvements (DAI) [#1231](https://github.com/betagouv/maestro/issues/1231).
  - Intégration de la substance active "cyprosulfamide" dans le référentiel [#1246](https://github.com/betagouv/maestro/issues/1246).
  - Gestion d'un fichier déclencheur lors de l'envoi de DAI via SFTP [#1289](https://github.com/betagouv/maestro/issues/1289).
- **Améliorations et corrections**
  - **Tableau de bord :** Correction de l'affichage des détails des prélèvements et de la récupération des conformités [#1288](https://github.com/betagouv/maestro/issues/1288), [#1262](https://github.com/betagouv/maestro/issues/1262).
  - **Intégration laboratoires :** Diverses corrections pour fiabiliser la récupération des données (Inovalys, Girpa, Cereco, Labcam) et la gestion des matrices [#1276](https://github.com/betagouv/maestro/issues/1276), [#1275](https://github.com/betagouv/maestro/issues/1275), [#1265](https://github.com/betagouv/maestro/issues/1265), [#1264](https://github.com/betagouv/maestro/issues/1264), [#1213](https://github.com/betagouv/maestro/issues/1213), [#1274](https://github.com/betagouv/maestro/issues/1274).
  - **Interface utilisateur :** Optimisation de l'affichage des détails d'échantillons, des noms de documents et de l'historique des rapports [#1229](https://github.com/betagouv/maestro/issues/1229), [#1232](https://github.com/betagouv/maestro/issues/1232), [#1230](https://github.com/betagouv/maestro/issues/1230).
  - **Corrections diverses :** Rectification du tableau de programmation en vue nationale [#1155](https://github.com/betagouv/maestro/issues/1155) et du formatage des références [#1263](https://github.com/betagouv/maestro/issues/1263).

### Évolutions techniques
- **Performance et architecture**
  - Optimisation de la consommation de mémoire vive (RAM) en modifiant le mode de mise à jour des départements [#1260](https://github.com/betagouv/maestro/issues/1260).
  - Refactorisation du code d'extraction des références Maestro pour les laboratoires afin de centraliser la logique [#1247](https://github.com/betagouv/maestro/issues/1247).
- **Outils et Build**
  - Nettoyage des avertissements (warnings) de l'outil de build Vite [#1261](https://github.com/betagouv/maestro/issues/1261).
  - Mise à jour de la gestion des scripts via le passage de `npm-run-all` à `npm-run-all2` [#1243](https://github.com/betagouv/maestro/issues/1243).
