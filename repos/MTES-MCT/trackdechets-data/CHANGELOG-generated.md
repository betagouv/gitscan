## Changelog : trackdechets-data (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à la plateforme trackdechets-data. Les modifications se concentrent principalement sur l'enrichissement et l'amélioration des modèles de données via dbt, notamment pour le suivi des déchets et l'approbation des révisions de données. Des corrections ont également été apportées pour améliorer la clarté et la précision des données.

### Évolutions fonctionnelles
- Ajout de nouvelles tables d'approbation pour les révisions des données BSDA, BSDD et BSDASRI via dbt [#69](https://github.com/MTES-MCT/trackdechets-data/issues/69).
- Ajout de modèles enrichis pour les registres entrants et sortants, facilitant le suivi des déchets [#65](https://github.com/MTES-MCT/trackdechets-data/issues/65).
- Correction du nom des colonnes dans le modèle `dnd_sortant_observatoires` pour une meilleure clarté [#64](https://github.com/MTES-MCT/trackdechets-data/issues/64).
- Amélioration du filtrage des registres pour exclure les versions annulées et obsolètes [#63](https://github.com/MTES-MCT/trackdechets-data/issues/63).

### Évolutions techniques
- Modification de la stratégie de matérialisation de plusieurs modèles trackdechets de "incremental" à "table" pour optimiser les performances.

### Autres changements
(Aucun changement significatif à signaler)
