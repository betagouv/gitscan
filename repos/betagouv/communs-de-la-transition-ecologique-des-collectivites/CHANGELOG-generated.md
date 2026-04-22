## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la performance de l'API, notamment concernant la classification des projets et la synchronisation des données d'aides. Des optimisations ont été apportées pour gérer des volumes de données plus importants et améliorer la fiabilité des traitements asynchrones. La documentation a également été enrichie pour faciliter l'intégration avec l'API.

### Évolutions fonctionnelles
- Ajout d'un endpoint POST `/management/batch-classify/recover` pour la récupération de classifications par lot.
- Amélioration du matching entre projets et aides avec l'ajout de `normalizedScore` et `axesMatched`.
- Ajout d'un endpoint POST `/fiches-action` pour l'intégration avec le programme TeT (Territoires Engagés pour la Transition).
- Enrichissement des données des collectivités responsables et des territoires concernés.
- Résolution automatique du code INSEE vers le périmètre territorial.
- Mise en place d'un cache dédupliqué et d'un pré-chauffage des territoires pour les aides AT (Aides Territoires).
- Augmentation de la limite de taille pour les requêtes POST `/projets/bulk` à 50MB.
- Ajout d'un paramètre `limit` à l'endpoint `/batch-classify` pour contrôler le nombre de projets traités par lot.

### Évolutions techniques
- Durcissement de la validation d'entrée pour l'endpoint POST `/analytics/trackEvent` afin d'améliorer la sécurité.
- Ajout des headers de sécurité sur les pages HTML servies par l'API.
- Refactor de la résolution de périmètre pour utiliser `perimeter_codes[]` dans les requêtes AT.
- Utilisation de l'API Batch Anthropic pour la classification par lot des projets, permettant de traiter des volumes plus importants.
- Correction d'un problème d'OOM (Out Of Memory) lors de la classification par lot en limitant le nombre de projets traités par job à 5000.
- Amélioration de la gestion des erreurs transitoires avec des retries et un backoff exponentiel.
- Correction de problèmes de flaky tests (tests instables) en utilisant des assertions plus robustes et en stabilisant les dépendances.
- Migration du domaine de l'API vers `api.collectivites.beta.gouv.fr`.
- Utilisation de Redis pour le caching des données d'aides et la synchronisation.
- Refactor du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Mise à jour de la documentation pour inclure des informations sur les limites de débit (rate limits), le traitement par lot (bulk), les FAQ et le stock.
- Ajout d'un guide d'intégration pour la classification et les aides pour le programme MEC.
- Correction de liens et de références dans la documentation.
- Publication de la version 0.4.0 du widget.
- Correction de pointeurs vers l'API de staging dans l'environnement de sandbox.
- Correction de bugs et améliorations diverses.
