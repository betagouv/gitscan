## Changelog : dialog (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en ajoutant de nouvelles fonctionnalités de recherche et de visualisation sur la carte. Des corrections ont également été apportées pour améliorer la stabilité et la performance du système, en particulier concernant le traitement des données DATEX et l'import Literalis. L'administration des utilisateurs et la gestion des arrétés ont également été améliorées.

### Évolutions fonctionnelles
- Ajout d'une prévisualisation cartographique de la localisation [#1790](https://github.com/MTES-MCT/dialog/issues/1790).
- Possibilité de rechercher dans la liste des organisations [#1824](https://github.com/MTES-MCT/dialog/issues/1824).
- Amélioration de l'affichage du filtre par organisation (élargissement de la largeur) [#1827](https://github.com/MTES-MCT/dialog/issues/1827).
- Ajout de la desserte locale [#1817](https://github.com/MTES-MCT/dialog/issues/1817).
- Affichage de la source de l'arrêté [#1812](https://github.com/MTES-MCT/dialog/issues/1812).
- Affichage de l'heure de modification des données [#1813](https://github.com/MTES-MCT/dialog/issues/1813).
- Possibilité de modifier un arrêté après sa publication [#1793](https://github.com/MTES-MCT/dialog/issues/1793).
- Sur la carte, désélectionner toutes les couches sauf 'Circulation interdite' par défaut [#1787](https://github.com/MTES-MCT/dialog/issues/1787).

### Évolutions techniques
- Amélioration de la disponibilité de la source de données Datex [#1805](https://github.com/MTES-MCT/dialog/issues/1805).
- Ajout d'une API pour récupérer les rues à proximité [#1809](https://github.com/MTES-MCT/dialog/issues/1809).
- Recréation des index BDTOPO via une commande Symfony au lieu de migrations [#1806](https://github.com/MTES-MCT/dialog/issues/1806).
- Correction des problèmes de mémoire liés au volume de données DATEX [#1798](https://github.com/MTES-MCT/dialog/issues/1798).
- Traitement synchronisé de la génération du Datex depuis la CI [#1794](https://github.com/MTES-MCT/dialog/issues/1794).
- Correction de l'import Literalis [#1792](https://github.com/MTES-MCT/dialog/issues/1792).
- Correction d'un problème de numérotation inversée des Pull Requests [#1822](https://github.com/MTES-MCT/dialog/issues/1822).
- Suppression des usages dépréciés [#1763](https://github.com/MTES-MCT/dialog/issues/1763).
- Amélioration de l'administration des utilisateurs pour les environnements de test [#1815](https://github.com/MTES-MCT/dialog/issues/1815).

### Autres changements
- Ajout de notifications d'intégration via Mattermost [#1797](https://github.com/MTES-MCT/dialog/issues/1797).
- Retour d'une erreur explicite en cas de problème d'intersection sur l'API [#1814](https://github.com/MTES-MCT/dialog/issues/1814).
