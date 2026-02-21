## Changelog : sparte (30 derniers jours)

### Résumé
Les dernières mises à jour de sparte se concentrent sur l'amélioration de la gestion des données, notamment l'intégration avec DataGouv et la correction de bugs liés à l'export de données et à la gestion des utilisateurs. De nouvelles fonctionnalités ont été ajoutées pour le suivi de l'évolution du logement vacant et l'analyse du carroyage des sols, offrant ainsi des outils plus performants pour l'analyse de l'artificialisation des sols.

### Évolutions fonctionnelles
- Ajout d'une vue pour le carroyage de la consommation d'espaces (#1434).
- Intégration d'un composant pour afficher l'évolution du taux de logement vacant (#1439).
- Ajout d'un graphique pour visualiser l'évolution du taux de logement vacant.
- Amélioration de la gestion des données d'artificialisation et de consommation avec l'ajout de paramètres utilisateur optionnels pour les graphiques (#1421).
- Correction de l'année affichée dans le rapport local, passant de 2023 à l'année en cours (#1423, #1424).
- Correction d'un problème lié à l'email utilisateur et à la jointure avec Brevo (#1425).
- Ajout de la possibilité d'exporter des données d'artificialisation et d'imperméabilisation par usage et couverture.

### Évolutions techniques
- Refactorisation des modèles SQL pour l'export de données d'artificialisation et d'imperméabilisation.
- Mise à jour des tests pour utiliser `get_dataset_configs` et vérifier les slugs de dataset.
- Suppression de colonnes obsolètes (`target_2031`, `target_2031_modified`) dans le modèle `project`.
- Implémentation de méthodes pour supprimer des datasets et des ressources dans `DataGouvHandler`.
- Ajout de la journalisation des réponses lors de la création et de la mise à jour des datasets dans `DataGouvHandler`.
- Amélioration de la gestion des erreurs lors de la création de datasets dans `DataGouvHandler`.
- Mise à jour de la planification du DAG pour l'exécution quotidienne à 4h00.
- Utilisation de `COALESCE` pour l'email utilisateur et modification du type de jointure avec `brevo_organism`.

### Autres changements
- Ajout de la journalisation pour la création et la mise à jour des datasets dans DataGouvHandler.
- Suppression des tests obsolètes et ajustement des assertions.
- Ajout d'une description pour le carroyage de la consommation d'espaces.
- Amélioration de l'interprétation des messages dans le composant `LogementVacantAutorisation`.
- Correction du formatage des nombres dans les tests.
- Refactorisation des composants `LogementVacant` pour une meilleure gestion des données et de l'affichage.
