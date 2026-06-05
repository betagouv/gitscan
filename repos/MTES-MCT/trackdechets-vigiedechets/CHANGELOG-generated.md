## Changelog : trackdechets-vigiedechets (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la fonctionnalité de contact/assistance avec l'ajout de la possibilité de joindre plusieurs fichiers. Des corrections ont également été apportées suite à des mises à jour de dépendances et des améliorations techniques ont été réalisées pour faciliter le développement local avec ClickHouse.

### Évolutions fonctionnelles
- Ajout de la possibilité de joindre plusieurs pièces jointes au formulaire de contact de la FAQ/assistance. [#476](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/476)
- Amélioration de la gestion des pièces jointes côté serveur et ajout d'un script pour peupler la base de données de l'assistance. [#476](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/476)

### Évolutions techniques
- Possibilité d'utiliser ClickHouse en local pour le développement. [#464](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/464)
- Correction de problèmes suite à des mises à jour de dépendances. [#490](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/490)
- Mise à jour des dépendances du projet. [#481](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/481), [#483](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/483), [#499](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/499)
- Amélioration de la gestion des lockfiles et des versions de paquets (pnpm).
- Passage à l'utilisation de `generateRegistryV2ExportAsAdmin` pour la génération. [#479](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/479)

### Autres changements
- Application de formatage du code avec `ruff`.
- Corrections mineures et ajustements de tests.
- Nettoyage et simplification du code.
