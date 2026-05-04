## Changelog : zero-logement-vacant (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la robustesse de l'application, notamment au niveau du traitement des données et de l'intégration avec les systèmes externes (CEREMA, Portail DF). Des améliorations significatives ont également été apportées à la documentation technique et à l'expérience utilisateur, avec des corrections de bugs et des optimisations de l'interface.

### Évolutions fonctionnelles
- Amélioration du matching d'adresses avec des règles de normalisation et un seuil abaissé à 0.85.
- Ajout de notifications lors de la création d'une campagne et de la suppression d'un groupe.
- Correction de l'affichage des pourcentages avec une décimale par défaut.
- Correction de l'affichage des noms de filtres de périmètre.
- Correction du comportement du bouton d'action de masse des groupes.
- Correction de l'affichage des images en brouillon lors du téléversement.
- Amélioration de la gestion des droits d'accès via le Portail DF, incluant la vérification des droits lors de la connexion et de la création de compte.
- Correction de l'état actif de la navigation pour la section "Parc de logements".
- Correction de l'affichage des informations sur les propriétaires principaux.

### Évolutions techniques
- Refactorisation de la configuration du serveur avec l'utilisation de Zod pour la validation et la gestion des variables d'environnement.
- Suppression de l'utilisation de Convict et remplacement par Zod.
- Mise à jour de Vite en version 8 et des plugins associés.
- Amélioration des performances des requêtes Dbt en optimisant le matching des propriétaires et en utilisant des tables matérialisées.
- Ajout de pipelines pour la génération de données ZLOVAC.
- Amélioration de la gestion des erreurs et de la robustesse du code.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Utilisation de statement-level triggers pour optimiser les mises à jour des comptages de groupes.
- Refactorisation de l'API Geo pour améliorer les performances et la maintenabilité.
- Mise en place d'un système de documentation automatique avec Swagger/OpenAPI.
- Amélioration de la gestion des dépendances et des configurations CI/CD.
- Ajout de l'outil Knip pour l'analyse des dépendances et la détection des dépendances inutilisées.

### Autres changements
- Mise à jour de la documentation technique avec des informations sur l'architecture, les API et les processus de déploiement.
- Ajout de documentation sur l'implémentation des "superpowers".
- Correction de problèmes de compatibilité avec macOS dans l'environnement CI.
- Suppression de code mort et de dépendances inutilisées.
- Amélioration de la qualité du code et de la lisibilité.
- Mise à jour des dépendances et des outils de développement.
- Ajout de badges Codecov pour le suivi de la couverture de test.
- Ajout de configuration Worktrunk pour faciliter le développement et les tests.
- Correction de problèmes liés à la génération de diagrammes Mermaid.
- Ajout de commentaires et de documentation pour améliorer la compréhension du code.
