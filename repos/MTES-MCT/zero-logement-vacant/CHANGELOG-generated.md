## Changelog : zero-logement-vacant (30 derniers jours, au 19 juin 2026)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de l'application, notamment l'implémentation de l'import des données LOVAC 2026, l'intégration de nouveaux types de graphiques DSFR (diagrammes en barres, diagrammes circulaires, tableaux) et une refonte de l'architecture pour améliorer les performances et la maintenabilité. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Implémentation de l'import des données LOVAC 2026, incluant la transformation et le chargement des données, avec des optimisations de performance et une gestion des erreurs améliorée.
- Ajout de la possibilité d'afficher des diagrammes en barres, des diagrammes circulaires et des tableaux à partir des données Metabase, en utilisant les composants DSFR.
- Ajout d'une colonne "Statut des destinataires" dans le tableau des destinataires de campagne.
- Amélioration de la navigation : redirection vers la vue tableau lors du clic sur un groupe depuis la carte.
- Ajout d'un indicateur de chargement au bouton de connexion.
- Possibilité de lier une campagne à un logement.
- Amélioration de la gestion des filtres de campagne.

### Évolutions techniques
- Migration vers React Router v7.
- Refonte de l'architecture pour utiliser des composants DSFR natifs pour les graphiques.
- Amélioration des performances de l'application en réduisant la taille du bundle frontend grâce au lazy loading.
- Utilisation de DuckDB pour le prétraitement des données LOVAC.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Utilisation de Zod pour la validation des données.
- Mise à jour des dépendances.
- Amélioration des tests unitaires et d'intégration.
- Utilisation de TypeScript pour une meilleure typage et détection d'erreurs.
- Utilisation de `tsx` au lieu de `ts-node`.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation des requêtes SQL.
- Amélioration de la gestion de la configuration.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés à l'application.
- Ajout de nouvelles variables d'environnement pour la configuration de l'application.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de tests pour les nouvelles fonctionnalités.
- Ajout de règles de linting et de formatage de code.
- Suppression de code obsolète.
- Amélioration de la gestion des secrets.
- Ajout de commentaires et de documentation au code.
- Ajout d'un workflow CI/CD pour automatiser le processus de déploiement.
- Mise en place d'un système de suivi des performances.
- Ajout de métriques pour surveiller l'utilisation de l'application.
- Ajout d'un système d'alerte pour notifier les administrateurs en cas de problème.
- Ajout de tests d'intégration pour les pipelines Dagster.
- Ajout de tests pour les transformations Dbt.
- Amélioration de la gestion des erreurs dans les pipelines Dagster.
- Ajout de documentation pour les pipelines Dagster.
