## Changelog : dialog (30 derniers jours, au 2026-05-13)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la cartographie, de l'administration des arrêtés, et de l'API. Des fonctionnalités ont été ajoutées pour faciliter la modification des arrêtés après publication, l'ajout de types de restrictions (interdiction de dépasser), et l'amélioration de la recherche et du filtrage. Des optimisations de performance ont également été apportées à la carte.

### Évolutions fonctionnelles
- Ajout de la possibilité de tracer librement des zones géographiques sur la carte pour une localisation précise. [#1816](https://github.com/MTES-MCT/dialog/issues/1816)
- Intégration de la cartographie dans l'export Word des arrêtés, permettant une visualisation contextuelle. [#1837](https://github.com/MTES-MCT/dialog/issues/1837)
- Ajout du type de restriction "interdiction de dépasser". [#1835](https://github.com/MTES-MCT/dialog/issues/1835)
- Possibilité de modifier un arrêté après sa publication. [#1793](https://github.com/MTES-MCT/dialog/issues/1793)
- Ajout de la desserte locale. [#1817](https://github.com/MTES-MCT/dialog/issues/1817)
- Amélioration de la recherche dans le sélecteur d'organisations. [#1824](https://github.com/MTES-MCT/dialog/issues/1824)
- Amélioration du rendu du filtre par organisation (élargissement de la largeur). [#1827](https://github.com/MTES-MCT/dialog/issues/1827)
- Ajout de tris sur les colonnes de la liste des arrêtés. [#1823](https://github.com/MTES-MCT/dialog/issues/1823)
- Affichage de la source de l'arrêté. [#1812](https://github.com/MTES-MCT/dialog/issues/1812)
- Affichage de l'heure de modification de l'arrêté. [#1813](https://github.com/MTES-MCT/dialog/issues/1813)
- Ajout d'une prévisualisation de la localisation sur la carte. [#1790](https://github.com/MTES-MCT/dialog/issues/1790)
- Ajout de la possibilité d'uploader un arrêté via l'API. [#1825](https://github.com/MTES-MCT/dialog/issues/1825)
- Affichage de l'utilisateur ayant effectué la dernière modification de l'arrêté. [#1836](https://github.com/MTES-MCT/dialog/issues/1836)

### Évolutions techniques
- Amélioration des performances de la carte. [#1842](https://github.com/MTES-MCT/dialog/issues/1842)
- Refonte de la création des index BDTOPO via une commande Symfony au lieu de migrations. [#1806](https://github.com/MTES-MCT/dialog/issues/1806)
- Amélioration de la disponibilité de Datex. [#1805](https://github.com/MTES-MCT/dialog/issues/1805)
- Ajout de la récupération des rues à proximité via l'API. [#1809](https://github.com/MTES-MCT/dialog/issues/1809)
- Correction de la numérotation inversée des Pull Requests. [#1822](https://github.com/MTES-MCT/dialog/issues/1822)
- Amélioration de l'administration des utilisateurs pour les environnements de test. [#1815](https://github.com/MTES-MCT/dialog/issues/1815)
- Retour d'une erreur explicite lors d'un problème d'intersection sur l'API. [#1814](https://github.com/MTES-MCT/dialog/issues/1814)

### Autres changements
- Mise à jour du workflow de l'équipe d'administration. [#1841](https://github.com/MTES-MCT/dialog/issues/1841)
- Améliorations diverses suite aux revues de code. [#1839](https://github.com/MTES-MCT/dialog/issues/1839)
