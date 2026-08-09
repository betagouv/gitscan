## Changelog : aides-jeunes-ops (30 derniers jours, au 08/08/2026)

### Résumé
Les récentes interventions visent à renforcer la fiabilité et la surveillance de l'infrastructure. L'accent a été mis sur la sécurisation des sauvegardes de données, l'amélioration de la détection d'incidents et l'optimisation des services de calcul.

### Évolutions techniques
- **Base de données** : Mise en place de sauvegardes quotidiennes vérifiées pour la base de production MongoDB, incluant la validation de la complétude des données et la sérialisation des exécutions [#240](https://github.com/betagouv/aides-jeunes-ops/issues/240) [#244](https://github.com/betagouv/aides-jeunes-ops/issues/244).
- **Supervision et Alerting** : Amélioration de la détection d'incidents via l'envoi des échecs d'unités systemd vers Sentry [#243](https://github.com/betagouv/aides-jeunes-ops/issues/243) et rétablissement du service de monitoring pour la compatibilité avec Node 24 [#238](https://github.com/betagouv/aides-jeunes-ops/issues/238).
- **Performance** : Optimisation du moteur de calcul OpenFisca par une gestion rigoureuse du nombre de workers et de la file d'attente des calculs [#237](https://github.com/betagouv/aides-jeunes-ops/issues/237).

### Autres changements
- **Maintenance** : Nettoyage des tâches planifiées (crontabs) des utilisateurs de déploiement obsolètes [#239](https://github.com/betagouv/aides-jeunes-ops/issues/239).
