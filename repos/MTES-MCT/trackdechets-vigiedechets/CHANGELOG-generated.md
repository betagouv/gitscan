## Changelog : trackdechets-vigiedechets (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à la préparation des fiches d'inspection, notamment au niveau de la visualisation des origines des déchets. Des corrections ont également été apportées pour assurer l'utilisation des données de registre les plus récentes. Enfin, de nouvelles fonctionnalités ont été ajoutées pour la gestion des exports de données et l'affichage de métriques sur les cartes.

### Évolutions fonctionnelles
- Amélioration de l'affichage des origines des déchets sur les fiches d'inspection, regroupées par type de BSD. [#446](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/446)
- Mise à jour des graphiques d'origines des déchets dans les templates de fiches. [#453](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/453)
- Ajout de métriques cumulées annuelles aux rubriques affichées sur les cartes. [#443](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/443)
- Prise en charge de la liste des emails autorisés lors de l'export de données. [#443](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/443)

### Évolutions techniques
- Correction des requêtes pour utiliser les tables `latest_registry_*` pour toutes les données de registre (NDW, terres excavées, SSD). [#445](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/445)
- Refactorisation de l'affichage des origines des déchets dans les fiches. [#446](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/446)
