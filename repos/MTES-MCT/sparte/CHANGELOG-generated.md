## Changelog : sparte (30 derniers jours)

### Résumé
Les dernières mises à jour de sparte se concentrent sur l'amélioration de la fonctionnalité de suivi du logement vacant, l'ajout d'une nouvelle fonctionnalité de carroyage pour l'analyse de la consommation d'espaces, et des corrections concernant l'intégration avec DataGouv. Ces améliorations visent à fournir aux collectivités des outils plus performants pour analyser et maîtriser l'artificialisation des sols.

### Évolutions fonctionnelles
- Ajout d'une nouvelle vue pour l'analyse du carroyage de la consommation d'espaces (#1434).
- Intégration de la configuration du carroyage dans les composants cartographiques et d'information.
- Ajout d'un composant et d'un graphique pour le suivi de l'évolution du taux de logements vacants (#1439).
- Amélioration de l'interprétation des messages et de la gestion des ratios dans le composant LogementVacantAutorisation (#1439).
- Ajout d'une carte pour visualiser les données de logements vacants.
- Ajout d'une description pour le carroyage de la consommation d'espaces dans le composant Consommation.

### Évolutions techniques
- Refactoring des composants liés au logement vacant pour améliorer la gestion des données et l'affichage.
- Refactoring des tests pour les graphiques de logements vacants, avec renommage et mise à jour de l'initialisation de `TauxProgressionChart`.
- Suppression des colonnes `target_2031` et `target_2031_modified` du modèle `project` (#1437).
- Modification de la structure du payload lors de la création et de la mise à jour des datasets dans `DataGouvHandler` pour encapsuler l'identifiant de l'organisation.
- Amélioration de la gestion des erreurs et ajout de la journalisation lors de la création et de la mise à jour des datasets dans `DataGouvHandler` (#1436, #1437).

### Autres changements
- Ajout de la journalisation des réponses lors de la création et de la mise à jour des datasets dans `DataGouvHandler`.
- Mise à jour des tests `formatNumber` pour retourner "-" pour les entrées `undefined`, `null` et `NaN`.
