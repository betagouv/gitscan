## Changelog : qualicharge (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Qualicharge se concentrent sur l'automatisation de la mise à jour des unités opérationnelles, des corrections de sécurité et des mises à jour de dépendances pour assurer la stabilité et la sécurité de la plateforme. Une nouvelle version (0.34.0) a été publiée avec ces améliorations.

### Évolutions fonctionnelles
- Automatisation de la mise à jour des unités opérationnelles [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9) : Simplifie la gestion et la maintenance des données relatives aux unités opérationnelles.

### Évolutions techniques
- Mise à jour de Django en version 6.0.5 [#f7364a3](https://github.com/MTES-MCT/qualicharge/commit/f7364a3) : Inclut des correctifs de sécurité importants.
- Mise à jour de Prefect en version 3.6.28 [#8bb79d7](https://github.com/MTES-MCT/qualicharge/commit/8bb79d7) : Corrige une vulnérabilité de sécurité.
- Mises à jour régulières des dépendances : Plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations (data7, starlette, idna, urllib3, mako).
- Mises à jour de l'image Docker astral-sh/uv et hashicorp/terraform : Assurent la compatibilité avec les dernières versions et bénéficient des améliorations de performance.

### Autres changements
- Publication de la version 0.34.0 [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26) : Intègre les évolutions fonctionnelles et techniques mentionnées ci-dessus.
- Mise à jour de l'image Docker metabase/metabase en version 0.60.4.
- Mise à jour de l'image Docker curlimages/curl en version 8.20.0.
