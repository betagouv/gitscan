## Changelog : qualicharge (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'automatisation de la mise à jour des unités opérationnelles via l'API, l'extension des indicateurs de volume au niveau des unités opérationnelles et la mise à jour de plusieurs dépendances pour améliorer la sécurité et la stabilité du système.

### Évolutions fonctionnelles
- Automatisation de la mise à jour des unités opérationnelles via l'API. [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9)
- Extension des indicateurs de volume aux unités opérationnelles, permettant une analyse plus granulaire. [#1527322](https://github.com/MTES-MCT/qualicharge/commit/1527322)

### Évolutions techniques
- Mise à jour de Django vers la version 6.0.5 incluant des correctifs de sécurité. [#f7364a3](https://github.com/MTES-MCT/qualicharge/commit/f7364a3)
- Mise à jour de la librairie Mako vers la version 1.3.12. [#41f2480](https://github.com/MTES-MCT/qualicharge/commit/41f2480)
- Mises à jour des images Docker pour `curlimages/curl`, `astral-sh/uv` et `metabase/metabase` pour bénéficier des dernières corrections et améliorations.
- Mise à jour de Terraform vers la version 1.14.9. [#d6abc19](https://github.com/MTES-MCT/qualicharge/commit/d6abc19)

### Autres changements
- Mises à jour de dépendances mineures (urllib3, python-dotenv, astral-sh/uv) pour corriger des vulnérabilités et améliorer la stabilité. Ces mises à jour sont gérées automatiquement par Dependabot et Renovate.
