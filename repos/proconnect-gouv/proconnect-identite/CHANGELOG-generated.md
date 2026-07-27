## Changelog : proconnect-identite (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, l'expérience utilisateur de l'authentification multi-facteurs (MFA) et la maintenance technique du projet. Des corrections ont été apportées pour améliorer la robustesse et la conformité de la plateforme.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):** Nouvelle interface utilisateur pour le choix de la méthode MFA [#2025](https://github.com/proconnect-gouv/proconnect-identite/pulls/2025).
- **Vérification d'email:** Clarification du texte sur la page de vérification d'email [#2045](https://github.com/proconnect-gouv/proconnect-identite/issues/2045) et correction d'une erreur de syntaxe [#2048](https://github.com/proconnect-gouv/proconnect-identite/pulls/2048).
- **Annuaire:** Synchronisation des données de l'annuaire 50041 avec l'API réelle [#2035](https://github.com/proconnect-gouv/proconnect-identite/pulls/2035).
- **FranceConnect:** Mise à jour de la page FranceConnect [#2013](https://github.com/proconnect-gouv/proconnect-identite/pulls/2013).
- **AMR:** Mise à jour des valeurs AMR (Authentication Method Reference) pour utiliser des standards [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).

### Évolutions techniques
- **Sécurité:** Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- **Tests:** Mock de l'API `api-lannuaire.service-public.fr` dans les tests end-to-end (E2E) [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029) et vérification quotidienne de la cohérence des données mockées [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029).
- **Refactoring:** Suppression du widget de chat Crisp [#2014](https://github.com/proconnect-gouv/proconnect-identite/pulls/2014) et refactoring du code associé [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).
- **Packaging:** Préparation du package `@proconnect-gouv/proconnect.email` pour une publication autonome [#2017](https://github.com/proconnect-gouv/proconnect-identite/pulls/2017).
- **Authentification:** Restriction des méthodes d'authentification au niveau du endpoint token [#2003](https://github.com/proconnect-gouv/proconnect-identite/pulls/2003).
- **Corrections:** Correction d'un bug lié à la clé de correspondance pour la vérification du `given_name` [#2015](https://github.com/proconnect-gouv/proconnect-identite/pulls/2015).
- **Anonymisation:** Correction de la copie anonymisée de la table des authentificateurs [#2027](https://github.com/proconnect-gouv/proconnect-identite/pulls/2027).

### Autres changements
- Mise à jour de plusieurs dépendances : `morgan`, `@hono/node-server`, `hono`, `body-parser`, `systeminformation`, `actions/setup-node`, `actions/labeler`, `sentry`, `ioredis`, `nodemailer`, `axe-core`, `cypress-io/github-action` et `proconnect-gouv/proconnect-test-client`.
- Revert d'une mise à jour de `vite` [#2024](https://github.com/proconnect-gouv/proconnect-identite/issues/2024).
- Correction d'un revert accidentel sur la branche `main`.
- Amélioration de la lisibilité du code (prettify).
