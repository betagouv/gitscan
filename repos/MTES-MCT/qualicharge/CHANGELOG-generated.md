## Changelog : qualicharge (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'automatisation de la mise à jour des entités opérationnelles et sur la correction de vulnérabilités de sécurité dans plusieurs dépendances du projet. Des mises à jour de versions mineures ont également été effectuées pour améliorer la stabilité et les performances.

### Évolutions fonctionnelles
- Automatisation de la mise à jour des unités opérationnelles via l'API. [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9)

### Évolutions techniques
- Mise à jour de Django vers la version 6.0.5, incluant des correctifs de sécurité. [#f7364a3](https://github.com/MTES-MCT/qualicharge/commit/f7364a3)
- Mise à jour de `uv` vers la version 0.11.16. [#726ef75](https://github.com/MTES-MCT/qualicharge/commit/726ef75) et [#8effd32](https://github.com/MTES-MCT/qualicharge/commit/8effd32)
- Mise à jour de `mako` vers la version 1.3.12 pour corriger des vulnérabilités. [#41f2480](https://github.com/MTES-MCT/qualicharge/commit/41f2480)
- Mise à jour de `urllib3` vers la version 2.7.0 pour corriger des vulnérabilités. [#e12bd72](https://github.com/MTES-MCT/qualicharge/commit/e12bd72)
- Mise à jour de `idna` vers la version 3.15 pour corriger des vulnérabilités. [#868965b](https://github.com/MTES-MCT/qualicharge/commit/868965b)
- Mise à jour de `prefect` vers la version 3.6.28, incluant des correctifs de sécurité. [#8bb79d7](https://github.com/MTES-MCT/qualicharge/commit/8bb79d7)

### Autres changements
- Mise à jour de l'image Docker `curlimages/curl` vers la version 8.20.0. [#8738d93](https://github.com/MTES-MCT/qualicharge/commit/8738d93)
- Mise à jour de l'image Docker `metabase/metabase` vers la version 0.60.4. [#ac0001d](https://github.com/MTES-MCT/qualicharge/commit/ac0001d)
- Bump de la release vers la version 0.34.0. [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26)
- Application de correctifs de sécurité via Dependabot. [#172a8f5](https://github.com/MTES-MCT/qualicharge/commit/172a8f5)
