## Changelog : qualicharge (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Qualicharge se concentrent sur l'automatisation de la mise à jour des unités opérationnelles et l'amélioration de la sécurité grâce à la mise à jour de plusieurs dépendances critiques. Des mises à jour régulières de l'infrastructure et des outils ont également été effectuées pour maintenir la plateforme à jour et performante.

### Évolutions fonctionnelles
- Automatisation de la mise à jour des unités opérationnelles via l'API. [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9)

### Évolutions techniques
- Mise à jour de Django en version 6.0.5, incluant des correctifs de sécurité. [#f7364a3](https://github.com/MTES-MCT/qualicharge/commit/f7364a3)
- Mise à jour de `uv` (outil de gestion des dépendances Python) en version 0.11.16. [#726ef75](https://github.com/MTES-MCT/qualicharge/commit/726ef75) et [#8effd32](https://github.com/MTES-MCT/qualicharge/commit/8effd32)
- Mise à jour de `mako` (moteur de template) en version 1.3.12. [#41f2480](https://github.com/MTES-MCT/qualicharge/commit/41f2480)
- Mise à jour de l'image Docker `metabase/metabase` en version 0.60.4. [#ac0001d](https://github.com/MTES-MCT/qualicharge/commit/ac0001d)
- Mise à jour de l'image Docker `curlimages/curl` en version 8.20.0. [#8738d93](https://github.com/MTES-MCT/qualicharge/commit/8738d93)
- Mise à jour de `prefect` en version 3.6.28, incluant des correctifs de sécurité. [#8bb79d7](https://github.com/MTES-MCT/qualicharge/commit/8bb79d7)

### Autres changements
- Application de mises à jour de sécurité pour les dépendances `idna` et `urllib3`. [#868965b](https://github.com/MTES-MCT/qualicharge/commit/868965b) et [#e12bd72](https://github.com/MTES-MCT/qualicharge/commit/e12bd72)
- Bump de la release en version 0.34.0. [#c30eb26](https://github.com/MTES-MCT/qualicharge/commit/c30eb26)
- Mises à jour mineures de l'action `zizmorcore/zizmor-action`. [#8effd32](https://github.com/MTES-MCT/qualicharge/commit/8effd32)
- Application de correctifs de sécurité généraux. [#172a8f5](https://github.com/MTES-MCT/qualicharge/commit/172a8f5)
