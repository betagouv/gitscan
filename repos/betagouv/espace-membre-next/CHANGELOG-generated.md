## Changelog : espace-membre-next (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié de nouvelles fonctionnalités pour faciliter les demandes d'accès aux bureaux Ségur et améliorer l'accueil des nouveaux membres via une checklist mise à jour. En coulisses, une importante modernisation de l'infrastructure a été réalisée pour rendre la gestion des tâches automatiques plus fiable et performante.

### Évolutions fonctionnelles
- Mise en place des demandes d'accès aux bureaux Ségur [#1460](https://github.com/betagouv/espace-membre-next/issues/1460), [#1468](https://github.com/betagouv/espace-membre-next/issues/1468)
- Amélioration de la checklist d'onboarding avec l'intégration des canaux Tchap [#1450](https://github.com/betagouv/espace-membre-next/issues/1450)
- Ajout d'un nudge (incitation) pour l'utilisation de ProConnect [#1405](https://github.com/betagouv/espace-membre-next/issues/1405)
- Mise à jour du suivi du statut des emails des membres [#1447](https://github.com/betagouv/espace-membre-next/issues/1447)

### Évolutions techniques
- Migration de la gestion des tâches planifiées de `pg-boss` vers le `Scalingo Scheduler` [#1505](https://github.com/betagouv/espace-membre-next/issues/1505)
- Standardisation de l'API REST (routes au pluriel pour les incubateurs, startups et membres) et ajout de la documentation OpenAPI [#1497](https://github.com/betagouv/espace-membre-next/issues/1497)
- Refactorisation et nettoyage important du code (suppression de tâches, de routes et d'utilitaires obsolètes) [#1504](https://github.com/betagouv/espace-membre-next/issues/1504), [#1495](https://github.com/betagouv/espace-membre-next/issues/1495), [#1489](https://github.com/betagouv/espace-membre-next/issues/1489)
- Résolution de plusieurs erreurs d'exécution liées aux tâches planifiées (cron/pg-boss) [#1493](https://github.com/betagouv/espace-membre-next/issues/1493), [#1487](https://github.com/betagouv/espace-membre-next/issues/1487), [#1488](https://github.com/betagouv/espace-membre-next/issues/1488)
- Optimisation de la gestion des emails (dimail) et de la synchronisation [#1449](https://github.com/betagouv/espace-membre-next/issues/1449)
- Mise à jour et correction de l'intégration Sentry pour le suivi des erreurs [#1491](https://github.com/betagouv/espace-membre-next/issues/1491)
- Optimisation du processus de build [#1482](https://github.com/betagouv/espace-membre-next/issues/1482)

### Autres changements
- Nettoyage de la documentation et des dépendances [#1506](https://github.com/betagouv/espace-membre-next/issues/1506), [#1496](https://github.com/betagouv/espace-membre-next/issues/1496)
