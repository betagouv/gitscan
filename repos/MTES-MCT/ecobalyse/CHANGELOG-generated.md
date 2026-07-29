## Changelog : ecobalyse (30 derniers jours, au 28 juillet 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données (notamment pour les véhicules, l'alimentation et les matières premières agricoles), l'amélioration de l'expérience utilisateur (ajout de fonctionnalités et corrections de bugs) et des optimisations techniques pour une meilleure performance et sécurité. Des améliorations ont également été apportées à l'API et à l'infrastructure.

### Évolutions fonctionnelles
- Ajout de la possibilité de localiser les nouvelles transformations avec des valeurs par défaut pertinentes.
- Amélioration de l'interface utilisateur pour la résolution du nom complet des régions.
- Ajout d'une option pour ajouter un seul élément de production.
- Restriction de l'accès aux impacts détaillés pour les utilisateurs non authentifiés.
- Ajout d'exemples d'articles alimentaires (pizza, etc.) pour faciliter l'utilisation.
- Ajout d'une fonctionnalité permettant d'exporter les données Ecospold1.
- Ajout de la possibilité de définir un lien de feedback.
- Implémentation de commandes API authentifiées.
- Ajout de la gestion des transports réfrigérés lorsque disponibles.
- Ajout de la prise en charge de l'importation de données BAFU à partir d'un export CSV Simapro.
- Ajout de la prise en charge de la modélisation des véhicules selon la réglementation EV.
- Ajout de processus intégrant le kilométrage pour la phase d'utilisation des véhicules.
- Ajout de la possibilité de configurer des liens vers la documentation.

### Évolutions techniques
- Utilisation de la base de données ecobalyse-data pour l'historique des scores.
- Optimisation de la vitesse de récupération de l'historique des scores.
- Refactorisation du code pour améliorer la cohérence et la maintenabilité.
- Mise à jour des dépendances (Litestar, sentry-sdk, pytest-databases, etc.).
- Amélioration de la sécurité en empêchant la falsification du jeton d'authentification.
- Migration pour resynchroniser la base de données et les modèles.
- Ajout d'une tâche planifiée pour l'historique des scores.
- Amélioration de la gestion des processus et des schémas.
- Correction de problèmes de configuration et de tests.

### Autres changements
- Corrections de données pour l'aluminium et l'acier.
- Corrections de données pour les ingrédients du poisson.
- Suppression de la duplication du schéma des processus.
- Corrections de tests de données.
- Nettoyage et mise à jour de données agricoles (sorgho, seigle, lin, haricot, amarande, etc.).
- Mise à jour des données de consommation des véhicules.
- Corrections de nommage de composants.
- Ajout de la région Maghreb.
- Ajout d'un tag `productmassdependent`.
- Amélioration de la gestion des transports.
- Ajout de la prise en charge de l'électricité en kWh.
- Correction de l'affichage des ratios de transport routier/maritime.
