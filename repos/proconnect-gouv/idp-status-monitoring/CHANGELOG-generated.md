## Changelog : idp-status-monitoring (30 derniers jours, au 20 juin 2026)

### Résumé
Ce mois-ci, les mises à jour se sont concentrées sur la correction d'un problème critique concernant la gestion des réponses du producteur, ainsi que sur la mise à jour des dépendances du projet pour bénéficier des dernières corrections de sécurité et améliorations.

### Évolutions fonctionnelles
- Correction d'un bug dans le producteur qui causait le "vol" de réponses entre différentes instances concurrentes [#123](https://github.com/proconnect-gouv/idp-status-monitoring/issues/123). Cette correction assure une meilleure fiabilité et cohérence des réponses envoyées.

### Évolutions techniques
- Mise à jour de plusieurs actions Docker utilisées dans les workflows CI/CD (buildx, compose, metadata, build-push, login) vers leurs dernières versions.
- Mise à jour de la librairie Hono (framework web) vers les versions 4.12.25 et 4.12.26.

### Autres changements
- Mises à jour mineures des dépendances de développement (prettier).
- Mise à jour de l'action `actions/checkout`.
