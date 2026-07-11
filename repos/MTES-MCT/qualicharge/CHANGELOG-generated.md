## Changelog : qualicharge (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'analyse des données de recharge, notamment l'ajout d'indicateurs E1-DMR et E5 pour une meilleure supervision. Des corrections ont également été apportées pour affiner le calcul des indicateurs de session. De plus, les dépendances du projet ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Ajout d'indicateurs E1-DMR pour une analyse plus fine des données de recharge. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431)
- Ajout d'indicateur E5. [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)
- Correction du calcul des indicateurs de session avec un décalage de 15 jours. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)

### Évolutions techniques
- Mise à jour de plusieurs dépendances Docker (Keycloak, Metabase, Locust, Curl, Terraform) vers leurs dernières versions.
- Mise à jour des actions GitHub (checkout, setup-python, setup-uv, zizmor-action) vers leurs dernières versions.
- Mise à jour des dépendances Python (pydantic-settings, python-multipart, pyjwt) pour corriger des vulnérabilités et améliorer la stabilité.
- Mise à jour de l'image Docker `ghcr.io/astral-sh/uv`.

### Autres changements
- Publication de la version 0.34.1. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)
