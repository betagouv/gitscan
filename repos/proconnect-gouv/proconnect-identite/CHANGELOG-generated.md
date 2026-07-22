## Changelog : proconnect-identite (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la modernisation de l'interface utilisateur pour l'authentification multi-facteurs (MFA), et l'amélioration de la robustesse des tests d'intégration. Des ajustements ont également été apportés à la configuration et à la gestion des dépendances.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):** Nouvelle interface utilisateur pour le choix des méthodes MFA [#2025](https://github.com/proconnect-gouv/proconnect-identite/pulls/2025).
- **Annuaire:** Synchronisation des données de l'annuaire avec l'API réelle pour les tests d'intégration [#2035](https://github.com/proconnect-gouv/proconnect-identite/pulls/2035).
- **AMR (Authentication Method Reference):** Mise à jour de la définition de l'AMR "mail" et remplacement des valeurs TOTP non standard [#2016](https://github.com/proconnect-gouv/proconnect-identite/pulls/2016) et [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).
- **Sécurité:** Restriction des méthodes d'authentification au niveau du point d'accès au token [#2011](https://github.com/proconnect-gouv/proconnect-identite/pulls/2011).

### Évolutions techniques
- **Tests d'intégration:** Mock de l'API `api-lannuaire.service-public.fr` pour les tests e2e, avec vérification quotidienne de la cohérence des données mockées [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029).
- **Suppression de Crisp:** Suppression du widget de chat Crisp pour alléger l'application et améliorer la sécurité [#2014](https://github.com/proconnect-gouv/proconnect-identite/pulls/2014).
- **Publication du package email:** Préparation du package `@proconnect-gouv/proconnect.email` pour une publication autonome [#2017](https://github.com/proconnect-gouv/proconnect-identite/pulls/2017).
- **Sécurité CSP:** Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- **Correction d'anomalie:** Correction d'une copie anonymisée incorrecte de la table `authenticators` [#2027](https://github.com/proconnect-gouv/proconnect-identite/pulls/2027).
- **Correction de bug:** Correction d'un bug dans la vérification du `given_name` [#2015](https://github.com/proconnect-gouv/proconnect-identite/pulls/2015).

### Autres changements
- **Documentation:** Mise à jour de la page FranceConnect [#2013](https://github.com/proconnect-gouv/proconnect-identite/pulls/2013).
- **CI/CD:** Amélioration de la configuration des scripts postinstall pour Cypress [#2006](https://github.com/proconnect-gouv/proconnect-identite/pulls/2006).
- **Dépendances:** Mises à jour de plusieurs dépendances (nodemailer, ioredis, undici, hono, tmp, form-data, actions/checkout, qs, @cypress/request) et actions GitHub.
