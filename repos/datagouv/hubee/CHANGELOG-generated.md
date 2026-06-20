## Changelog : hubee (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'architecture interne de la plateforme, la sécurisation des informations et la préparation de l'environnement pour les futures évolutions technologiques. Des ajustements ont également été faits concernant l'utilisation de l'IA et la gestion des dépendances.

### Évolutions techniques
- Refactorisation de l'architecture pour adopter une approche modulaire avec des namespaces dédiés (API, Portail, Hubee) [#69](https://github.com/datagouv/hubee/issues/69).
- Gel de la version de l'API à V2, passage à PostgreSQL 18 et Ruby 4.0.5 [#65](https://github.com/datagouv/hubee/issues/65).
- Mise à jour des gems et suppression des contraintes de version pour faciliter les futures mises à jour [#66](https://github.com/datagouv/hubee/issues/66).
- Adoption du plugin `hubee-claude-plugin` comme source de vérité pour l'intégration de l'IA [#67](https://github.com/datagouv/hubee/issues/67).

### Autres changements
- Interdiction des références à des informations confidentielles dans le dépôt public, renforçant la sécurité des données [#68](https://github.com/datagouv/hubee/issues/68).
