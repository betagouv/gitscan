## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 14 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'API et du back-office, notamment avec l'ajout de fonctionnalités pour la gestion des questionnaires, des services et des aides, ainsi que des améliorations significatives pour l'intégration avec le programme MEC (Médiateur Énergétique des Collectivités). Des efforts ont également été faits pour améliorer la robustesse et la documentation du projet.

### Évolutions fonctionnelles
- **Back-office:**
    - Ajout d'un éditeur de questionnaires, permettant de définir et modifier les questionnaires directement depuis l'interface. [#1234](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/1234)
    - Possibilité d'ajouter et de retirer des aides ou des services depuis l'écran de gestion.
    - Amélioration de la lisibilité de l'écran de gestion des cibles, réglages et services hors catalogue.
    - Affichage des données réelles renvoyées par l'API dans le back-office pour faciliter le débogage.
    - Ajout de la possibilité d'ajouter un service "hors catalogue" décrit par l'agent.
- **API:**
    - Expose l'identifiant de l'aide dans les financements.
    - Génération des descriptions manquantes des services à partir des sites web, évitant ainsi les "hallucinations".
    - Mise à disposition de l'ensemble du catalogue de services numériques, avec des logos et des descriptions complétées.
    - Ajout de questionnaires, recommandations et du catalogue de services numériques à l'API.
    - Vrais logos des services numériques hébergés par l'API.
- **Dashboard TE:**
    - Ajout de filtres multi-valeurs pour la commune, le département et la source.

### Évolutions techniques
- **Intégration MEC:**
    - Refonte de la documentation d'intégration MEC.
    - Ajout d'endpoints pour les territoires et les décisions (vue territoriale DDT via MEC).
    - Implémentation d'un schéma `decisions_humaines` pour un journal append-only des décisions humaines.
    - Mise en place d'une doctrine d'accès aux données (data_scopes) pour une meilleure gestion des permissions.
    - Amélioration de la gestion des erreurs et de la robustesse des endpoints liés à l'intégration MEC.
- **Architecture & Performance:**
    - Suppression des thématiques du contrat public des services.
    - Refactoring et simplification du code après revue.
    - Amélioration de la gestion des erreurs Undici et ajout de mécanismes de throttling pour les routes d'ingestion partenaires.
    - Optimisation de l'enqueue des leviers MEC (retry, purge, nom de job distinct, patch).
- **Tests:**
    - Ajout de tests pour l'enregistrement asynchrone des données d'utilisation (analytics).
    - Désactivation temporaire de certaines suites de tests e2e instables en CI.

### Autres changements
- Documentation : Ajout d'un guide d'édition pour les questionnaires et clarification de la signification de `horsCatalogue`.
- Suppression des scripts d'exploration du dépôt et réparation de la commande `pnpm validate`.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des versions (0.1.103, 0.1.102, 0.1.101, 0.1.100, 0.1.99).
