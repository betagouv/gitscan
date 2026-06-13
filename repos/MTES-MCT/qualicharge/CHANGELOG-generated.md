## Changelog : qualicharge (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement de l'API avec la prise en charge des tarifs de recharge, ainsi que sur l'automatisation de la mise à jour des unités opérationnelles. Des mises à jour de sécurité et des corrections de dépendances ont également été apportées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la prise en charge des tarifs de recharge via l'API. [#37a19af](https://github.com/MTES-MCT/qualicharge/commit/37a19af)
- Automatisation de la mise à jour des unités opérationnelles. [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9)

### Évolutions techniques
- Mise à jour de Prefect vers la version 3.6.28 incluant des correctifs de sécurité. [#8bb79d7](https://github.com/MTES-MCT/qualicharge/commit/8bb79d7)
- Mises à jour de plusieurs dépendances (uv, terraform, zizmor-action) pour bénéficier des dernières corrections et améliorations.
- Bump de la version de l'API vers 0.34.0 [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26)

### Autres changements
- Mise à jour des dépendances `pyarrow`, `starlette`, `data7` et `idna` pour corriger des vulnérabilités et améliorer la stabilité.
- Mises à jour mineures de l'infrastructure Docker et des outils CI/CD.
