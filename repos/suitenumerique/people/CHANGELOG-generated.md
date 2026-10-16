## Changelog : people (30 derniers jours, au 12 octobre 2026)

### Résumé
Cette période a été marquée par une simplification majeure de l'application avec le retrait des fonctionnalités liées à OAuth2 et aux fournisseurs d'identité. La sécurité a été renforcée, notamment sur la gestion des domaines et des permissions, tandis que l'infrastructure de développement et les outils de contrôle de qualité du code ont été modernisés.

### Évolutions fonctionnelles
- **Sécurité et permissions** : les utilisateurs ayant un rôle de "lecteur de domaine" n'ont plus accès à la configuration des domaines.
- **Gestion des domaines** : amélioration de la précision de la correspondance des domaines de messagerie des organisations.
- **Simplification de l'offre** : suppression des fonctionnalités liées à OAuth2 et aux fournisseurs d'identité (IdP).

### Évolutions techniques
- **CI/CD** : mise à jour de plusieurs GitHub Actions (setup-python, setup-node, checkout, cache, upload-artifact).
- **Sécurité** : mise à jour de la bibliothèque `urllib3` vers la version 2.8.0.
- **Qualité du code et Frontend** : migration vers ESLint 9, transformation de la configuration `eslint-config-people` en plugin et application des nouvelles règles de linting.
- **Base de données** : suppression des tables obsolètes liées à OAuth2.

### Autres changements
- **Internationalisation** : mise à jour des chaînes de traduction et de la configuration i18n.
- **Maintenance** : mise à jour des configurations applicatives (desk app, e2e) et refactorisation de variables pour la conformité Sonar.
