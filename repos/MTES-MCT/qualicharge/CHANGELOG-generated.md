## Changelog : qualicharge (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données disponibles via l'API, notamment avec l'ajout du support des tarifs de recharge. Des mises à jour automatiques de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout du support des tarifs de recharge via l'API. [#37a19af](https://github.com/MTES-MCT/qualicharge/pull/37a19af)
- Automatisation de la mise à jour des unités opérationnelles via l'API. [#42f10b9](https://github.com/MTES-MCT/qualicharge/pull/42f10b9)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité :
    - Starlette (version >= 1.0.1) [#6960978](https://github.com/MTES-MCT/qualicharge/pull/6960978)
    - Prefect (version 3.6.28) [#8bb79d7](https://github.com/MTES-MCT/qualicharge/pull/8bb79d7)
    - urllib3 (version 2.7.0) [#e12bd72](https://github.com/MTES-MCT/qualicharge/pull/e12bd72)
    - idna (version 3.15) [#868965b](https://github.com/MTES-MCT/qualicharge/pull/868965b)
- Mises à jour de `uv`, `ghcr.io/astral-sh/uv`, `hashicorp/terraform`, `zizmorcore/zizmor-action`, `curlimages/curl` et `data7` via Renovate et Dependabot.

### Autres changements
- Publication de la version 0.34.0 de l'API. [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26)
