## Changelog : espace-membre-next (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes dans la gestion des utilisateurs et des structures, notamment avec l'introduction de la co-incubation pour les produits et de nouvelles procédures de demande d'accès (Ségur). L'expérience d'accueil (onboarding) a été fluidifiée et l'infrastructure technique a été modernisée, passant d'une gestion de tâches interne à un système de planification plus robuste.

### Évolutions fonctionnelles
- **Gestion des structures et produits** : possibilité de gérer la co-incubation d'un produit [#1498](https://github.com/betagouv/espace-membre-next/issues/1498).
- **Demandes d'accès** : mise en place de la gestion des demandes d'accès pour les bureaux Ségur [#1460](https://github.com/betagouv/espace-membre-next/issues/1460) [#1468](https://github.com/betagouv/espace-membre-next/issues/1468).
- **Parcours d'accueil (Onboarding)** : 
    - Amélioration de l'affichage des conditions d'entrée.
    - Filtrage des éléments de checklist par domaine utilisateur [#1517](https://github.com/betagouv/espace-membre-next/issues/1517).
    - Mise à jour de la checklist avec l'intégration des canaux Tchap [#1450](https://github.com/betagouv/espace-membre-next/issues/1450).
- **Expérience utilisateur** : ajout d'un nudge pour encourager l'utilisation de ProConnect [#1405](https://github.com/betagouv/espace-membre-next/issues/1405).

### Évolutions techniques
- **Infrastructure et tâches de fond** : migration de la gestion des jobs de `pg-boss` vers `Scalingo Scheduler` [#1505](https://github.com/betagouv/espace-membre-next/issues/1505) et suppression des anciens processus obsolètes [#1504](https://github.com/betagouv/espace-membre-next/issues/1504).
- **API et Sécurité** : 
    - Refonte des routes REST pour les incubateurs, startups et membres avec mise à jour de la documentation OpenAPI [#1497](https://github.com/betagouv/espace-membre-next/issues/1497).
    - Correction des droits d'accès en lecture pour les utilisateurs connectés via l'API [#1508](https://github.com/betagouv/espace-membre-next/issues/1508).
- **Maintenance et mises à jour** : 
    - Passage à Next.js 15.5.23 [#1514](https://github.com/betagouv/espace-membre-next/issues/1514).
    - Mise à jour de Sentry [#1491](https://github.com/betagouv/espace-membre-next/issues/1491).
    - Nettoyage des dépendances [#1496](https://github.com/betagouv/espace-membre-next/issues/1496).
- **Corrections de bugs** : résolution d'exceptions d'exécution liées à `pg-boss` [#1487](https://github.com/betagouv/espace-membre-next/issues/1487) et correction d'importations sur les tâches cron [#1493](https://github.com/betagouv/espace-membre-next/issues/1493).

### Autres changements
- **Documentation** : ajout d'une section dédiée à la documentation de l'API dans le README.
- **Nettoyage** : suppression de fichiers obsolètes, nettoyage de Storybook et optimisation des fichiers de routes et utilitaires.
