## Changelog : espace-membre-next (30 derniers jours, au 20 août 2026)

### Résumé
Ce mois-ci, la plateforme a évolué pour offrir plus de flexibilité dans la gestion des produits (possibilité de co-incubation) et une meilleure précision dans les processus d'accompagnement (gestion des ateliers et des checklists). Des améliorations structurelles importantes ont été apportées à l'API et à la gestion des tâches de fond pour renforcer la stabilité et la performance du système.

### Évolutions fonctionnelles
- Gestion de la co-incubation pour les produits [#1498](https://github.com/betagouv/espace-membre-next/issues/1498).
- Restriction de la validation des ateliers d'embarquement aux seuls animateurs [#1470](https://github.com/betagouv/espace-membre-next/issues/1470).
- Filtrage des éléments de checklist par domaine utilisateur [#1517](https://github.com/betagouv/espace-membre-next/issues/1517).
- Mise en place de la gestion des demandes d'accès "Ségur" [#1468](https://github.com/betagouv/espace-membre-next/issues/1468).
- Introduction d'un nudge pour encourager l'utilisation de ProConnect [#1405](https://github.com/betagouv/espace-membre-next/issues/1405).
- Clarification des conditions d'affichage lors de l'onboarding.

### Évolutions techniques
- Migration de la gestion des tâches de fond (jobs) de `pg-boss` vers Scalingo Scheduler [#1505](https://github.com/betagouv/espace-membre-next/issues/1505).
- Refonte de l'API : passage aux routes REST au pluriel et mise à jour de la documentation OpenAPI [#1497](https://github.com/betagouv/espace-membre-next/issues/1497).
- Autorisation de l'accès en lecture via OpenAPI pour les utilisateurs connectés [#1508](https://github.com/betagouv/espace-membre-next/issues/1508).
- Montée de version de Next.js [#1514](https://github.com/betagouv/espace-membre-next/issues/1514) et de Sentry [#1491](https://github.com/betagouv/espace-membre-next/issues/1491).
- Résolution d'exceptions d'exécution liées à la gestion des tâches et aux imports cron [#1487](https://github.com/betagouv/espace-membre-next/issues/1487), [#1488](https://github.com/betagouv/espace-membre-next/issues/1488), [#1493](https://github.com/betagouv/espace-membre-next/issues/1493).
- Optimisation du processus de build [#1482](https://github.com/betagouv/espace-membre-next/issues/1482).

### Autres changements
- Ajout d'une section dédiée à la documentation de l'API dans le README.
- Nettoyage général du code, suppression de fichiers obsolètes (legacy) et maintenance de Storybook.
