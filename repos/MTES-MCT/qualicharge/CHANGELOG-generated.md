## Changelog : qualicharge (30 derniers jours, au 14 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à l'API, notamment en exigeant au moins une cible lors de la création d'un tarif. Des corrections ont également été apportées aux requêtes Prefect pour une meilleure gestion des données des bornes de recharge, incluant celles qui ont été désactivées. Enfin, des indicateurs de session (e1-DMR et e5) ont été ajoutés.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Ajout d'indicateurs de session e1-DMR et e5 pour une analyse plus fine des données. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431) et [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)

### Évolutions techniques
- Correction d'une erreur dans Prefect concernant la plage de temps des requêtes sur la table `lateststatus`. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Inclusion des points de recharge désactivés dans les requêtes Prefect. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Mise à jour de plusieurs dépendances Docker (Keycloak, Metabase, Locust, Curl, Terraform) et actions GitHub (checkout, setup-python, setup-uv, zizmor-action).
- Mise à jour de plusieurs dépendances Python (pydantic-settings, python-multipart, pyjwt).
- Bump de la version de release à 0.34.1 [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)

### Autres changements
- Amélioration de la gestion des indicateurs de session avec un offset de 15 jours dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
