## Changelog : hubee (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'architecture de Hubee, l'amélioration de la sécurité et la mise en place d'outils d'automatisation pour la gestion des dépendances et l'intégration continue. Ces changements préparent le terrain pour de futures évolutions et renforcent la robustesse de la plateforme.

### Évolutions techniques
- Refactorisation de l'architecture vers une approche modulaire avec des namespaces dédiés pour l'API, le Portail et le cœur de Hubee [#69](https://github.com/datagouv/hubee/pull/69).
- Mise en place de Renovate pour la gestion automatisée des mises à jour de dépendances [#72](https://github.com/datagouv/hubee/pull/72).
- Ajout d'une CI GitHub Actions et d'un hook pre-commit pour améliorer le processus de développement et garantir la qualité du code [#70](https://github.com/datagouv/hubee/pull/70).
- Gel de la version de l'API V2, passage à PostgreSQL 18 et Ruby 4.0.5 [#65](https://github.com/datagouv/hubee/pull/65).
- Mise à jour des gems et suppression des contraintes de version pour simplifier la gestion des dépendances [#66](https://github.com/datagouv/hubee/pull/66).
- Adoption du plugin `hubee-claude-plugin` comme source de vérité pour l'intégration de l'IA [#67](https://github.com/datagouv/hubee/pull/67).

### Autres changements
- Documentation : interdiction des références confidentielles dans le dépôt public, renforçant la sécurité des informations sensibles [#68](https://github.com/datagouv/hubee/pull/68).
