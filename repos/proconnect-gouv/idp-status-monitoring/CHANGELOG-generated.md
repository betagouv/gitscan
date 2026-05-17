## Changelog : idp-status-monitoring (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la réactivité du producteur en streaming des résultats et sur la mise à jour des dépendances du projet pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Le producteur stream désormais les résultats `/idp/internet` dès qu'ils sont disponibles, améliorant ainsi la réactivité du système. [#99](https://github.com/proconnect-gouv/idp-status-monitoring/pull/99)

### Évolutions techniques
- Mise à jour de Hono (4.12.14 -> 4.12.18) pour bénéficier des dernières corrections et améliorations.
- Mise à jour de Zod (4.3.6 -> 4.4.3) pour bénéficier des dernières corrections et améliorations.
- Mise à jour d'amqplib (1.0.3 -> 1.0.7) pour bénéficier des dernières corrections et améliorations.
- Mise à jour de UUID (13.0.0 -> 14.0.0) pour bénéficier des dernières corrections et améliorations.
- Mise à jour de Bun (1.3.12-alpine -> 1.3.13-alpine) pour bénéficier des dernières corrections et améliorations.
- Mise à jour des dépendances de développement : @types/bun, prettier, typescript.
- Mise à jour de l'action GitHub `actions/upload-artifact` (7.0.0 -> 7.0.1).

### Autres changements
- Aucune information supplémentaire.
