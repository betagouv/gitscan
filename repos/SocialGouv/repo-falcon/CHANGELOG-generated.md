## Changelog : repo-falcon (30 derniers jours)

### Résumé
Ce mois-ci, repo-falcon a connu une progression significative, avec une attention particulière portée à l'intégration avec des agents de codage comme Claude. De nombreuses améliorations ont été apportées à l'installation, à la configuration et à l'expérience utilisateur, ainsi qu'à l'automatisation des processus de publication grâce à l'amélioration des workflows CI/CD. Plusieurs versions ont été publiées, témoignant d'un rythme de développement soutenu.

### Évolutions fonctionnelles
- Amélioration de l'intégration avec les agents de codage, notamment pour l'utilisation de Claude [#1234](https://github.com/SocialGouv/repo-falcon/issues/1234).
- Ajout de la recherche multi-dépôts dans la fonctionnalité "fleet".
- Support de davantage d'agents de codage.
- Amélioration de l'expérience utilisateur pour l'intégration des agents.
- Mise en place d'une fonctionnalité d'auto-intégration pour les agents de codage.
- Amélioration des templates de prompting pour les agents de codage.
- Correction de l'analyse AST pour JavaScript et TypeScript, améliorant la compréhension du code.

### Évolutions techniques
- Mise en place d'un système de CI/CD complet avec gestion de la versioning et publication automatisée.
- Refonte de l'installation et de la configuration avec l'utilisation de devbox et de hooks pre-commit.
- Correction de problèmes liés à la construction Docker avec CGO.
- Ajout de tests d'intégration (e2e).
- Amélioration de la gestion de la concurrence dans les workflows CI.
- Correction de problèmes liés à la gestion des dépendances et au vendor Go.
- Utilisation de direnv et devbox pour un environnement de développement plus cohérent.
- Amélioration de la gestion des versions et des publications.

### Autres changements
- Amélioration de la documentation pour l'installation et l'utilisation de repo-falcon.
- Correction de bugs mineurs et amélioration de la convivialité générale.
- Ajout d'une commande séparée pour la configuration de l'agent.
- Amélioration des scripts d'installation.
