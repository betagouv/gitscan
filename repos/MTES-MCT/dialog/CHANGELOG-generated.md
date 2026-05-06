## Changelog : dialog (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en ajoutant des tris dans les listes d'arrêtés, en améliorant la recherche et l'affichage des informations, et en optimisant les performances de l'application. Des améliorations significatives ont également été apportées à l'API, notamment pour l'upload d'arrêtés et la recherche de rues à proximité.

### Évolutions fonctionnelles
- Ajout de tris sur les colonnes de la liste des arrêtés [#1823](https://github.com/MTES-MCT/dialog/issues/1823)
- Ajout de la recherche dans le select des organisations [#1824](https://github.com/MTES-MCT/dialog/issues/1824)
- Amélioration du rendu du filtre par organisation en agrandissant la largeur [#1827](https://github.com/MTES-MCT/dialog/issues/1827)
- Ajout de la desserte locale [#1817](https://github.com/MTES-MCT/dialog/issues/1817)
- Affichage de la source de l'arrêté [#1812](https://github.com/MTES-MCT/dialog/issues/1812)
- Affichage de l'heure de modification des arrêtés [#1813](https://github.com/MTES-MCT/dialog/issues/1813)
- Ajout d'une prévisualisation cartographique de la localisation [#1790](https://github.com/MTES-MCT/dialog/issues/1790)
- Possibilité de modifier un arrêté après publication [#1793](https://github.com/MTES-MCT/dialog/issues/1793)
- Envoi de notifications d'intégration via Mattermost [#1797](https://github.com/MTES-MCT/dialog/issues/1797)

### Évolutions techniques
- Ajout de l'upload d'arrêté via l'API [#1825](https://github.com/MTES-MCT/dialog/issues/1825)
- Amélioration de la disponibilité des données Datex [#1805](https://github.com/MTES-MCT/dialog/issues/1805)
- Ajout d'une API pour récupérer les rues à proximité [#1809](https://github.com/MTES-MCT/dialog/issues/1809)
- Correction des problèmes de mémoire liés à la quantité de données DATEX [#1798](https://github.com/MTES-MCT/dialog/issues/1798)
- Traitement synchronisé de la génération du Datex depuis la CI [#1794](https://github.com/MTES-MCT/dialog/issues/1794)
- Correction de l'import Literalis [#1792](https://github.com/MTES-MCT/dialog/issues/1792)
- Recréation des index BDTOPO via une commande Symfony au lieu de migrations [#1806](https://github.com/MTES-MCT/dialog/issues/1806)
- Correction des dépréciations [#1763](https://github.com/MTES-MCT/dialog/issues/1763)
- Correction de la numérotation des Pull Requests inversée [#1822](https://github.com/MTES-MCT/dialog/issues/1822)
- Amélioration de l'administration des utilisateurs pour les environnements de test [#1815](https://github.com/MTES-MCT/dialog/issues/1815)

### Autres changements
- Sur la carte, désélectionner tout sauf 'Circulation interdite' par défaut [#1787](https://github.com/MTES-MCT/dialog/issues/1787)
- Retourner une erreur explicite lors d'un problème d'intersection sur l'API [#1814](https://github.com/MTES-MCT/dialog/issues/1814)
