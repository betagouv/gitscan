## Changelog : proconnect-identite (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'expérience utilisateur de l'authentification multifacteur (MFA) et la maintenance technique. Des corrections ont été apportées pour empêcher l'envoi abusif de codes de vérification par email, et une nouvelle interface utilisateur pour le choix des méthodes MFA a été déployée. La suppression du widget de chat Crisp et la restriction des méthodes d'authentification au niveau du token renforcent la sécurité.

### Évolutions fonctionnelles
- **Authentification multifacteur (MFA):** Nouvelle interface utilisateur pour le choix des méthodes MFA [#2025](https://github.com/proconnect-gouv/proconnect-identite/pulls/2025).
- **Vérification d'email:** Limitation du nombre de tentatives d'envoi de codes de vérification par email pour prévenir les abus [#2004](https://github.com/proconnect-gouv/proconnect-identite/pulls/2004).
- **Annuaire API:** Synchronisation de la fixture de l'annuaire avec l'API réelle [#2035](https://github.com/proconnect-gouv/proconnect-identite/pulls/2035).
- **Tests E2E:** Mock de l'API api-lannuaire.service-public.fr pour les tests end-to-end [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029). Vérification quotidienne de la cohérence des données mockées avec l'API réelle.

### Évolutions techniques
- **Sécurité:** Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026).
- **Sécurité:** Restriction des méthodes d'authentification autorisées pour le endpoint token [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).
- **Refactoring:** Suppression du widget de chat Crisp [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).
- **Packaging:** Préparation du package `@proconnect-gouv/proconnect.email` pour une publication autonome [#2017](https://github.com/proconnect-gouv/proconnect-identite/pulls/2017).
- **Tests:** Amélioration de la configuration des tests Cypress avec l'utilisation de variables d'environnement par défaut de l'image `proconnect-test-client` [#2011](https://github.com/proconnect-gouv/proconnect-identite/pulls/2011).
- **AMR:** Utilisation de valeurs AMR standard pour les méthodes d'authentification [#2012](https://github.com/proconnect-gouv/proconnect-identite/pulls/2012).

### Autres changements
- Mise à jour de la page FranceConnect [#2013](https://github.com/proconnect-gouv/proconnect-identite/pulls/2013).
- Mise à jour de la définition AMR `mail` [#2016](https://github.com/proconnect-gouv/proconnect-identite/pulls/2016).
- Correction d'une erreur dans la logique de vérification du `given_name` [#2015](https://github.com/proconnect-gouv/proconnect-identite/pulls/2015).
