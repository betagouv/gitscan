## Changelog : eva (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur la mise à jour des dépendances du projet, notamment les outils de développement et de test, ainsi que sur la modernisation du code pour éviter les dépréciations. Ces mises à jour visent à améliorer la stabilité, la performance et la maintenabilité de la plateforme.

### Évolutions techniques
- Mise à jour de Jest de la version 27 à la version 29, nécessitant une correction des tests associés. [#92b5e82](https://github.com/betagouv/eva/commit/92b5e82)
- Migration du `sass-loader` vers son API moderne pour une meilleure compatibilité et performance. [#da9a778](https://github.com/betagouv/eva/commit/da9a778)
- Mise à jour de Webpack Dev Server de la version 4.15.2 à la version 5.2.1. [#c1b4893](https://github.com/betagouv/eva/commit/c1b4893)
- Mise à jour d'ESLint vers la version 10. [#231042e](https://github.com/betagouv/eva/commit/231042e)
- Refactorisation des fichiers SCSS pour supprimer les alertes de dépréciation et assurer la compatibilité future. [#12768dc](https://github.com/betagouv/eva/commit/12768dc)
- Mise à jour de plusieurs dépendances mineures : `lint-staged`, `webpack-node-externals`, `workbox-webpack-plugin`, `@tootallnate/once`, `jest-environment-jsdom` et `rollbar`. [#ea9e9d9](https://github.com/betagouv/eva/commit/ea9e9d9), [#2a179ea](https://github.com/betagouv/eva/commit/2a179ea), [#033ed07](https://github.com/betagouv/eva/commit/033ed07)

### Autres changements
- Mise à jour des dépendances transitives pour assurer la cohérence du projet. [#7a70151](https://github.com/betagouv/eva/commit/7a70151)
- Mise à jour des dépendances mineures. [#5e057f5](https://github.com/betagouv/eva/commit/5e057f5)
