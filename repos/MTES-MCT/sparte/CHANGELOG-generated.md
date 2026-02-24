## Changelog : sparte (30 derniers jours)

### Résumé
Les dernières mises à jour de sparte se concentrent sur l'amélioration de l'analyse de l'artificialisation des sols et de la consommation d'espaces, notamment avec l'ajout d'une nouvelle fonctionnalité de carroyage. Des améliorations ont également été apportées au suivi du logement vacant et à l'intégration avec DataGouv, ainsi que des corrections de bugs pour assurer la fiabilité des données et des rapports.

### Évolutions fonctionnelles
- Ajout d'une vue pour le carroyage des sols, incluant la configuration et l'intégration dans les composants de cartographie et d'information (#1434).
- Amélioration de l'affichage et de la fonctionnalité du carroyage de la consommation d'espaces.
- Ajout d'un composant et d'un graphique pour suivre l'évolution du taux de logement vacant (#1439).
- Refonte des graphiques d'urbanisme et ajout d'une carte du logement vacant.
- Correction de l'affichage de l'année dans le rapport local (#1423, #1424).
- Amélioration de la gestion des erreurs et de la journalisation lors de la création et de la mise à jour des datasets sur DataGouv (#1436, #1437).
- Ajout de paramètres utilisateur optionnels aux constructeurs des graphiques d'artificialisation et de consommation (#1421).
- Correction du traitement des ratios et des messages d'interprétation dans le composant LogementVacantAutorisation (#1439).

### Évolutions techniques
- Refactorisation des modèles SQL pour l'export des données imperméabilisées et artificialisées, avec une utilisation optimisée des index (#1417).
- Mise à jour des tests pour utiliser `get_dataset_configs` et vérification des slugs de dataset. Suppression des tests obsolètes et ajustement des assertions.
- Suppression des colonnes `target_2031` et `target_2031_modified` du modèle `project`.
- Implémentation d'un DAG pour la suppression des datasets de data.gouv.fr et mise à jour des configurations avec des slugs de dataset pour 2026.
- Utilisation de `COALESCE` pour l'email utilisateur et modification du type de jointure avec `brevo_organism` pour améliorer la robustesse.
- Mise à jour de la planification du DAG pour s'exécuter à 4h00 chaque jour.
- Refactorisation des composants LogementVacant pour une meilleure gestion des données et de l'affichage.
- Amélioration du formatage des nombres dans les tests.

### Autres changements
- Ajout de la journalisation des réponses lors de la création et de la mise à jour des datasets dans DataGouvHandler.
- Suppression des références à l'année 2023 dans le rapport local.
