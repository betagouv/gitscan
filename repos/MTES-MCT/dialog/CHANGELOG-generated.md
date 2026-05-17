## Changelog : dialog (30 derniers jours, au 2026-05-15)

### Résumé
Les dernières mises à jour de dialog se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des arrêtés (recherche, tri, modification après publication) et de la cartographie (tracé libre, légendes, aperçu). Des optimisations de performance ont également été apportées à la carte et à l'import de données.

### Évolutions fonctionnelles
- Possibilité de trier les colonnes de la liste des arrêtés [#1823](https://github.com/MTES-MCT/dialog/issues/1823).
- Ajout de la recherche dans le sélecteur d'organisations [#1824](https://github.com/MTES-MCT/dialog/issues/1824).
- Amélioration du rendu du filtre par organisation, avec une largeur accrue [#1827](https://github.com/MTES-MCT/dialog/issues/1827).
- Ajout du type d'interdiction de dépasser [#1835](https://github.com/MTES-MCT/dialog/issues/1835).
- Affichage de l'utilisateur ayant modifié l'arrêté dans l'historisation [#1836](https://github.com/MTES-MCT/dialog/issues/1836).
- Ajout de la possibilité de modifier un arrêté après sa publication [#1793](https://github.com/MTES-MCT/dialog/issues/1793).
- Ajout de la desserte locale [#1817](https://github.com/MTES-MCT/dialog/issues/1817).
- Affichage de la source de l'arrêté [#1812](https://github.com/MTES-MCT/dialog/issues/1812).
- Ajout de la cartographie dans l'export Word [#1837](https://github.com/MTES-MCT/dialog/issues/1837).
- Affichage des légendes en fonction des tracés cartographiques [#1848](https://github.com/MTES-MCT/dialog/issues/1848).
- Introduction du tracé libre dans le champ GeoJSON sur la carte [#1816](https://github.com/MTES-MCT/dialog/issues/1816).
- Ajout d'un aperçu de la localisation sur la carte [#1790](https://github.com/MTES-MCT/dialog/issues/1790).
- Possibilité d'uploader un arrêté via l'API [#1825](https://github.com/MTES-MCT/dialog/issues/1825).
- Obtention des rues à proximité via l'API [#1809](https://github.com/MTES-MCT/dialog/issues/1809).

### Évolutions techniques
- Améliorations des performances de la carte [#1842](https://github.com/MTES-MCT/dialog/issues/1842).
- Correction de la numérotation des Pull Requests inversée [#1822](https://github.com/MTES-MCT/dialog/issues/1822).
- Correction d'un problème d'intersection sur l'API, retournant une erreur plus explicite [#1814](https://github.com/MTES-MCT/dialog/issues/1814).
- Augmentation de la disponibilité de Datex [#1805](https://github.com/MTES-MCT/dialog/issues/1805).
- Recréation des index BDTOPO via une commande Symfony au lieu de migrations [#1806](https://github.com/MTES-MCT/dialog/issues/1806).
- Amélioration de l'administration des utilisateurs pour les environnements de test [#1815](https://github.com/MTES-MCT/dialog/issues/1815).
- Mise à jour du workflow de l'équipe d'administration [#1841](https://github.com/MTES-MCT/dialog/issues/1841).

### Autres changements
- Améliorations diverses suite aux revues de code [#1839](https://github.com/MTES-MCT/dialog/issues/1839).
- Affichage de l'heure de modification [#1813](https://github.com/MTES-MCT/dialog/issues/1813).
