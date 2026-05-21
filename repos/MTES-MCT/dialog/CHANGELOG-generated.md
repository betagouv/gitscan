## Changelog : dialog (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'interface cartographique, l'ajout de nouvelles fonctionnalités pour la gestion des arrêtés (recherche, tris, upload, affichage d'informations complémentaires) et des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations de performance sur la carte ont également été apportées.

### Évolutions fonctionnelles
- **Carte :**
    - Mise à jour des couleurs de la carte pour une meilleure lisibilité. [#1849](https://github.com/MTES-MCT/dialog/issues/1849)
    - Introduction du tracé libre dans le champ GeoJSON, offrant plus de flexibilité pour la définition de zones. [#1816](https://github.com/MTES-MCT/dialog/issues/1816)
    - Ajout d'une prévisualisation de la localisation sur la carte. [#1790](https://github.com/MTES-MCT/dialog/issues/1790)
    - Amélioration des performances de la carte. [#1842](https://github.com/MTES-MCT/dialog/issues/1842)
- **Gestion des arrêtés :**
    - Ajout du type d'interdiction de dépasser. [#1835](https://github.com/MTES-MCT/dialog/issues/1835)
    - Ajout de tris sur les colonnes de la liste des arrêtés pour une organisation plus efficace. [#1823](https://github.com/MTES-MCT/dialog/issues/1823)
    - Possibilité d'uploader un arrêté via l'API. [#1825](https://github.com/MTES-MCT/dialog/issues/1825)
    - Ajout de la recherche dans le sélecteur d'organisations. [#1824](https://github.com/MTES-MCT/dialog/issues/1824)
    - Amélioration du rendu du filtre par organisation. [#1827](https://github.com/MTES-MCT/dialog/issues/1827)
    - Affichage de la source de l'arrêté. [#1812](https://github.com/MTES-MCT/dialog/issues/1812)
    - Affichage de l'heure de modification de l'arrêté. [#1813](https://github.com/MTES-MCT/dialog/issues/1813)
    - Affichage de l'utilisateur ayant modifié l'arrêté dans l'historique. [#1836](https://github.com/MTES-MCT/dialog/issues/1836)
- **Export :** Ajout de la carto dans l'export Word. [#1837](https://github.com/MTES-MCT/dialog/issues/1837)
- **Légendes :** Affichage des légendes en fonction des tracés. [#1848](https://github.com/MTES-MCT/dialog/issues/1848)

### Évolutions techniques
- **Admin :** Correction du workflow de l'équipe admin. [#1841](https://github.com/MTES-MCT/dialog/issues/1841)
- **Admin :** Amélioration de l'administration des utilisateurs pour les environnements de test. [#1815](https://github.com/MTES-MCT/dialog/issues/1815)
- **Datex :** Augmentation de la disponibilité pour Datex. [#1805](https://github.com/MTES-MCT/dialog/issues/1805)
- **API :** Retour d'une erreur explicite lors d'un problème d'intersection sur l'API. [#1814](https://github.com/MTES-MCT/dialog/issues/1814)
- **PR :** Correction de la numérotation inversée des Pull Requests. [#1822](https://github.com/MTES-MCT/dialog/issues/1822)

### Autres changements
- Améliorations générales et revue du code. [#1839](https://github.com/MTES-MCT/dialog/issues/1839)
- Ajout de la desserte locale. [#1817](https://github.com/MTES-MCT/dialog/issues/1817)
