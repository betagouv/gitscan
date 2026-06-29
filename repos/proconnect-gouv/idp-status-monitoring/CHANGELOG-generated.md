## Changelog : idp-status-monitoring (30 derniers jours, au 20 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la correction d'un problème critique concernant la gestion des réponses RabbitMQ par le producteur, améliorant ainsi la fiabilité de la communication entre les différents composants de l'application. Des mises à jour de dépendances ont également été appliquées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Correction d'un bug dans le producteur qui causait un "vol" de réponses entre les différentes instances concurrentes, assurant ainsi que chaque requête reçoit la réponse correcte. [#123](https://github.com/proconnect-gouv/idp-status-monitoring/issues/123)

### Évolutions techniques
- Mise à jour de l'action Docker `setup-buildx-action` de la version 4.0.0 à la version 4.1.0. [#117](https://github.com/proconnect-gouv/idp-status-monitoring/issues/117)
- Mise à jour de l'action Docker `setup-compose-action` de la version 2.1.0 à la version 2.2.0. [#118](https://github.com/proconnect-gouv/idp-status-monitoring/issues/118)
- Mise à jour de la librairie Hono de la version 4.12.22 à la version 4.12.23 puis à la version 4.12.25 et enfin à la version 4.12.26. [#119](https://github.com/proconnect-gouv/idp-status-monitoring/issues/119), [#121](https://github.com/proconnect-gouv/idp-status-monitoring/issues/121), [#125](https://github.com/proconnect-gouv/idp-status-monitoring/issues/125)
- Mise à jour de l'action `actions/checkout` de la version 6.0.2 à la version 6.0.3. [#120](https://github.com/proconnect-gouv/idp-status-monitoring/issues/120)
- Mise à jour de Prettier de la version 3.8.3 à la version 3.8.4. [#122](https://github.com/proconnect-gouv/idp-status-monitoring/issues/122)
