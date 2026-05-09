## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 08 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'enrichissement de l'API avec de nouveaux endpoints et filtres, notamment pour les données MEC et le dashboard de transition écologique. Des améliorations ont été apportées à la classification des projets, à la gestion des aides et à la robustesse de l'application, avec une attention particulière portée à la performance et à la gestion des erreurs. Des corrections de bugs et des optimisations ont également été réalisées.

### Évolutions fonctionnelles
- Ajout d'un endpoint pour signaler une aide non pertinente pour un projet [#3a4444b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3a4444b).
- Intégration d'un filtre source et de la date de signature CRTE sur les dispositifs/projets du dashboard de transition écologique [#1fa06f6](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/1fa06f6).
- Ajout d'un endpoint pour exporter les projets depuis le dashboard [#a95497c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/a95497c).
- Ajout d'endpoints dédiés pour les données MEC (data_mec) [#30353a1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/30353a1) et [#843a001](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/843a001).
- Possibilité de filtrer par type (duplicate/affinity) sur les clusters du dashboard [#2aaf8c1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/2aaf8c1).
- Ajout d'un endpoint pour récupérer les dispositifs territoriaux (COT ADEME) [#c7cfe7c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c7cfe7c).
- Amélioration des statistiques via communes et EPCI [#a95497c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/a95497c).
- Exposition du dashboard Swagger sur le hub public [#05242c0](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/05242c0).

### Évolutions techniques
- Refactor de l'API pour déplacer les dispositifs du référentiel vers le dashboard-te [#02dc6fa](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/02dc6fa).
- Mise en place d'une classification batch via l'API Batch Anthropic pour les gros volumes de projets [#08413bf](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/08413bf).
- Amélioration de la gestion des erreurs transitoires avec ajout de retries et backoff [#5c8c0d1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/5c8c0d1).
- Augmentation de la limite de taille du body pour l'endpoint `/projets/bulk` à 50MB [#8cd259c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/8cd259c).
- Correction d'un problème d'OOM (Out Of Memory) dans le processus de classification batch [#f9cbd45](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/f9cbd45).
- Utilisation de types bigint pour le champ `budget_previsionnel` afin de supporter des valeurs supérieures à 2.1 milliards [#9082fea](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9082fea).
- Mise à jour du schéma de données `data_mec` avec Drizzle [#7a86d84](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/7a86d84).
- Ajout de headers de sécurité sur les pages HTML servies [#3144fb9](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3144fb9).
- Correction de la validation d'entrée de l'endpoint `POST /analytics/trackEvent` [#bd4daac](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/bd4daac).

### Autres changements
- Documentation et corrections de migrations de base de données (plusieurs commits).
- Corrections de typage et de noms de colonnes pour le dashboard-te [#634113d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/634113d).
- Amélioration de la robustesse du processus de classification batch [#b62ae69](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b62ae69).
- Correction de la configuration CSP (Content Security Policy) [#10e2e09](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/10e2e09).
- Alignement de l'API GET /aides sur projetId (camelCase) avec dépréciation progressive de projet_id [#c80923d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c80923d).
- Validation du paramètre projetId sur GET /aides/feedback [#3a4444b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3a4444b).
- Ajout de total sur les endpoints paginés du dashboard [#96d736e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/96d736e).
- Enrichissement de /projets avec collectiviteNom et codeDepartement [#bb3084d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/bb3084d).
- Correction du fallback data_mec/data_tet sur les endpoints legacy /projets [#1b6f19b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/1b6f19b).
- Correction des noms de colonnes dans le dashboard-te [#656d01b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/656d01b).
