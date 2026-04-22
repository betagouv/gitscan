## Changelog : dialog (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la performance du traitement des données réglementaires, notamment concernant les flux Datex et Literalis. Des corrections ont été apportées pour améliorer la stabilité de l'import de données et la gestion de la mémoire. De nouvelles fonctionnalités permettent d'obtenir les rues à proximité et de modifier un arrêté après publication. L'interface utilisateur a également été améliorée avec une désélection par défaut sur la carte.

### Évolutions fonctionnelles
- Possibilité de récupérer les rues à proximité via l'API. [#1809](https://github.com/MTES-MCT/dialog/issues/1809)
- Modification d'un arrêté après sa publication est maintenant possible. [#1793](https://github.com/MTES-MCT/dialog/issues/1793)
- Amélioration de l'interface cartographique : désélection de toutes les couches par défaut, sauf "Circulation interdite". [#1787](https://github.com/MTES-MCT/dialog/issues/1787)
- Notifications d'intégration envoyées via Mattermost. [#1797](https://github.com/MTES-MCT/dialog/issues/1797)

### Évolutions techniques
- Amélioration de la disponibilité du flux Datex. [#1805](https://github.com/MTES-MCT/dialog/issues/1805)
- Correction des problèmes de mémoire liés au traitement des données Datex. [#1798](https://github.com/MTES-MCT/dialog/issues/1798)
- Optimisation du traitement du flux Datex en utilisant le streaming. [#1771](https://github.com/MTES-MCT/dialog/issues/1771)
- Refonte de l'import Literalis avec un nouveau client WFS. [#1724](https://github.com/MTES-MCT/dialog/issues/1724)
- Correction de l'import Literalis. [#1792](https://github.com/MTES-MCT/dialog/issues/1792) et [#1773](https://github.com/MTES-MCT/dialog/issues/1773)
- Amélioration de la gestion des index de la base de données BDTOPO via une commande Symfony. [#1806](https://github.com/MTES-MCT/dialog/issues/1806)
- Configuration de la CI pour le nouveau flux Literalis. [#1770](https://github.com/MTES-MCT/dialog/issues/1770)
- Correction de la CI. [#1767](https://github.com/MTES-MCT/dialog/issues/1767)

### Autres changements
- Suppression des usages dépréciés. [#1763](https://github.com/MTES-MCT/dialog/issues/1763)
- POC de génération de fichiers statiques pour l'API des réglementations. [#1772](https://github.com/MTES-MCT/dialog/issues/1772)
