## Changelog : qualicharge (30 derniers jours, au 14 juillet 2026)

### Résumé
Les récentes mises à jour de QualiCharge améliorent la précision des données de supervision des bornes de recharge, notamment en incluant les bornes hors service et en affinant les indicateurs de session. Des corrections ont également été apportées pour garantir la validité des tarifs et des requêtes de données. Enfin, les dépendances du projet ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Ajout d'un indicateur E1-DMR pour une meilleure identification des données. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431)
- Ajout d'un indicateur E5. [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)

### Évolutions techniques
- Correction d'une erreur dans Prefect concernant la plage de temps des requêtes sur la table `lateststatus`. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Inclusion des points de charge hors service dans les calculs Prefect. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Correction d'un décalage de 15 jours pour les indicateurs de session dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
- Mise à jour de plusieurs dépendances Docker (Keycloak, Metabase, Locust, Curl, Terraform, UV) vers leurs dernières versions stables.
- Mise à jour des actions GitHub (checkout, setup-python, setup-uv, zizmor-action).
- Mise à jour des dépendances Python pour corriger des vulnérabilités de sécurité (pydantic-settings, python-multipart, pyjwt).

### Autres changements
- Publication de la version 0.34.1 de l'API. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)
