## Changelog : territoires-en-transitions (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des plans d'action, notamment avec la possibilité de les dupliquer, et sur l'import de plans via un nouveau module dédié. Des améliorations significatives ont également été apportées à l'interface utilisateur, en particulier pour la gestion des actions et des preuves, ainsi qu'à la sécurité et à la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de dupliquer un plan d'action, incluant les budgets et les preuves associées.
- Nouvelle fonctionnalité permettant de générer une archive ZIP des preuves d'audit, accessible uniquement aux auditeurs.
- Amélioration de la vue des actions avec une nouvelle interface tabulaire (activable via un *feature flag*).
- Possibilité d'éditer les actions directement depuis le tableau des actions.
- Ajout d'un bandeau pour faciliter l'accès à la nouvelle vue de labellisation.
- Amélioration de l'affichage du statut d'audit et des badges associés.
- Ajout de la possibilité de filtrer les actions par statut et priorité.
- Amélioration de l'affichage des sous-mesures et des indicateurs.
- Correction de bugs liés à l'affichage des données et à la gestion des accès.
- Amélioration de la gestion des commentaires sur les sous-mesures.
- Ajout d'un indicateur visuel pour les actions privées.
- Amélioration de l'expérience utilisateur pour la gestion des tâches.

### Évolutions techniques
- Refactor important du code pour migrer les labels JSX vers un système centralisé (`appLabels`) pour une meilleure maintenabilité.
- Implémentation d'un nouveau module pour l'import de plans d'action, incluant la gestion des erreurs et la validation des données.
- Utilisation de Drizzle pour la gestion de la base de données dans le module d'import.
- Amélioration de la sécurité avec des corrections pour prévenir les injections SQL et les IDOR (Insecure Direct Object Reference).
- Mise à jour des dépendances et des outils de développement (Next.js, eslint, Playwright).
- Optimisation des performances avec la suppression de dépendances inutiles et l'amélioration du code.
- Amélioration de la gestion des erreurs et de la journalisation.
- Refactor de la gestion des accès et des permissions.
- Utilisation de TypeScript pour une meilleure typage et une détection plus précoce des erreurs.
- Amélioration de la structure du code et de la documentation.
- Migration des tests Cypress vers Vitest.

### Autres changements
- Ajout de documentation pour la création de `client_id` et `client_secret` via curl.
- Mise à jour des données de test pour refléter les dernières évolutions.
- Nettoyage du code et suppression des fichiers inutilisés.
- Amélioration de la configuration CI/CD.
- Correction de problèmes de style et de mise en page.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des *feature flags*.
- Ajout de métriques de suivi pour l'utilisation de la plateforme.
