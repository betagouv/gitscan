## Changelog : proconnect-identite (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la modernisation de l'interface utilisateur pour l'authentification multi-facteurs (MFA), et la maintenance technique du projet, notamment la suppression de fonctionnalités obsolètes et la mise à jour des dépendances. Des améliorations ont également été apportées à la gestion des données et aux tests.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):** Nouvelle interface utilisateur pour le choix du MFA, améliorant l'expérience utilisateur. [#2025](https://github.com/proconnect-gouv/proconnect-identite/pulls/2025)
- **Email de vérification:** Clarification du libellé des emails de vérification pour une meilleure compréhension des utilisateurs. [#2056](https://github.com/proconnect-gouv/proconnect-identite/issues/2056) et [#2045](https://github.com/proconnect-gouv/proconnect-identite/issues/2045)
- **Suppression du support des scopes `organizations`:** Le support des scopes `organizations` a été supprimé. [#2055](https://github.com/proconnect-gouv/proconnect-identite/pulls/2055)
- **Suppression de l'ancienne adresse email:** Suppression de la prise en charge de l'ancienne adresse email moncomptepro. [#2061](https://github.com/proconnect-gouv/proconnect-identite/pulls/2061)
- **Amélioration de l'algorithme de jointure commune:** Mise à jour de l'algorithme de jointure commune. [#2039](https://github.com/proconnect-gouv/proconnect-identite/pulls/2039)

### Évolutions techniques
- **Sécurité:** Suppression de `unsafe-inline` de la Content Security Policy pour renforcer la sécurité. [#2026](https://github.com/proconnect-gouv/proconnect-identite/pulls/2026)
- **Refactoring:** Refactorisation de la chaîne principale de garde (main guard). [#2059](https://github.com/proconnect-gouv/proconnect-identite/pulls/2059)
- **Tests:** Mock de l'API `api-lannuaire.service-public.fr` dans les tests end-to-end pour une meilleure isolation et fiabilité. [#2029](https://github.com/proconnect-gouv/proconnect-identite/pulls/2029)
- **Publication du package email:** Le package `@proconnect-gouv/proconnect.email` a été rendu publiable en tant que module autonome. [#2017](https://github.com/proconnect-gouv/proconnect-identite/pulls/2017)
- **Suppression de Crisp:** Suppression de la chatbox Crisp. [#2014](https://github.com/proconnect-gouv/proconnect-identite/pulls/2014)
- **Amélioration de la récursivité du `userSignInRequirementsGuard`:** Modification pour une gestion plus propre des exigences de connexion utilisateur. [#2057](https://github.com/proconnect-gouv/proconnect-identite/pulls/2057)

### Autres changements
- **Documentation:** Mise à jour de la définition AMR `mail`. [#2016](https://github.com/proconnect-gouv/proconnect-identite/pulls/2016)
- **Fixtures:** Synchronisation des fixtures de l'annuaire 50041 avec l'API réelle. [#2035](https://github.com/proconnect-gouv/proconnect-identite/pulls/2035)
- **Correction de données anonymisées:** Correction de la copie anonymisée de la table des authentificateurs. [#2027](https://github.com/proconnect-gouv/proconnect-identite/pulls/2027)
- **Correction d'une erreur de syntaxe:** Correction d'une erreur de syntaxe sur la page de vérification de l'email. [#2048](https://github.com/proconnect-gouv/proconnect-identite/pulls/2048)
- **Correction d'une typo:** Correction d'une faute de frappe dans le template d'email de vérification. [#2045](https://github.com/proconnect-gouv/proconnect-identite/issues/2045)
