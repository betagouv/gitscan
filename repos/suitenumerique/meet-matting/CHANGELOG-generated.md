## Changelog : meet-matting (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la qualité de la segmentation de l'arrière-plan, notamment en affinant les seuils de détection et en corrigeant des bugs.  Un travail important a également été réalisé pour mettre en place un benchmark permettant d'évaluer et d'optimiser les performances du système.

### Évolutions fonctionnelles
- Amélioration de la segmentation de l'arrière-plan grâce à l'optimisation des seuils de détection [#ddb9755](https://github.com/suitenumerique/meet-matting/commit/ddb9755).
- Correction d'un bug dans le comparateur visuel [#a02b28c](https://github.com/suitenumerique/meet-matting/commit/a02b28c).
- Résolution d'un bug lié à la compatibilité sur macOS [#e02fabc](https://github.com/suitenumerique/meet-matting/commit/e02fabc).
- Correction d'un problème lié aux erreurs de warping de flux [#1c31f53](https://github.com/suitenumerique/meet-matting/commit/1c31f53).

### Évolutions techniques
- Mise en place d'un benchmark pour mesurer les performances du système, incluant le calcul de la latence P95 et des métriques d'évaluation comme l'IoU et la Boundary F-measure [#52aecbd](https://github.com/suitenumerique/meet-matting/commit/52aecbd), [#b58e79e](https://github.com/suitenumerique/meet-matting/commit/b58e79e), [#fc30a41](https://github.com/suitenumerique/meet-matting/commit/fc30a41).
- Optimisation et correction du workflow de benchmark [#7218fb5](https://github.com/suitenumerique/meet-matting/commit/7218fb5).
- Implémentation de plusieurs seuils pour une analyse plus avancée [#485e71b](https://github.com/suitenumerique/meet-matting/commit/485e71b).
- Initialisation du projet et des premiers commits [#2c8e2dc](https://github.com/suitenumerique/meet-matting/commit/2c8e2dc), [#cfaea70](https://github.com/suitenumerique/meet-matting/commit/cfaea70).

### Autres changements
- Ajout de traductions [#fb6aab7](https://github.com/suitenumerique/meet-matting/commit/fb6aab7).
- Mise à jour de la documentation des métriques [#2991c71](https://github.com/suitenumerique/meet-matting/commit/2991c71).
- Ajout d'un fichier `.gitignore` [#0704030](https://github.com/suitenumerique/meet-matting/commit/0704030).
- Résolution de conflits dans le fichier README [#5c6579b](https://github.com/suitenumerique/meet-matting/commit/5c6579b).
