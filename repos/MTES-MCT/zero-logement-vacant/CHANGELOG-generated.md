## Changelog : zero-logement-vacant (30 derniers jours, au 08 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances, la refactorisation du code et l'intégration des droits d'accès via le Portail DF. Des corrections de bugs ont également été apportées, notamment concernant la gestion des statuts de logement et l'affichage des noms de périmètres. La documentation technique a été considérablement enrichie.

### Évolutions fonctionnelles
- Amélioration de l'affichage des noms de périmètres dans la liste des logements ([#1757](https://github.com/MTES-MCT/zero-logement-vacant/pull/1757)).
- Intégration des droits d'accès via le Portail DF, permettant de filtrer les données en fonction des autorisations des utilisateurs ([#1649](https://github.com/MTES-MCT/zero-logement-vacant/pull/1649)).
- Ajout de la navigation vers la liste des logements filtrée par campagne ([#1762](https://github.com/MTES-MCT/zero-logement-vacant/pull/1762)).
- Correction de la gestion des statuts de logement "jamais contacté" ([#1794](https://github.com/MTES-MCT/zero-logement-vacant/pull/1794)).

### Évolutions techniques
- Optimisation des performances du comptage des logements, réduisant le temps d'exécution de 4 à 36% selon les filtres ([#1793](https://github.com/MTES-MCT/zero-logement-vacant/pull/1793)).
- Refactorisation importante du code, incluant la suppression de code mort, la simplification de la configuration et la migration vers des outils plus modernes (Vite 8).
- Remplacement de l'index `geo-code` par un index plus performant sur `owners_housing`.
- Migration de l'OpenAPI spec vers un format YAML et remplacement de Swagger UI par Scalar.
- Utilisation de Zod pour la validation de la configuration du serveur.
- Amélioration de la couverture des tests, notamment pour les modèles de données.
- Ajout de factories pour la création d'objets de test.
- Refonte de l'authentification et de la gestion des droits d'accès.
- Suppression de l'ancien flux de campagne.

### Autres changements
- Mise à jour de la documentation technique, incluant des diagrammes et des descriptions détaillées des processus.
- Ajout de badges Codecov et amélioration de la configuration CI/CD.
- Correction de vulnérabilités de dépendances via Snyk.
- Ajout de métriques et d'outils de suivi (PostHog).
- Ajout de l'intégration avec Notion pour le suivi des MCP.
- Ajout de l'intégration avec Claude pour l'analyse des données.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour des dépendances.
