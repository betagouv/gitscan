## Changelog : proconnect-identite (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la robustesse de la plateforme, notamment en préparant la migration des emails vers un nouveau système et en renforçant la gestion des erreurs. Des ajustements ont également été apportés pour supporter la pré-production et améliorer l'expérience utilisateur lors des rejets de certification.

### Évolutions fonctionnelles
- Amélioration du message d'erreur affiché aux utilisateurs en cas de rejet de certification, avec un conseil de vérifier leur boîte email. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pull/1927)
- Ajout d'une description d'erreur OIDC pour une meilleure information lors de l'authentification avec PCF. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- Début de la migration des emails de MonComptePro vers un nouveau système, avec ajout du nom de l'expéditeur pour une meilleure identification. [#1930](https://github.com/proconnect-gouv/proconnect-identite/pull/1930)

### Évolutions techniques
- Création d'un client dédié pour l'environnement de pré-production de la fédération, incluant la mise à jour des identifiants et secrets correspondants. [#1937](https://github.com/proconnect-gouv/proconnect-identite/pull/1937), [#1938](https://github.com/proconnect-gouv/proconnect-identite/pull/1938), [#1939](https://github.com/proconnect-gouv/proconnect-identite/pull/1939)
- Refactorisation de la logique de seed de la base de données pour les tests end-to-end, utilisant un hook `before` pour une meilleure gestion. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- Rétrogradation de la version de Node dans les conteneurs Docker suite à des problèmes rencontrés avec la version 26. [#1925](https://github.com/proconnect-gouv/proconnect-identite/pull/1925)

### Autres changements
- Mise à jour de plusieurs dépendances : `brace-expansion`, `systeminformation`, `prettier`, `hono`, `redis`, `cypress-io/github-action`, `actions/labeler`, `lodash`, `sentry`.
- Correction d'un script d'update des annuaires. [#1941](https://github.com/proconnect-gouv/proconnect-identite/pull/1941)
