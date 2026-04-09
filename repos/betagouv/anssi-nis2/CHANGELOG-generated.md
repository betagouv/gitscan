## Changelog : anssi-nis2 (30 derniers jours, au 3 mai 2026)

### Résumé
Ce projet a connu une évolution majeure avec le remplacement de l'application complète par un simple serveur web statique. Cette modification simplifie considérablement le déploiement et la maintenance de l'application, tout en conservant l'accès aux informations essentielles sur la directive NIS 2. Les fonctionnalités interactives, comme la simulation et le calcul, ne sont plus disponibles dans cette version.

### Évolutions fonctionnelles
- L'application est désormais servie comme un site web statique. Les fonctionnalités dynamiques ont été supprimées.

### Évolutions techniques
- Remplacement complet de l'application par un serveur web statique. [#1234](https://github.com/betagouv/anssi-nis2/issues/1234)
- Suppression de l'API REST et GraphQL, ainsi que de la base de données PostgreSQL.
- Suppression des tests Jest et Vitest.
- Suppression des workflows de CI/CD (checkov.yml, deploiement.yml, node.js.yml).
