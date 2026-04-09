## Changelog : eva (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur la mise à jour des dépendances du projet, notamment les outils de développement et de test. Ces mises à jour visent à améliorer la stabilité, la sécurité et les performances de la plateforme. Une correction a également été apportée pour restaurer une fonctionnalité précédente concernant les consignes d'objets.

### Évolutions techniques
- Mise à jour de Jest de la version 27 à la version 29, incluant la correction des tests associés. [#92b5e82](https://github.com/betagouv/eva/commit/92b5e82)
- Migration de `sass-loader` vers l'API moderne pour une meilleure compatibilité et performance. [#da9a778](https://github.com/betagouv/eva/commit/da9a778)
- Mise à jour de Webpack Dev Server de la version 4.15.2 à la version 5.2.1. [#c1b4893](https://github.com/betagouv/eva/commit/c1b4893)
- Actualisation de plusieurs dépendances mineures (lint-staged, webpack-node-externals, workbox-webpack-plugin). [#2a179ea](https://github.com/betagouv/eva/commit/2a179ea)
- Mise à jour d'ESLint vers la version 10. [#231042e](https://github.com/betagouv/eva/commit/231042e)
- Actualisation des fichiers SCSS pour supprimer les alertes de dépréciation. [#12768dc](https://github.com/betagouv/eva/commit/12768dc)

### Autres changements
- Restauration de la consigne d'objet précédente. [#cb57c4b](https://github.com/betagouv/eva/commit/cb57c4b)
