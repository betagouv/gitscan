## Changelog : qualicharge (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la gestion des tarifs de recharge via l'API, ainsi que sur la maintenance et la sécurité des dépendances du projet. Une nouvelle version (0.34.0) a été publiée incluant ces changements.

### Évolutions fonctionnelles
- Ajout du support des tarifs de recharge via l'API. [#37a19af](https://github.com/MTES-MCT/qualicharge/commit/37a19af)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité :
    - Starlette (au moins v1.0.1)
    - Prefect (v3.6.28)
    - idna (v3.15)
    - data7 (v1.0.2)
- Mise à jour des images Docker `astral-sh/uv` et `hashicorp/terraform`.
- Mise à jour de l'action `zizmorcore/zizmor-action`.

### Autres changements
- Publication de la version 0.34.0 de l'API. [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26)
