## Changelog : proconnect-identite (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la modernisation de l'interface utilisateur pour l'authentification multi-facteurs (MFA) et l'amélioration de la robustesse des tests. Des corrections de bugs et des refactorings ont également été réalisés pour améliorer la qualité du code et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):** Nouvelle interface utilisateur pour le choix des méthodes MFA [#2025](https://github.com/proconnect-gouv/proconnect-identite/pulls/2025).
- **Vérification d'email:** Clarification du texte sur la page de vérification d'email [#2048](https://github.com/proconnect-gouv/proconnect-identite/pulls/2048) et correction d'une faute de frappe [#2045](https://github.com/proconnect-gouv/proconnect-identite/issues/2045).
- **Annuaire:** Synchronisation de la fixture de l'annuaire avec l'API réelle [#2035](https://github.com/proconnect-gouv/proconnect-identite/pulls/2035).
- **AMR (Authentication Method Reference):** Mise à jour de la définition AMR `mail` et remplacement des valeurs TOTP non standard [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).

### Évolutions techniques
- **Sécurité:** Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- **Tests:**
    - Mock de l'API `api-lannuaire.service-public.fr` pour les tests end-to-end [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029).
    - Vérification quotidienne de la cohérence des données mockées avec l'API réelle.
    - Correction d'une erreur dans la clé de correspondance pour la vérification de `given_name` [#2015](https://github.com/proconnect-gouv/proconnect-identite/issues/2015).
- **Refactoring:** Suppression du widget de chat Crisp [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012) et refactoring du code associé.
- **Packages:** Publication standalone du package `@proconnect-gouv/proconnect.email` [#2017](https://github.com/proconnect-gouv/proconnect-identite/pulls/2017).
- **Dépendances:** Mises à jour de plusieurs dépendances (nodemailer, ioredis, vite, axe-core, redis, sentry, actions/labeler, actions/setup-node, body-parser, morgan, systeminformation, @hono/node-server, hono, cypress-io/github-action).

### Autres changements
- Correction d'une copie anonymisée de la table `authenticators` [#2027](https://github.com/proconnect-gouv/proconnect-identite/pulls/2027).
- Revert d'une mise à jour de Vite qui causait des problèmes [#2024](https://github.com/proconnect-gouv/proconnect-identite/issues/2024).
- Suppression d'un commit accidentellement poussé sur `main` [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- Amélioration de la lisibilité du code (prettify) [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- Mise à jour des variables d'environnement par défaut pour les tests [#2011](https://github.com/proconnect-gouv/proconnect-identite/pulls/2011).
- Restriction des méthodes d'authentification au niveau de l'endpoint token [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).
