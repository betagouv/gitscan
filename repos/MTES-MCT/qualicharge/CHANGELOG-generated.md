## Changelog : qualicharge (30 derniers jours, au 2026-04-15)

### Résumé
Ce mois-ci, les évolutions de Qualicharge se concentrent sur l'amélioration de la robustesse de l'API, notamment dans la gestion des stations de recharge (décommissionnement, remise en service) et la gestion des erreurs. Des corrections ont également été apportées pour améliorer la fiabilité des indicateurs Prefect et des messages d'erreur. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Amélioration de la gestion des stations de recharge : les stations orphelines sont désormais mises hors service au lieu d'être supprimées, ce qui permet une meilleure traçabilité. [#936](https://github.com/MTES-MCT/qualicharge/issues/936)
- Les stations sont remises en service automatiquement lorsqu'un seul point de charge redevient opérationnel.
- Amélioration des messages d'erreur pour les opérations de lecture et de listage, les rendant plus clairs et informatifs.
- Suppression des sessions longues de l'indicateur OCCT dans Prefect pour une meilleure précision.

### Évolutions techniques
- Mise à jour de plusieurs dépendances Python, incluant `pyjwt` (avec correction de sécurité), `requests`, `dynaconf`, `Django`, `pytest` et d'autres, pour bénéficier des dernières corrections et améliorations.
- Mise à jour des images Docker utilisées pour Metabase, Keycloak, Locust, Terraform, et UV.
- Mise à jour des actions GitHub utilisées pour le déploiement et la publication (upload-artifact, gh-action-pypi-publish, setup-uv).
- Upgrade de pygments à la version 2.20.0

### Autres changements
- Publication d'une nouvelle version de l'API (0.33.1).
