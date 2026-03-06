## Changelog : sparte (30 derniers jours)

### Résumé
Les dernières mises à jour de sparte se concentrent sur l'amélioration de l'analyse du logement vacant, l'ajout d'une fonctionnalité d'analyse du carroyage de la consommation d'espaces et des améliorations générales de l'interface utilisateur. Ces évolutions permettent aux collectivités d'avoir une vision plus complète de l'artificialisation des sols et de la gestion du territoire.

### Évolutions fonctionnelles
- Ajout d'une vue pour afficher les détails d'une parcelle de terrain. [#1443](https://github.com/MTES-MCT/sparte/pull/1443)
- Implémentation de la fonctionnalité de carroyage de la consommation d'espaces, incluant la configuration et l'intégration cartographique. [#1434](https://github.com/MTES-MCT/sparte/pull/1434)
- Ajout d'une description pour le carroyage de la consommation d'espaces dans le composant Consommation.
- Ajout d'un composant et d'un graphique pour suivre l'évolution du taux de logements vacants. [#1439](https://github.com/MTES-MCT/sparte/pull/1439)
- Amélioration de l'interprétation des messages concernant le ratio de logements vacants. [#1439](https://github.com/MTES-MCT/sparte/pull/1439)
- Ajout d'une carte pour visualiser la répartition des logements vacants.
- Refonte des composants liés au logement vacant pour une meilleure gestion et affichage des données.

### Évolutions techniques
- Refactoring des tests pour les graphiques liés au logement vacant, incluant la mise à jour de l'initialisation et le renommage.
- Mise à jour de la gestion des ratios et amélioration des messages d'interprétation dans le composant LogementVacantAutorisation.
- Amélioration des composants CarroyageLeaMap et Consommation pour une meilleure fonctionnalité et un meilleur style.
- Intégration de la configuration du carroyage dans les composants CarroyageLeaMap et CarroyageLeaInfo.

### Autres changements
- Ajout de la vue CarroyageDestinationConfig.
- Ajout d'une couche Carroyage Lea et intégration cartographique.
