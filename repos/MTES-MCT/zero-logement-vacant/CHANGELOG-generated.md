## Changelog : zero-logement-vacant (30 derniers jours)

### Résumé
Les dernières mises à jour de l'application Zero Logement Vacant se concentrent sur l'amélioration de la gestion des documents, l'ajout de nouvelles fonctionnalités de filtrage et d'affichage des informations sur les logements, ainsi que des optimisations techniques et des corrections de bugs pour améliorer la performance et la stabilité de la plateforme. Des améliorations ont également été apportées à l'importation de données et à la sécurité.

### Évolutions fonctionnelles
- Ajout d'un filtre de localisation relative des logements (#1629).
- Possibilité de masquer le nom du propriétaire d'un logement (#1635).
- Amélioration de l'édition des informations DPE (Diagnostic de Performance Énergétique) et affichage de la consommation énergétique réelle (#1571).
- Ajout d'un onglet pour gérer les documents liés à un logement, avec la possibilité de télécharger, renommer et supprimer des documents (#1577, #1601, #1610).
- Affichage de l'ID de parcelle à la place de la référence cadastrale (#1625).
- Amélioration de la gestion des sources de données externes (Insee, DGALN, DGFIP) et correction de bugs associés.
- Mise à jour de la page 404.
- Amélioration de la gestion des droits utilisateurs et filtrage des données en fonction du périmètre Portail DF (#1508).
- Ajout d'un script pour exporter les utilisateurs vers Cerema-scraper (#1633).
- Import des propriétaires depuis Datafoncier 2024 (#1627).

### Évolutions techniques
- Refactorisation de la gestion des documents pour une meilleure architecture et une plus grande flexibilité.
- Mise à jour et optimisation de la configuration NX pour améliorer les performances de build et de test.
- Passage à Vitest 4 et correction des tests associés.
- Utilisation d'esbuild pour la construction du serveur afin d'améliorer la vitesse de compilation.
- Suppression de la bibliothèque Highland et migration vers Web Streams.
- Amélioration de la gestion des événements liés aux documents (création, modification, suppression).
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Mise à jour des dépendances (webpack, axios, express, lodash-es, posthog-js, effect, tar).
- Amélioration de la gestion des erreurs et des logs.
- Correction de bugs et amélioration de la stabilité de l'application.
- Suppression des champs de précision obsolètes.
- Ajout de migrations pour supprimer les colonnes de précision obsolètes de la base de données.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture.
- Ajout de fichiers de configuration pour les agents IA (AGENTS.md).
- Correction de problèmes de configuration CI/CD.
- Mise en production de nouvelles versions de l'application.
- Amélioration de la gestion des secrets et des variables d'environnement.
- Correction de problèmes de typage et de linting.
- Suppression de code inutile et nettoyage du codebase.
- Mise à jour des configurations de déploiement.
- Ajout d'un script pour lister les logements potentiellement erronés.
- Ajout d'un script pour mettre à jour le statut des logements en campagne.
- Correction de la gestion des fuseaux horaires.
- Amélioration de la gestion des erreurs de validation.
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
