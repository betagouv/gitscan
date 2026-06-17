## Changelog : qualicharge (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement de l'API avec la prise en charge des tarifs de recharge, ainsi que sur la maintenance et la sécurité des dépendances du projet. Une nouvelle version (0.34.0) a été publiée avec ces améliorations.

### Évolutions fonctionnelles
- Ajout de la prise en charge des tarifs de recharge via l'API. [#37a19af](https://github.com/MTES-MCT/qualicharge/pull/37a19af)
- Automatisation de la mise à jour des unités opérationnelles via l'API. [#42f10b9](https://github.com/MTES-MCT/qualicharge/pull/42f10b9)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité :
    - `starlette` (au moins v1.0.1)
    - `prefect` (v3.6.28)
    - `idna` (v3.15)
    - `data7` (v1.0.2)
- Mise à jour des images Docker `astral-sh/uv` et `hashicorp/terraform`.
- Publication de la version 0.34.0 de l'API. [#c30eb26](https://github.com/MTES-MCT/qualicharge/tag/0.34.0)
