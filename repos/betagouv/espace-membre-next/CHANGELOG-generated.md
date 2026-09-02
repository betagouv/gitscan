## Changelog : espace-membre-next (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois-ci, la plateforme a gagné en flexibilité avec l'introduction de la co-incubation pour les startups et un meilleur contrôle des processus d'embarquement. Un chantier important a été mené sur l'infrastructure pour fiabiliser la gestion des tâches planifiées, tout en améliorant l'accessibilité et la documentation de l'API.

### Évolutions fonctionnelles
- **Gestion des produits** : Possibilité de gérer la co-incubation d'un produit pour les startups [#1498](https://github.com/betagouv/espace-membre-next/pull/1498).
- **Parcours d'embarquement** : Affinement des conditions d'affichage de l'onboarding et restriction de la validation des ateliers d'embarquement aux seuls animateurs [#1470](https://github.com/betagouv/espace-membre-next/pull/1470).
- **Checklists** : Filtrage des éléments de checklist en fonction du domaine de l'utilisateur [#1517](https://github.com/betagouv/espace-membre-next/pull/1517).
- **Accès et sécurité** : Ajout de la gestion des demandes d'accès Ségur [#1468](https://github.com/betagouv/espace-membre-next/pull/1468) et ajout d'un rappel (nudge) pour l'utilisation de ProConnect [#1405](https://github.com/betagouv/espace-membre-next/pull/1405).

### Évolutions techniques
- **Infrastructure** : Migration de la gestion des tâches (jobs) de `pg-boss` vers le `Scalingo Scheduler` pour plus de stabilité [#1505](https://github.com/betagouv/espace-membre-next/pull/1505).
- **API** : Refonte des routes REST pour les incubateurs, startups et membres, incluant la mise à jour de la documentation OpenAPI [#1497](https://github.com/betagouv/espace-membre-next/pull/1497).
- **API** : Correction des droits d'accès en lecture sur l'API pour les utilisateurs connectés [#1508](https://github.com/betagouv/espace-membre-next/pull/1508).
- **Framework** : Mise à jour du projet vers Next.js 15.5.23 [#1514](https://github.com/betagouv/espace-membre-next/pull/1514).
- **Stabilité** : Résolution de plusieurs exceptions d'exécution liées aux tâches planifiées et aux imports de cron [#1487](https://github.com/betagouv/espace-membre-next/pull/1487), [#1488](https://github.com/betagouv/espace-membre-next/pull/1488), [#1493](https://github.com/betagouv/espace-membre-next/pull/1493).
- **CI/CD** : Optimisation des processus de build [#1482](https://github.com/betagouv/espace-membre-next/pull/1482).

### Autres changements
- **Documentation** : Ajout d'une section dédiée à l'API dans le README et mise à jour des liens de documentation de développement [#1532](https://github.com/betagouv/espace-membre-next/pull/1532).
- **Maintenance** : Nettoyage important du code (suppression de fichiers obsolètes, de tâches inutiles et de code legacy) et optimisation de Storybook.
