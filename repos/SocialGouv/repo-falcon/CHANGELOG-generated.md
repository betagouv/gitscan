## Changelog : repo-falcon (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par une progression significative de repo-falcon, avec l'ajout de nouvelles fonctionnalités, notamment l'intégration d'agents de codage et la recherche multi-dépôts. De nombreuses améliorations ont également été apportées à l'installation, à la documentation et aux workflows CI/CD, rendant l'outil plus facile à utiliser et à intégrer dans les pipelines existants. Une série de corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité du projet.

### Évolutions fonctionnelles
- Ajout de la recherche multi-dépôts via l'API Fleet. [#9cf8a22](https://github.com/SocialGouv/repo-falcon/commit/9cf8a22)
- Amélioration de l'intégration avec les agents de codage, notamment pour Claude. [#b6761bf](https://github.com/SocialGouv/repo-falcon/commit/b6761bf), [#c2534d3](https://github.com/SocialGouv/repo-falcon/commit/c2534d3), [#150ddd2](https://github.com/SocialGouv/repo-falcon/commit/150ddd2), [#634134d](https://github.com/SocialGouv/repo-falcon/commit/634134d)
- Prise en charge de davantage d'agents de codage. [#c2534d3](https://github.com/SocialGouv/repo-falcon/commit/c2534d3)
- Amélioration des modèles de prompting pour les agents de codage. [#bee6ac6](https://github.com/SocialGouv/repo-falcon/commit/bee6ac6)
- Intégration automatique des agents de codage. [#abb4b8e](https://github.com/SocialGouv/repo-falcon/commit/abb4b8e)
- Amélioration de la correction de l'AST (Abstract Syntax Tree) pour JavaScript et TypeScript. [#4ac82ed](https://github.com/SocialGouv/repo-falcon/commit/4ac82ed), [#17b79a0](https://github.com/SocialGouv/repo-falcon/commit/17b79a0)

### Évolutions techniques
- Mise en place d'un système de versioning et de release plus robuste avec les workflows CI/CD. [#a237ea9](https://github.com/SocialGouv/repo-falcon/commit/a237ea9)
- Amélioration du script d'installation et de la documentation associée. [#81e39ca](https://github.com/SocialGouv/repo-falcon/commit/81e39ca)
- Correction d'un problème de build Docker lié à CGO. [#e51e210](https://github.com/SocialGouv/repo-falcon/commit/e51e210)
- Ajout de tests E2E (End-to-End). [#b665f88](https://github.com/SocialGouv/repo-falcon/commit/b665f88)
- Correction de problèmes de concurrence dans les workflows CI. [#6033a3a](https://github.com/SocialGouv/repo-falcon/commit/6033a3a)
- Utilisation de devbox et pre-commit hooks pour améliorer l'environnement de développement. [#d576391](https://github.com/SocialGouv/repo-falcon/commit/d576391)
- Ajout d'une action GitHub pour faciliter l'intégration. [#b02e4b5](https://github.com/SocialGouv/repo-falcon/commit/b02e4b5)

### Autres changements
- Amélioration de la documentation pour l'installation et l'utilisation de l'outil. [#7767bd8](https://github.com/SocialGouv/repo-falcon/commit/7767bd8), [#a86cdab](https://github.com/SocialGouv/repo-falcon/commit/a86cdab)
- Correction de la version affichée par l'interface CLI. [#41c29e1](https://github.com/SocialGouv/repo-falcon/commit/41c29e1)
- Amélioration de la cohérence et de la documentation de l'interface CLI. [#bed1ed2](https://github.com/SocialGouv/repo-falcon/commit/bed1ed2)
- Correction d'un problème lié aux permissions refusées. [#889a8f7](https://github.com/SocialGouv/repo-falcon/commit/889a8f7)
- Ajout d'un fix temporaire en attendant une nouvelle release de mlugg/setup-zig. [#1733335](https://github.com/SocialGouv/repo-falcon/commit/1733335)
- Nettoyage du code et formatage avec `fmt`. [#f0bbfb6](https://github.com/SocialGouv/repo-falcon/commit/f0bbfb6)
- Ajout d'un hook git pour assurer la qualité du code. [#f0bbfb6](https://github.com/SocialGouv/repo-falcon/commit/f0bbfb6)
