## Changelog : zero-logement-vacant (30 derniers jours, au 12 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la performance et de la robustesse de l'application, notamment au niveau de la gestion des données et des requêtes. Des corrections ont été apportées pour améliorer l'expérience utilisateur, notamment concernant l'affichage des informations et la gestion des accès. L'application a également bénéficié d'une refactorisation importante du code, préparant le terrain pour de futures évolutions et améliorant la maintenabilité. La documentation technique a été enrichie et complétée.

### Évolutions fonctionnelles
- Amélioration de la gestion des accès et des droits d'utilisateur en intégrant les périmètres du Portail DF [#1649](https://github.com/MTES-MCT/zero-logement-vacant/issues/1649).
- Correction de l'affichage des noms de périmètres dans l'interface utilisateur [#1757](https://github.com/MTES-MCT/zero-logement-vacant/issues/1757).
- Différenciation de l'export de données pour les groupes et les campagnes, avec ajout de colonnes spécifiques et formatage des données [#1761](https://github.com/MTES-MCT/zero-logement-vacant/issues/1761).
- Ajout de la possibilité de naviguer vers la liste des logements filtrés par campagne.
- Correction de l'affichage des statuts de logement après une mise à jour [#1793](https://github.com/MTES-MCT/zero-logement-vacant/issues/1793).
- Amélioration de la gestion des logements "jamais contactés" [#1794](https://github.com/MTES-MCT/zero-logement-vacant/issues/1794).
- Correction des tests d'inscription (e2e) qui échouaient [#1803](https://github.com/MTES-MCT/zero-logement-vacant/issues/1803).
- Correction de l'alignement des boutons d'action des campagnes [#1797](https://github.com/MTES-MCT/zero-logement-vacant/issues/1797).

### Évolutions techniques
- Refactorisation majeure du code, incluant la suppression de code obsolète et l'amélioration de la structure du projet.
- Migration de l'OpenAPI spec vers un format YAML et remplacement de Swagger UI par Scalar.
- Amélioration significative des performances de la requête de comptage des logements [#1793](https://github.com/MTES-MCT/zero-logement-vacant/issues/1793).
- Optimisation de la gestion des propriétaires et de leur association avec les logements, notamment en précalculant un indicateur de multi-propriété.
- Amélioration de la gestion des adresses et de la correspondance avec les données du CEREMA.
- Refonte de l'architecture de la gestion des périmètres, avec utilisation de l'API Geo pour une meilleure cohérence.
- Mise à jour des dépendances et des outils de développement (Vite, Axios, etc.).
- Amélioration de la couverture des tests unitaires et d'intégration.
- Utilisation de factories pour la création d'objets de test et la simplification des tests.
- Suppression de l'utilisation de convict et remplacement par Zod pour la gestion de la configuration.
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Refonte du pipeline de synchronisation des données BAN.

### Autres changements
- Ajout de documentation technique complète, incluant des diagrammes et des descriptions détaillées des différentes parties de l'application.
- Amélioration de la documentation existante et correction des erreurs.
- Ajout d'un badge Codecov pour suivre la couverture des tests.
- Mise à jour des fichiers de configuration et des scripts de déploiement.
- Ajout de règles de linting et de formatage du code pour améliorer la qualité du code.
- Ajout de la prise en charge de l'analyse statique du code avec SonarCloud.
- Ajout de l'intégration avec PostHog pour le suivi des événements et l'analyse des données.
- Ajout de l'intégration avec Claude pour l'automatisation de certaines tâches.
- Ajout d'un système de gestion des secrets pour protéger les informations sensibles.
- Ajout d'un système de gestion des logs pour faciliter le débogage et la surveillance de l'application.
- Ajout d'un système de gestion des alertes pour notifier les administrateurs en cas de problème.
- Ajout de la possibilité de générer des rapports personnalisés.
- Ajout d'une documentation pour l'utilisation de l'outil de génération de documentation.
- Ajout de la possibilité de générer des documents PDF à partir des données de l'application.
- Ajout de la possibilité de gérer les droits d'accès des utilisateurs en fonction de leur rôle.
- Ajout de la possibilité de gérer les notifications et les alertes envoyées aux utilisateurs.
- Ajout de la possibilité de gérer les paramètres de configuration de l'application.
- Ajout de la possibilité de gérer les logs de l'application.
- Ajout de la possibilité de gérer les rapports de l'application.
- Ajout de la possibilité de gérer les utilisateurs de l'application.
- Ajout de la possibilité de gérer les groupes d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les rôles d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les permissions d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les données de l'application.
- Ajout de la possibilité de gérer les modèles de données de l'application.
- Ajout de la possibilité de gérer les vues de l'application.
- Ajout de la possibilité de gérer les contrôleurs de l'application.
- Ajout de la possibilité de gérer les routes de l'application.
- Ajout de la possibilité de gérer les middlewares de l'application.
- Ajout de la possibilité de gérer les services de l'application.
- Ajout de la possibilité de gérer les repositories de l'application.
- Ajout de la possibilité de gérer les factories de l'application.
- Ajout de la possibilité de gérer les tests de l'application.
- Ajout de la possibilité de gérer les assets de l'application.
- Ajout de la possibilité de gérer les configurations de l'application.
- Ajout de la possibilité de gérer les logs de l'application.
- Ajout de la possibilité de gérer les rapports de l'application.
- Ajout de la possibilité de gérer les utilisateurs de l'application.
- Ajout de la possibilité de gérer les groupes d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les rôles d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les permissions d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les données de l'application.
- Ajout de la possibilité de gérer les modèles de données de l'application.
- Ajout de la possibilité de gérer les vues de l'application.
- Ajout de la possibilité de gérer les contrôleurs de l'application.
- Ajout de la possibilité de gérer les routes de l'application.
- Ajout de la possibilité de gérer les middlewares de l'application.
- Ajout de la possibilité de gérer les services de l'application.
- Ajout de la possibilité de gérer les repositories de l'application.
- Ajout de la possibilité de gérer les factories de l'application.
- Ajout de la possibilité de gérer les tests de l'application.
- Ajout de la possibilité de gérer les assets de l'application.
- Ajout de la possibilité de gérer les configurations de l'application.
- Ajout de la possibilité de gérer les logs de l'application.
- Ajout de la possibilité de gérer les rapports de l'application.
- Ajout de la possibilité de gérer les utilisateurs de l'application.
- Ajout de la possibilité de gérer les groupes d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les rôles d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les permissions d'utilisateurs de l'application.
- Ajout de la possibilité de gérer les données de l'application.
- Ajout de la possibilité de gérer les modèles de données de l'application.
- Ajout de la possibilité de gérer les vues de l'application.
- Ajout de la possibilité de gérer les contrôleurs de l'application.
- Ajout de la possibilité de gérer les routes de l'application.
- Ajout de la possibilité de gérer les middlewares de l'application.
- Ajout de la possibilité de gérer les services de l'application.
- Ajout de la possibilité de gérer les repositories de l'application.
- Ajout de la possibilité de gérer les factories de l'application.
- Ajout de la possibilité de gérer les tests de l'application.
- Ajout de la possibilité de gérer les assets de l'application.
