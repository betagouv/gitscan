## Changelog : eva (30 derniers jours, au 15 mai 2026)

### Résumé
Ce changelog couvre une période de maintenance et d'amélioration technique pour le projet eva. Les efforts se sont concentrés sur la mise à jour des dépendances, l'amélioration de la compatibilité avec les dernières versions de tooling (Jest, Webpack, ESLint) et la correction de bugs mineurs. Ces mises à jour visent à assurer la stabilité et la pérennité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug concernant la restitution de l'ancienne consigne d'objet trouvé. [#cb57c4b](https://github.com/betagouv/eva/commit/cb57c4b)

### Évolutions techniques
- Mise à jour de Jest vers la version 29, avec correction des tests associés. [#92b5e82](https://github.com/betagouv/eva/commit/92b5e82) et [#ccbe8a6](https://github.com/betagouv/eva/commit/ccbe8a6)
- Migration du `sass-loader` vers l'API moderne. [#da9a778](https://github.com/betagouv/eva/commit/da9a778)
- Mise à jour de Webpack Dev Server vers la version 5.2.1 [#c1b4893](https://github.com/betagouv/eva/commit/c1b4893)
- Mise à jour de ESLint vers la version 10. [#231042e](https://github.com/betagouv/eva/commit/231042e)
- Actualisation de nombreuses dépendances mineures et transitives pour améliorer la sécurité et la performance. [#ea9e9d9](https://github.com/betagouv/eva/commit/ea9e9d9), [#7a70151](https://github.com/betagouv/eva/commit/7a70151), [#5e057f5](https://github.com/betagouv/eva/commit/5e057f5), [#2a179ea](https://github.com/betagouv/eva/commit/2a179ea), [#033ed07](https://github.com/betagouv/eva/commit/033ed07)
- Refactorisation des fichiers SCSS pour supprimer les alertes de dépréciation. [#12768dc](https://github.com/betagouv/eva/commit/12768dc)
