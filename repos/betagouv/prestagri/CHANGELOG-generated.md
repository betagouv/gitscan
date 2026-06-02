## Changelog : prestagri (30 derniers jours, au 1er juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'ajout et l'amélioration du calcul du quotient familial, une fonctionnalité essentielle pour déterminer l'éligibilité aux prestations sociales.  Des travaux ont également été réalisés pour intégrer et utiliser le module Catala, et pour moderniser l'environnement de gestion des dépendances.

### Évolutions fonctionnelles
- Ajout du calcul du quotient familial spécifique à l'aide scolaire [#8f54964](https://github.com/betagouv/prestagri/commit/8f54964).
- Implémentation du calcul général du quotient familial [#ce6b60d](https://github.com/betagouv/prestagri/commit/ce6b60d).
- Première version du calcul du quotient familial disponible [#dd7d9c4](https://github.com/betagouv/prestagri/commit/dd7d9c4).
- Ajout d'une route d'éligibilité [#f066037](https://github.com/betagouv/prestagri/commit/f066037).

### Évolutions techniques
- Remplacement du package Catala par un module généré, améliorant ainsi la maintenabilité et la performance [#49d9263](https://github.com/betagouv/prestagri/commit/49d9263).
- Utilisation du module Python généré dans l'application web [#37ebb2b](https://github.com/betagouv/prestagri/commit/37ebb2b).
- Nettoyage et simplification du code lié au quotient familial [#e62698c](https://github.com/betagouv/prestagri/commit/e62698c).
- Migration de la gestion des dépendances de Poetry à uv [#aadffc0](https://github.com/betagouv/prestagri/commit/aadffc0).

### Autres changements
- Ajout de Catala aux références du projet [#726b05b](https://github.com/betagouv/prestagri/commit/726b05b).
- Correction d'une erreur d'import [#f4bc0b9](https://github.com/betagouv/prestagri/commit/f4bc0b9).
- Correction de la page Catala dans la documentation [#4c0fbf6](https://github.com/betagouv/prestagri/commit/4c0fbf6).
