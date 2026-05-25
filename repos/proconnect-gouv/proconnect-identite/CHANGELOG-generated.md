## Changelog : proconnect-identite (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se concentrent sur la préparation de l'environnement de pré-production, l'amélioration de la gestion des erreurs et la migration progressive des envois d'emails depuis MonComptePro. Des corrections et des ajustements ont également été apportés pour améliorer la qualité et la fiabilité du service.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs OIDC : Ajout d'une description d'erreur OIDC envoyée à PCF pour faciliter le diagnostic des problèmes [#1914](https://github.com/proconnect-gouv/proconnect-identite/pulls/1914).
- Modification du message de rejet de certification dirigeant : Le motif de rejet a été remplacé par un message invitant l'utilisateur à consulter son email pour plus d'informations [#1927](https://github.com/proconnect-gouv/proconnect-identite/pulls/1927).
- Préparation de la migration des emails : Début de la migration des envois d'emails depuis MonComptePro, avec ajout du nom de l'expéditeur pour une meilleure identification [#1930](https://github.com/proconnect-gouv/proconnect-identite/pulls/1930).

### Évolutions techniques
- Création d'un client dédié pour l'environnement de pré-production de la fédération : Mise en place d'un client spécifique pour l'environnement de pré-production, incluant la mise à jour des identifiants et secrets correspondants [#1937](https://github.com/proconnect-gouv/proconnect-identite/pulls/1937), [#1938](https://github.com/proconnect-gouv/proconnect-identite/pulls/1938), [#1939](https://github.com/proconnect-gouv/proconnect-identite/pulls/1939).
- Refactoring des tests E2E : Utilisation d'un hook `before` pour initialiser la base de données dans la majorité des tests E2E, améliorant ainsi la performance et la fiabilité des tests [#1926](https://github.com/proconnect-gouv/proconnect-identite/pulls/1926).
- Mise à jour de l'image Node : Tentative de mise à jour de l'image Node vers la version 26-slim (revertée suite à des problèmes) [#1921](https://github.com/proconnect-gouv/proconnect-identite/pulls/1921), [#1925](https://github.com/proconnect-gouv/proconnect-identite/pulls/1925).

### Autres changements
- Mise à jour de plusieurs dépendances : Redis, Cypress, Prettier, Systeminformation, Brace-expansion, Hono, Lodash, Sentry. Ces mises à jour visent à améliorer la sécurité et la stabilité du projet.
- Correction du script de mise à jour des annuaires : Correction d'un problème lié à l'utilisation des nouveaux fichiers dans le script de mise à jour des annuaires [#1941](https://github.com/proconnect-gouv/proconnect-identite/pulls/1941), [#1939](https://github.com/proconnect-gouv/proconnect-identite/pulls/1939).
