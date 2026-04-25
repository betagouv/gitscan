## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration et l'enrichissement de l'API, notamment pour le nouveau dashboard V3 et l'intégration avec Anthropic pour la classification par lot de projets. Des corrections et optimisations ont également été apportées pour améliorer la robustesse et la performance de l'API, en particulier lors de la gestion de volumes importants de données.

### Évolutions fonctionnelles
- Ajout de filtres de type (duplicate/affinity) sur les clusters du dashboard-te [#085ab26](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/085ab26).
- Enrichissement de l'endpoint `/projets` avec les informations `collectiviteNom` et `codeDepartement` [#bb3084d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/bb3084d).
- Ajout du total de résultats sur les endpoints paginés du dashboard-te [#96d736e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/96d736e).
- Amélioration du matching des aides avec l'ajout de `normalizedScore` et `axesMatched` [#7ecae8f](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/7ecae8f).
- Ajout d'un endpoint `/management/batch-classify/recover` pour la reprise de classifications par lot [#812426d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/812426d).
- Ajout d'un filtre `source` sur l'endpoint `/management/batch-classify` [#fdea5d5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/fdea5d5).

### Évolutions techniques
- Intégration de la classification par lot via l'API Batch Anthropic pour les gros volumes de données [#08413bf](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/08413bf).
- Optimisation de la gestion des erreurs transitoires avec ajout de retries et backoff pour l'API Anthropic [#5c8c0d1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/5c8c0d1).
- Refactoring pour utiliser `perimeter_codes[]` pour la résolution de périmètre [#656d01b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/656d01b).
- Augmentation de la limite du body pour l'endpoint `/projets/bulk` à 50MB [#8cd259c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/8cd259c).
- Correction d'un problème d'OOM (Out Of Memory) lors de la classification par lot en limitant le nombre de projets par job à 5000 [#f9cbd45](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/f9cbd45).
- Amélioration de la robustesse du parsing des réponses JSON du LLM (multi-blocs) [#2ee5093](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/2ee5093).
- Mise en place d'un cache dédupliqué SWR et pré-chauffage des territoires pour les aides Anthropic [#b3420ca](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b3420ca).

### Autres changements
- Mise à jour du widget en version 0.4.0 [#cebfe19](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/cebfe19).
- Correction du pointage vers l'API de production dans l'environnement sandbox [#bc76cdf](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/bc76cdf).
- Ajout de headers de sécurité sur les pages HTML servies [#3144fb9](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3144fb9).
- Durcissement de la validation d'entrée pour l'endpoint `/analytics/trackEvent` [#bd4daac](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/bd4daac).
- Correction d'un problème de CSP (Content Security Policy) en autorisant les polices Google et en ajoutant un hash pour le script Matomo [#10e2e09](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/10e2e09).
- Correction de bugs et améliorations diverses identifiées lors des revues de code [#8fdba7d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/8fdba7d), [#b62ae69](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b62ae69).
- Correction du fallback pour les groupements EPCI dans `/projets` [#cc82012](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/cc82012).
- Correction du type de colonne dans `/plans/:id/groupements` (type au lieu de nature\_juridique) [#4e2a89c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/4e2a89c).
- Correction des noms de colonnes dans le dashboard-te (camelCase + JSONB llm\_sites) [#634113d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/634113d).
- Correction du type de `budget_previsionnel` en `bigint` pour supporter les valeurs supérieures à 2.1 milliards [#9082fea](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9082fea).
- Correction du custom\_id batch Anthropic (remplacement de : par --) [#1edbe1e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/1edbe1e).
- Correction des retours de review sur le batch processor [#b62ae69](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b62ae69).
