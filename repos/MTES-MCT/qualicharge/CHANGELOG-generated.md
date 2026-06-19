## Changelog : qualicharge (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la gestion des tarifs de recharge via l'API, ainsi que sur la maintenance et la sécurisation des dépendances du projet. Une nouvelle version (0.34.0) a été publiée.

### Évolutions fonctionnelles
- Ajout du support des tarifs de recharge via l'API. [#37a19af](https://github.com/MTES-MCT/qualicharge/commit/37a19af)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité :
    - Starlette (au moins v1.0.1) [#6960978](https://github.com/MTES-MCT/qualicharge/commit/6960978)
    - Prefect (v3.6.28 - correction de sécurité) [#8bb79d7](https://github.com/MTES-MCT/qualicharge/commit/8bb79d7)
    - idna (v3.15) [#868965b](https://github.com/MTES-MCT/qualicharge/commit/868965b)
    - data7 (v1.0.2) [#82d7b18](https://github.com/MTES-MCT/qualicharge/commit/82d7b18)
    - pyarrow (v23.0.1) [#9cfc1a2](https://github.com/MTES-MCT/qualicharge/commit/9cfc1a2)
- Mise à jour des images Docker `astral-sh/uv` et `hashicorp/terraform`.
- Publication de la version 0.34.0 de l'API. [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26)
