## Changelog : proconnect-identite (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur en cas d'erreur lors de l'authentification, notamment en fournissant des informations plus claires sur les raisons du rejet. Des améliorations techniques ont également été apportées pour optimiser les tests et la gestion des dépendances.

### Évolutions fonctionnelles
- Amélioration du message d'erreur affiché lors du rejet d'une certification de dirigeant, avec un conseil à l'utilisateur de consulter son email pour plus d'informations. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pull/1927)
- Ajout d'une description d'erreur OIDC (OpenID Connect) pour fournir des informations plus précises à ProConnect Federation (PCF) en cas de problème d'authentification. [#1914](https://github.com/proconnect-gouv/proconnect-identite/pull/1914)

### Évolutions techniques
- Refactorisation de la préparation de la base de données avant les tests E2E pour une meilleure efficacité et maintenabilité. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- Mise à jour de plusieurs dépendances :
    - Redis (7.2.13 -> 7.2.14)
    - Prettier (3.8.1 -> 3.8.3)
    - Lodash (4.18.0 -> 4.18.1)
    - Hono (4.12.14 -> 4.12.18)
    - Cypress GitHub Action (7.1.9 -> 7.3.0)
    - Actions/Labeler (6.0.1 -> 6.1.0)
    - @dotenvx/dotenvx (1.55.1 -> 1.61.0)
- Tentative de mise à jour de la version de Node (24-slim -> 26-slim) puis rétractation en raison de problèmes. [#1921](https://github.com/proconnect-gouv/proconnect-identite/pull/1921)

### Autres changements
- Mise à jour de la documentation et des configurations.
- Corrections mineures et améliorations de la qualité du code.
