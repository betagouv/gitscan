## Changelog : espace-membre-next (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration du parcours d'embarquement des nouveaux membres et l'optimisation de l'infrastructure technique. Le système permet désormais de gérer la co-incubation de produits et offre un filtrage plus précis des checklists. Côté technique, la gestion des tâches de fond a été modernisée pour gagner en fiabilité.

### Évolutions fonctionnelles
- **Gestion de l'embarquement** : restriction de la validation de l'atelier d'embarquement aux seuls animateurs [#1470](https://github.com/betagouv/espace-membre-next/pull/1470) et clarification des conditions d'affichage de l'entrée en embarquement.
- **Gestion des startups** : possibilité de gérer la co-incubation d'un produit [#1498](https://github.com/betagouv/espace-membre-next/pull/1498).
- **Checklists** : filtrage des éléments de checklist en fonction du domaine de l'utilisateur [#1517](https://github.com/betagouv/espace-membre-next/pull/1517).

### Évolutions techniques
- **Infrastructure et tâches de fond** : migration de la gestion des tâches de `pg-boss` vers `Scalingo Scheduler` [#1505](https://github.com/betagouv/espace-membre-next/pull/1505) et suppression des tâches obsolètes [#1504](https://github.com/betagouv/espace-membre-next/pull/1504).
- **API** : mise en conformité des routes REST (incubateurs, startups et membres) avec l'ajout de la documentation OpenAPI [#1497](https://github.com/betagouv/espace-membre-next/pull/1497) et correction des droits d'accès en lecture pour les utilisateurs connectés [#1508](https://github.com/betagouv/espace-membre-next/pull/1508).
- **Maintenance et correctifs** : 
    - Mise à jour de Next.js [#1514](https://github.com/betagouv/espace-membre-next/pull/1514) et de Sentry [#1491](https://github.com/betagouv/espace-membre-next/pull/1491).
    - Résolution d'exceptions d'exécution liées aux tâches planifiées (cron/pg-boss) [#1487](https://github.com/betagouv/espace-membre-next/pull/1487), [#1488](https://github.com/betagouv/espace-membre-next/pull/1488) et [#1493](https://github.com/betagouv/espace-membre-next/pull/1493).

### Autres changements
- **Documentation** : ajout d'une section dédiée à l'API dans le README et mise à jour des liens de la documentation de l'embarquement [#1532](https://github.com/betagouv/espace-membre-next/pull/1532).
- **Nettoyage** : suppression de code et de fichiers obsolètes, et nettoyage de l'environnement Storybook.
