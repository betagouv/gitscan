## Changelog : qualicharge (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'automatisation de la mise à jour des unités opérationnelles via l'API, améliorant ainsi l'efficacité de la gestion des données. De nombreuses mises à jour de sécurité et de dépendances ont également été appliquées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Automatisation de la mise à jour des unités opérationnelles via l'API. [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9)

### Évolutions techniques
- Mise à jour de Django vers la version 6.0.5, incluant des correctifs de sécurité. [#f7364a3](https://github.com/MTES-MCT/qualicharge/commit/f7364a3)
- Mises à jour régulières des images Docker utilisées (uv, metabase, curl).
- Mises à jour de plusieurs dépendances Python (urllib3, idna, mako, prefect) pour bénéficier des derniers correctifs et améliorations de sécurité.

### Autres changements
- Mises à jour de l'action Zizmor pour l'intégration continue.
- Mises à jour de la librairie `astral-sh/uv` pour la gestion des fuseaux horaires.
- Application de correctifs de sécurité via Dependabot et Renovate.
