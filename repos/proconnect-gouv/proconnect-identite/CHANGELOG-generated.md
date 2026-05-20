## Changelog : proconnect-identite (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur en cas d'erreur OIDC, la migration progressive des envois d'emails depuis MonComptePro, et la clarification des motifs de rejet lors des demandes de certification. Des optimisations techniques et des mises à jour de dépendances ont également été réalisées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Amélioration des messages d'erreur OIDC : une description d'erreur plus détaillée est maintenant transmise à ProConnect Federation (PCF) pour une meilleure compréhension des problèmes d'authentification. [#1914](https://github.com/proconnect-gouv/proconnect-identite/pulls/1914)
- Clarification du motif de rejet : le motif de rejet d'une demande de certification a été remplacé par un message invitant l'utilisateur à consulter son email pour plus d'informations. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pulls/1927)
- Migration des emails : début de la migration des envois d'emails depuis MonComptePro, avec l'ajout du nom de l'expéditeur. [#1930](https://github.com/proconnect-gouv/proconnect-identite/pulls/1930)

### Évolutions techniques
- Refactoring des tests E2E : Utilisation de "before hook" pour initialiser la base de données avant la plupart des tests E2E, améliorant ainsi leur fiabilité et leur performance. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pulls/1926)
- Optimisation des dépendances : Mise à jour de plusieurs dépendances, incluant `redis`, `hono`, `prettier`, `systeminformation`, `brace-expansion`, `lodash`, `cypress-io/github-action` et `actions/labeler`.
- Rétrogradation de la version de Node : Rétrogradation de la version de Node de 26-slim à 24-slim suite à des problèmes rencontrés. [#1925](https://github.com/proconnect-gouv/proconnect-identite/pulls/1925)

### Autres changements
- Documentation : Mise à jour de la vue `certification-dirigeant/close-match-error.ejs`.
- Maintenance : Suppression d'une dépendance obsolète (`dotenvx`).
- CI/CD : Mise à jour de la configuration du workflow CI/CD.
