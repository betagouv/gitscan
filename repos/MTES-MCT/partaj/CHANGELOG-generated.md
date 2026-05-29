## Changelog : partaj (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Partaj se sont concentrées sur l'amélioration de l'expérience utilisateur, notamment en permettant aux demandeurs de voir la relation de parrainage et en corrigeant des blocages lors de la validation de sous-saisines. Des mises à jour techniques importantes ont également été réalisées pour moderniser les dépendances et améliorer la stabilité des tests.

### Évolutions fonctionnelles
- Les demandeurs peuvent désormais visualiser la relation de parrainage associée à leur saisine. [#a3f978d](https://github.com/MTES-MCT/partaj/commit/a3f978d)
- Correction d'un blocage lors de la validation d'une sous-saisine. [#85b8735](https://github.com/MTES-MCT/partaj/commit/85b8735)
- Correction d'un problème d'affichage d'image dans le module "jedonnemonavis". [#04d3b0e](https://github.com/MTES-MCT/partaj/commit/04d3b0e)

### Évolutions techniques
- Mise à jour de React vers la version 18. [#b53d2ab](https://github.com/MTES-MCT/partaj/commit/b53d2ab)
- Mise à jour de la librairie `react-query` vers `tanstack`. [#bb2db0c](https://github.com/MTES-MCT/partaj/commit/bb2db0c)
- Mise à jour de la version de Jest et ajout d'un délai pour les tests front-end afin d'améliorer leur stabilité. [#607a7e0](https://github.com/MTES-MCT/partaj/commit/607a7e0), [#c0f61ff](https://github.com/MTES-MCT/partaj/commit/c0f61ff)
- Mise à jour de la version de React Router. [#4004cc0](https://github.com/MTES-MCT/partaj/commit/4004cc0)
- Synchronisation des versions de PostgreSQL, Elasticsearch et Django. [#185ac4b](https://github.com/MTES-MCT/partaj/commit/185ac4b)
- Ajout du tag GCP sur l'ensemble des jobs CI pour une meilleure identification de l'environnement. [#e2860b1](https://github.com/MTES-MCT/partaj/commit/e2860b1)

### Autres changements
- Ajout de tests pour la fonctionnalité de parrainage. [#67024a7](https://github.com/MTES-MCT/partaj/commit/67024a7)
- Correction d'un problème dans l'environnement de test. [#be16579](https://github.com/MTES-MCT/partaj/commit/be16579)
- Force des notifications synchrones à des fins de test. [#6d55f83](https://github.com/MTES-MCT/partaj/commit/6d55f83)
