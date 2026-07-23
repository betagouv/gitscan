## Changelog : qualicharge (30 derniers jours, au 14 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à l'API, notamment en exigeant au moins une cible lors de la création d'un tarif. Des corrections ont également été apportées aux requêtes Prefect pour une meilleure gestion des données des bornes de recharge, incluant celles qui ont été décommissionnées. Enfin, des indicateurs de session (E1-DMR et E5) ont été ajoutés et un décalage a été appliqué pour une meilleure précision.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Ajout d'indicateurs de session E1-DMR et E5. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431)

### Évolutions techniques
- Correction d'une erreur dans Prefect concernant la plage de temps des requêtes sur la table `lateststatus`. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Inclusion des bornes de recharge décommissionnées dans les requêtes Prefect. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Ajout d'un décalage de 15 jours pour les indicateurs de session dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
- Mise à jour de plusieurs dépendances Docker (Keycloak, Metabase, Locust, Curl, Terraform, UV) et actions GitHub (checkout, setup-python, setup-uv, zizmor-action).
- Mise à jour de plusieurs dépendances Python (pydantic-settings, python-multipart, pyjwt).

### Autres changements
- Publication de la version 0.34.1 de l'API. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)
