## Changelog : sparte (30 derniers jours)

### Résumé
Les dernières mises à jour de sparte apportent des améliorations significatives à l'analyse de l'artificialisation des sols et de la consommation d'espaces, notamment avec l'ajout de nouvelles fonctionnalités de carroyage et de visualisation des données de logement vacant. Des corrections ont également été apportées pour améliorer la gestion des données, l'intégration avec DataGouv et l'expérience utilisateur globale. L'application a été optimisée pour mieux gérer les données des utilisateurs DGALN et inclut un suivi des liens sortants via Matomo.

### Évolutions fonctionnelles
- Ajout de la vue Carroyage pour l'analyse de la consommation d'espaces (#1434).
- Intégration de la configuration du carroyage dans les composants CarroyageLeaMap et CarroyageLeaInfo (#1434).
- Ajout d'un composant LogementVacantTaux pour suivre l'évolution du taux de logements vacants (#1439).
- Ajout d'une carte LogementVacant pour visualiser les données de logements vacants (#1439).
- Amélioration de la visibilité des objectifs territorialisés pour les membres DGALN (#1418).
- Ajout d'un paramètre utilisateur optionnel aux constructeurs des graphiques d'artificialisation et de consommation (#1421).
- Suppression des références à l'année 2023 dans le rapport local (#1423, #1424).
- Suivi des clics sur les liens sortants via Matomo (#1415).

### Évolutions techniques
- Refactor des modèles SQL pour l'export des données imperméabilisées et artificialisées par usage et couverture (#1431).
- Ajout d'un DAG pour supprimer tous les datasets de data.gouv.fr et mise à jour des configurations avec des slugs de dataset pour 2026 (#1431).
- Amélioration de la gestion des erreurs et de la journalisation dans DataGouvHandler (#1436, #1437).
- Modification de la structure du payload lors de la création et de la mise à jour des datasets dans DataGouvHandler (#1437).
- Utilisation de COALESCE pour l'email utilisateur et modification du type de jointure avec brevo_organism (#1425).
- Refactor des composants LogementVacant pour une meilleure gestion des données et de l'affichage (#1439).
- Refactor des tests pour LogementVacant charts (#1439).
- Suppression des colonnes target_2031 et target_2031_modified dans le modèle project (#1417).
- Ajout d'un DAG pour ingérer les données de brevo_user_organism et création des fichiers SQL associés (#1416).

### Autres changements
- Mise à jour des tests pour utiliser `get_dataset_configs` et vérification des slugs de dataset (#1431).
- Ajustement de la planification du DAG pour s'exécuter à 4h00 chaque jour (#1425).
- Amélioration de la logique de visibilité des objectifs territorialisés pour les membres DGALN (#1418).
