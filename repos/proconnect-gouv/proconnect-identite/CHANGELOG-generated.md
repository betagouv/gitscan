## Changelog : proconnect-identite (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se concentrent sur l'amélioration de l'expérience utilisateur en fournissant des informations plus claires en cas d'erreur OIDC et en affinant les messages d'erreur pour les certifications de dirigeants. Des optimisations techniques ont également été apportées, notamment au niveau des tests et de la gestion des dépendances.

### Évolutions fonctionnelles
- Amélioration des messages d'erreur pour les rejets de certification de dirigeants, avec un conseil à l'utilisateur de consulter son email. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pull/1927)
- Ajout d'une description d'erreur OIDC pour une meilleure information des utilisateurs et des partenaires ProConnect. [#1914](https://github.com/proconnect-gouv/proconnect-identite/pull/1914)
- Modification de la vue `close-match-error.ejs` pour la certification de dirigeant. [#1914](https://github.com/proconnect-gouv/proconnect-identite/pull/1914)

### Évolutions techniques
- Refactorisation du "seed" de la base de données pour être exécuté avant les tests E2E, améliorant ainsi la fiabilité des tests. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- Mise à jour de plusieurs dépendances : Redis (7.2.14), Prettier (3.8.3), Lodash (4.18.1), Hono (4.12.18), Cypress GitHub Action (7.3.0), actions/labeler (6.1.0).
- Tentative de mise à jour de la version de Node (de 24-slim à 26-slim) puis annulation suite à des problèmes. [#1921](https://github.com/proconnect-gouv/proconnect-identite/pull/1921)

### Autres changements
- Mise à jour des dépendances de développement Sentry. [#1908](https://github.com/proconnect-gouv/proconnect-identite/pull/1908)
- Mise à jour de la dépendance dotenvx. [#1909](https://github.com/proconnect-gouv/proconnect-identite/pull/1909)
