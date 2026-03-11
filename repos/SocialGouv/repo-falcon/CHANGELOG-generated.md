## Changelog : repo-falcon (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à repo-falcon, un outil d'analyse de code qui transforme un dépôt en artefacts déterministes et en un graphe de connaissances. Les efforts récents se sont concentrés sur l'amélioration de l'intégration avec les agents de codage (Claude), l'automatisation du processus de CI/CD, et l'amélioration de la documentation et de l'expérience de développement. Plusieurs versions ont été publiées au cours de la période.

### Évolutions fonctionnelles
- Amélioration du template de prompting pour l'agent de codage Claude [#150ddd2](https://github.com/SocialGouv/repo-falcon/commit/150ddd2).
- Intégration automatique de l'agent de codage [#abb4b8e](https://github.com/SocialGouv/repo-falcon/commit/abb4b8e).
- L'agent de codage est maintenant prêt à l'emploi [#160fc5e](https://github.com/SocialGouv/repo-falcon/commit/160fc5e).
- Correction d'un bug lié à l'intégration de Claude et à son mécanisme de "Message Context Preservation" (MCP) [#150ddd2](https://github.com/SocialGouv/repo-falcon/commit/150ddd2), [#634134d](https://github.com/SocialGouv/repo-falcon/commit/634134d).
- Ajout d'une action GitHub pour l'automatisation [#b02e4b5](https://github.com/SocialGouv/repo-falcon/commit/b02e4b5).

### Évolutions techniques
- Mise en place d'un CI complet et d'un système de versioning automatisé [#a237ea9](https://github.com/SocialGouv/repo-falcon/commit/a237ea9).
- Utilisation de `devbox` et de hooks `pre-commit` pour améliorer l'environnement de développement [#d576391](https://github.com/SocialGouv/repo-falcon/commit/d576391).
- Configuration de `direnv` pour une meilleure gestion des variables d'environnement en développement [#c4ef4d1](https://github.com/SocialGouv/repo-falcon/commit/c4ef4d1).
- Correction de problèmes de concurrence dans le CI [#6033a3a](https://github.com/SocialGouv/repo-falcon/commit/6033a3a).
- Correction de la version du CLI [#41c29e1](https://github.com/SocialGouv/repo-falcon/commit/41c29e1).
- Ajout du vendor go dans le commit [#68f32f3](https://github.com/SocialGouv/repo-falcon/commit/68f32f3).
- Amélioration de la gestion des versions avec un bump conventionnel et pnpm [#efae3ee](https://github.com/SocialGouv/repo-falcon/commit/efae3ee).

### Autres changements
- Amélioration de la documentation et ajout d'informations pour faciliter l'installation et l'utilisation [#a86cdab](https://github.com/SocialGouv/repo-falcon/commit/a86cdab), [#7767bd8](https://github.com/SocialGouv/repo-falcon/commit/7767bd8).
- Publication des versions v0.1.0, v0.1.1, v0.1.2 et v0.1.3.
- Initialisation du dépôt avec un premier commit [#4ea2631](https://github.com/SocialGouv/repo-falcon/commit/4ea2631).
