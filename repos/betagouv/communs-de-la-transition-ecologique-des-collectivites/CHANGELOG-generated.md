## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 04 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'enrichissement de l'API et du dashboard de la transition écologique, notamment avec l'ajout de nouvelles fonctionnalités pour le traitement des données MEC (Maîtrise Energétique des Collectivités) et l'amélioration des statistiques disponibles. Des optimisations ont été apportées pour gérer des volumes de données plus importants et améliorer la robustesse de l'application.

### Évolutions fonctionnelles
- Ajout d'un filtre source et de la date de signature CRTE sur les dispositifs et projets du dashboard de la transition écologique. [#1234](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/1234)
- Amélioration des statistiques disponibles via les communes et les EPCI, avec ajout d'un endpoint d'export des projets.
- Intégration des dispositifs territoriaux (COT ADEME) avec un nouvel endpoint dédié.
- Ajout du nom de la collectivité et du code département à l'endpoint `/projets`.
- Enrichissement de l'endpoint `/dashboard-te/stats/national` avec des colonnes communes et correction de données.
- Ajout de filtres et d'endpoints pour le dashboard V3, incluant des filtres sur le type de cluster (duplicate/affinity).
- Ajout des champs `normalizedScore` et `axesMatched` dans le matching des aides.
- Ajout d'un endpoint pour la récupération des classifications batch interrompues (`/management/batch-classify/recover`).
- Ajout d'un endpoint pour la classification batch via l'API Batch Anthropic pour les gros volumes.
- Correction de l'auto-création du plan CRTE lors de la mise à jour d'un projet MEC.
- Correction de l'inclusion du `MecModule` dans la spécification OpenAPI Swagger.

### Évolutions techniques
- Refactorisation du code pour déplacer les dispositifs du référentiel vers le dashboard de la transition écologique.
- Amélioration de la gestion des erreurs en bulk dans l'API MEC.
- Utilisation de `jsonb` au lieu de `text` pour stocker les métadonnées dans le référentiel.
- Correction de la migration Drizzle pour le schéma `data_mec`.
- Augmentation de la limite de taille du corps de requête pour l'endpoint `/projets/bulk` à 50MB.
- Optimisation du batch classification pour éviter les erreurs de mémoire (OOM) en limitant le nombre de projets par job à 5000.
- Ajout de retry avec backoff pour gérer les erreurs transitoires avec AT.
- Utilisation de `perimeter_codes[]` au lieu de la résolution de périmètre.
- Durcissement de la validation d'entrée pour l'endpoint `/analytics/trackEvent`.
- Ajout de headers de sécurité sur les pages HTML servies.
- Correction de la validation PATCH de l'API MEC.
- Correction de la classification de l'API MEC.
- Correction des noms de colonnes dans le dashboard-te (camelCase + JSONB llm_sites).
- Correction du type de colonne `budget_previsionnel` en `bigint`.
- Correction de l'utilisation de `ANY(array)` pour les statistiques des dispositifs.

### Autres changements
- Mise à jour de la version du widget à 0.4.0.
- Correction de la configuration de l'environnement sandbox pour pointer vers l'API de production.
- Diverses corrections et améliorations de la documentation et de la configuration.
- Publication de plusieurs versions (0.1.50 à 0.1.74) avec des corrections et des améliorations mineures.
