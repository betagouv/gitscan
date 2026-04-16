## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'API, notamment l'intégration d'un nouveau service de classification des projets de transition écologique, l'enrichissement des données territoriales et l'optimisation des performances grâce à la mise en cache. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un endpoint POST `/fiches-action` pour permettre la soumission de fiches action via le Territoire Environnemental et Transition écologique (TeT). [#21ae414](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/21ae414)
- Classification automatique des projets à la création, utilisant le modèle Claude Sonnet 4.6. [#233a0af](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/233a0af)
- Enrichissement des données des collectivités responsables (siren) et des territoires concernés (communes). [#e1a5fdc](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/e1a5fdc)
- Résolution automatique du code INSEE vers le périmètre AT (Aire Territoriale). [#690e8c5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/690e8c5)
- Mise en place d'un cron job pour synchroniser les données des aides et utilisation d'un cache Redis pour améliorer les performances. [#fa1546c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/fa1546c)
- Ajout d'un proxy enrichi pour les aides-territoires avec un mécanisme de matching. [#3f8f250](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/3f8f250)

### Évolutions techniques
- Refactor de l'API pour utiliser `perimeter_codes[] AT` au lieu de la résolution de périmètre. [#656d01b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/656d01b)
- Migration du domaine de l'API vers `api.collectivites.beta.gouv.fr`. [#a90b097](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/a90b097)
- Amélioration de la robustesse du parser JSON pour les réponses du LLM (gestion des multi-blocs). [#2ee5093](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/2ee5093)
- Optimisation du warmup de l'API pour respecter le rate-limit AT (séquentiel + retry 429). [#40a998b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/40a998b)
- Mise en cache dédupliqué SWR et pré-chauffage des territoires pour les aides AT. [#b3420ca](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/b3420ca)
- Correction de tests unitaires et E2E flakys (BullMQ, GeoService). [#2502e4c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/2502e4c), [#95f338a](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/95f338a), [#415126b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/415126b)
- Utilisation de GeoService au lieu de GeoApiService dans les tests E2E. [#3c3dd89](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/3c3dd89)

### Autres changements
- Documentation de la formule de matching projet ↔ aide. [#0859bc8](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/0859bc8)
- Mise à jour de la documentation pour le guide MEC (rate limits, bulk, FAQ, stock). [#45ae124](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/45ae124)
- Refonte de la page "Vocabulaire métier" (v2). [#8f24d7a](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/8f24d7a)
- Correction de la cohérence du vocabulaire avec le schéma technique. [#4b1081c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/4b1081c)
- Correction du domaine API dans la documentation. [#e0afa5e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/e0afa5e)
- Renommage d'endpoints et de champs de l'API suite aux retours de TeT. [#50d4397](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/pulls/50d4397)
