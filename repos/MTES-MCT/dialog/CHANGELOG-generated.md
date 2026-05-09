## Changelog : dialog (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités clés, notamment en ce qui concerne la cartographie, la gestion des arrêtés et l'intégration de données externes. Des optimisations ont également été apportées pour améliorer la performance et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de tracer librement des zones sur la carte GeoJSON [#1816](https://github.com/MTES-MCT/dialog/issues/1816).
- Intégration de la cartographie dans l'export Word des arrêtés [#1837](https://github.com/MTES-MCT/dialog/issues/1837).
- Ajout du type d'interdiction de dépasser pour les réglementations [#1835](https://github.com/MTES-MCT/dialog/issues/1835).
- Affichage de l'utilisateur ayant modifié un arrêté dans l'historique [#1836](https://github.com/MTES-MCT/dialog/issues/1836).
- Ajout de tris sur les colonnes de la liste des arrêtés [#1823](https://github.com/MTES-MCT/dialog/issues/1823).
- Ajout de la possibilité de rechercher une organisation dans le sélecteur [#1824](https://github.com/MTES-MCT/dialog/issues/1824).
- Amélioration de l'affichage du filtre par organisation (élargissement de la largeur) [#1827](https://github.com/MTES-MCT/dialog/issues/1827).
- Ajout de la notion de desserte locale [#1817](https://github.com/MTES-MCT/dialog/issues/1817).
- Affichage de la source de l'arrêté [#1812](https://github.com/MTES-MCT/dialog/issues/1812).
- Affichage de l'heure de modification d'un arrêté [#1813](https://github.com/MTES-MCT/dialog/issues/1813).
- Possibilité de modifier un arrêté après sa publication [#1793](https://github.com/MTES-MCT/dialog/issues/1793).
- Prévisualisation de la localisation sur la carte [#1790](https://github.com/MTES-MCT/dialog/issues/1790).
- Obtention des rues à proximité via l'API [#1809](https://github.com/MTES-MCT/dialog/issues/1809).

### Évolutions techniques
- Amélioration de la gestion des erreurs d'intersection sur l'API, retournant un message d'erreur plus explicite [#1814](https://github.com/MTES-MCT/dialog/issues/1814).
- Correction de la numérotation inversée des Pull Requests [#1822](https://github.com/MTES-MCT/dialog/issues/1822).
- Augmentation de la disponibilité de la source de données Datex [#1805](https://github.com/MTES-MCT/dialog/issues/1805).
- Correction des problèmes de mémoire liés à la quantité de données DATEX [#1798](https://github.com/MTES-MCT/dialog/issues/1798).
- Recréation des index de la base de données BDTOPO via une commande Symfony au lieu de migrations [#1806](https://github.com/MTES-MCT/dialog/issues/1806).
- Amélioration de l'administration des utilisateurs pour les environnements de test [#1815](https://github.com/MTES-MCT/dialog/issues/1815).

### Autres changements
- Envoi de notifications d'intégration via Mattermost [#1797](https://github.com/MTES-MCT/dialog/issues/1797).
- Améliorations diverses suite aux revues de code [#1839](https://github.com/MTES-MCT/dialog/issues/1839).
