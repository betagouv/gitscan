## Changelog : qualicharge-carto (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, l'application qualicharge-carto a bénéficié d'améliorations significatives en termes de fonctionnalités de cartographie et de filtrage. De nouvelles options de visualisation, comme les heatmaps et l'analyse des prix, ont été ajoutées, permettant une meilleure compréhension de la répartition et des coûts des bornes de recharge. L'interface utilisateur a également été améliorée, notamment avec la refonte de l'affichage des informations sur les bornes et les points de recharge.

### Évolutions fonctionnelles
- Ajout de heatmaps pour visualiser la densité des bornes de recharge [#f1a66c4](https://github.com/MTES-MCT/qualicharge-carto/commit/f1a66c4).
- Implémentation de l'analyse et de l'affichage des prix sur la carte [#983263a](https://github.com/MTES-MCT/qualicharge-carto/commit/983263a).
- Amélioration des filtres de la carte avec des requêtes sur l'itinérance et l'opérateur [#be855ce](https://github.com/MTES-MCT/qualicharge-carto/commit/be855ce).
- Amélioration de la catégorie de puissance (AFIR) et refonte du regroupement des onglets de connecteurs par puissance et statut PDC [#d88030b](https://github.com/MTES-MCT/qualicharge-carto/commit/d88030b).
- Affichage correct des PDC disponibles, indépendamment de l'énumération `EtatPDCEnum` [#34bf25c](https://github.com/MTES-MCT/qualicharge-carto/commit/34bf25c).
- Utilisation du nombre réel de PDC (`station.pdcs.length`) au lieu d'un indicateur potentiellement inexact [#55d80d8](https://github.com/MTES-MCT/qualicharge-carto/commit/55d80d8).
- Refonte des modes d'affichage de la carte [#aa7b282](https://github.com/MTES-MCT/qualicharge-carto/commit/aa7b282).
- Ajout d'une prévisualisation de l'image Panoramax, inspirée de Chargemap [#32e5605](https://github.com/MTES-MCT/qualicharge-carto/commit/32e5605).
- Ajout de la logique et de l'interface utilisateur pour les options de filtrage [#dcf358c](https://github.com/MTES-MCT/qualicharge-carto/commit/dcf358c).

### Évolutions techniques
- La carte a été déplacée à la racine de l'application web [#69cce35](https://github.com/MTES-MCT/qualicharge-carto/commit/69cce35).
- Refactorisation pour isoler la station du PDC et fusionner les données dynamiques [#dc15b5c](https://github.com/MTES-MCT/qualicharge-carto/commit/dc15b5c) et [#5a7780b](https://github.com/MTES-MCT/qualicharge-carto/commit/5a7780b).
- Mise en place de l'intégration continue avec GitHub Actions (CI) [#ede0cec](https://github.com/MTES-MCT/qualicharge-carto/commit/ede0cec), [#25a96b4](https://github.com/MTES-MCT/qualicharge-carto/commit/25a96b4), [#33d8a41](https://github.com/MTES-MCT/qualicharge-carto/commit/33d8a41), [#dd32b2c](https://github.com/MTES-MCT/qualicharge-carto/commit/dd32b2c), [#cff45c0](https://github.com/MTES-MCT/qualicharge-carto/commit/cff45c0), [#62d907b](https://github.com/MTES-MCT/qualicharge-carto/commit/62d907b).
- Amélioration de l'interface utilisateur de la superposition (overlay) [#060eccd](https://github.com/MTES-MCT/qualicharge-carto/commit/060eccd).

### Autres changements
- Correction d'erreurs typographiques [#7f4ab63](https://github.com/MTES-MCT/qualicharge-carto/commit/7f4ab63).
- Correction d'un bug empêchant les champs de recherche de filtre de se réinitialiser correctement [#0a5886a](https://github.com/MTES-MCT/qualicharge-carto/commit/0a5886a).
