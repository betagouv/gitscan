## Changelog : trackdechets-vigiedechets (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des données de registre, notamment pour les types de déchets et les tables de données les plus récentes. De nouvelles fonctionnalités sont également introduites pour l'exportation de données et la visualisation cartographique, offrant un meilleur contrôle et une analyse plus approfondie des données de déchets.

### Évolutions fonctionnelles
- Amélioration de l'affichage des origines de déchets par type BSD dans les fiches. [#446](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/446)
- Ajout de la possibilité de spécifier des adresses email autorisées lors de l'exportation de données. [#443](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/443)
- Ajout de métriques cumulées annuelles aux rubriques quotidiennes sur les cartes.
- Correction de l'utilisation des tables de registre les plus récentes (ndw, terres excavées, SSD) pour toutes les données de registre. [#445](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/445)

### Évolutions techniques
- Modification du champ `size` dans le modèle `DataExport` pour utiliser `PositiveBigIntegerField` afin de supporter des tailles plus importantes. [#436](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/436)

### Autres changements
(Aucun changement significatif à signaler)
