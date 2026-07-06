## Changelog : proconnect-identite (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se sont concentrées sur l'amélioration de la sécurité, de la performance et de l'expérience utilisateur. Des restrictions ont été ajoutées aux méthodes d'authentification, des optimisations de base de données ont été réalisées et des corrections ont été apportées pour prévenir les abus liés à la vérification par email. De plus, la compatibilité avec PostgreSQL 17 a été assurée et de nouvelles catégories juridiques ont été ajoutées.

### Évolutions fonctionnelles
- Correction d'un problème empêchant de sélectionner une organisation après un échec de certification. [#1974](https://github.com/proconnect-gouv/proconnect-identite/issues/1974)
- Ajout de la catégorie juridique "Pôle d'équilibre territorial et rural". [#1982](https://github.com/proconnect-gouv/proconnect-identite/issues/1982)
- Prévention de l'envoi répétitif de codes de vérification par email pour limiter les abus. [#2004](https://github.com/proconnect-gouv/proconnect-identite/issues/2004)
- Mise à jour des valeurs AMR (Authentification Method Reference) pour utiliser des valeurs standard, notamment pour l'authentification TOTP. [#2012](https://github.com/proconnect-gouv/proconnect-identite/issues/2012)
- Restriction des méthodes d'authentification autorisées au niveau du endpoint de token. [#2003](https://github.com/proconnect-gouv/proconnect-identite/issues/2003)

### Évolutions techniques
- Optimisation de la performance en ajoutant un index sur les tables `users_oidc_clients`. [#1989](https://github.com/proconnect-gouv/proconnect-identite/issues/1989)
- Mise à jour de la compatibilité avec PostgreSQL 17. [#1983](https://github.com/proconnect-gouv/proconnect-identite/issues/1983)
- Mise à jour des dépendances : `ioredis`, `vite`, `nodemailer`, `qs`, `@cypress/request`, `undici`, `hono`, `tmp`, `form-data`, `actions/checkout`, `@electric-sql/pglite`, `proconnect-gouv/proconnect-test-client`, `concurrently`.
- Amélioration de la gestion des nouveaux niveaux ACR (Action Credential Request).
- Intégration d'un authentificateur pour Metabase. [#1967](https://github.com/proconnect-gouv/proconnect-identite/issues/1967)

### Autres changements
- Correction d'un bug dans l'annuaire du service public qui incluait les adresses email falsy dans les résultats. [#1996](https://github.com/proconnect-gouv/proconnect-identite/issues/1996)
- Modification du type d'un paramètre dans `certification-dirigeant` pour plus de précision. [#1985](https://github.com/proconnect-gouv/proconnect-identite/issues/1985)
- Mise à jour de la configuration par défaut de `allow_editing` à `false` pour la modération. [#1981](https://github.com/proconnect-gouv/proconnect-identite/issues/1981)
- Rétrogradation d'une mise à jour de `@electric-sql/pglite` suite à un problème. [#1997](https://github.com/proconnect-gouv/proconnect-identite/issues/1997)
- Revert d'une modification permettant les scripts postinstall de Cypress.
