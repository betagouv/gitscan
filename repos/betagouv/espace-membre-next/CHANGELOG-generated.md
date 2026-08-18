## Changelog : espace-membre-next (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, la plateforme a enrichi ses capacités métier avec la gestion de la co-incubation et des demandes d'accès aux services Ségur, tout en affinant l'expérience d'accueil des nouveaux utilisateurs. Un travail important de simplification technique et de migration d'infrastructure a également été réalisé pour améliorer la stabilité et la maintenabilité du système.

### Évolutions fonctionnelles
- **Gestion métier** : introduction de la possibilité de co-incuber un produit ([#1498](https://github.com/betagouv/espace-membre-next/issues/1498)) et mise en place des demandes d'accès aux bureaux et services Ségur ([#1460](https://github.com/betagouv/espace-membre-next/issues/1460), [#1468](https://github.com/betagouv/espace-membre-next/issues/1468)).
- **Expérience utilisateur (Onboarding)** : amélioration du parcours d'accueil avec une clarification des conditions d'affichage et une mise à jour des canaux Tchap dans les checklists ([#1450](https://github.com/betagouv/espace-membre-next/issues/1450)).
- **Checklists** : filtrage des éléments de checklist par domaine utilisateur pour plus de pertinence ([#1517](https://github.com/betagouv/espace-membre-next/issues/1517)).
- **Authentification** : ajout d'une incitation (nudge) pour encourager l'utilisation de ProConnect ([#1405](https://github.com/betagouv/espace-membre-next/issues/1405)).

### Évolutions techniques
- **Infrastructure** : migration de la gestion des tâches planifiées de `pg-boss` vers le `Scalingo Scheduler` ([#1505](https://github.com/betagouv/espace-membre-next/issues/1505)).
- **API** : standardisation des routes REST (utilisation du pluriel) et mise à jour de la documentation OpenAPI ([#1497](https://github.com/betagouv/espace-membre-next/issues/1497), [#1508](https://github.com/betagouv/espace-membre-next/issues/1508)).
- **Maintenance et nettoyage** : suppression de code obsolète (legacy), de tâches inutiles et simplification des fichiers de routes et d'utilitaires ([#1504](https://github.com/betagouv/espace-membre-next/issues/1504), [#1495](https://github.com/betagouv/espace-membre-next/issues/1495), [#1489](https://github.com/betagouv/espace-membre-next/issues/1489)).
- **Corrections de bugs** : résolution d'exceptions d'exécution liées à la gestion des tâches planifiées ([#1487](https://github.com/betagouv/espace-membre-next/issues/1487), [#1493](https://github.com/betagouv/espace-membre-next/issues/1493)).
- **CI/CD** : optimisation des processus de build en supprimant les étapes inutiles ([#1482](https://github.com/betagouv/espace-membre-next/issues/1482)).

### Autres changements
- **Documentation** : ajout d'une section dédiée à la documentation de l'API dans le README.
- **Nettoyage** : maintenance de Storybook et divers nettoyages de fichiers de configuration ([#1506](https://github.com/betagouv/espace-membre-next/issues/1506)).
