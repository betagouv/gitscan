## Changelog : proconnect-identite (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de l'expérience utilisateur, notamment avec la refonte de l'interface utilisateur pour l'authentification multi-facteurs (MFA) et la restriction des méthodes d'authentification au niveau du token. Des corrections ont également été apportées pour éviter le spam des codes de vérification par email et pour améliorer la gestion des données de l'annuaire public.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):** Nouvelle interface utilisateur pour le choix du MFA, améliorant l'expérience utilisateur. [#2025](https://github.com/proconnect-gouv/proconnect-identite/pull/2025)
- **Vérification Email:** Limitation du nombre de tentatives d'envoi de codes de vérification par email pour prévenir le spam. [#2004](https://github.com/proconnect-gouv/proconnect-identite/pull/2004)
- **AMR (Authentication Method Reference):** Mise à jour des valeurs AMR pour utiliser des valeurs standard, notamment pour le TOTP. [#2012](https://github.com/proconnect-gouv/proconnect-identite/pull/2012)
- **Niveaux ACR (Authentication Context Class):** Ajout de nouveaux niveaux ACR. [#1965](https://github.com/proconnect-gouv/proconnect-identite/pull/1965)
- **Annuaire Service Public:** Correction pour exclure les adresses email non valides des résultats de l'annuaire. [#1996](https://github.com/proconnect-gouv/proconnect-identite/pull/1996)

### Évolutions techniques
- **Sécurité:** Restriction des méthodes d'authentification autorisées pour l'obtention des tokens. [#2003](https://github.com/proconnect-gouv/proconnect-identite/pull/2003)
- **Tests E2E:** Mock de l'API api-lannuaire.service-public.fr pour les tests end-to-end, permettant des tests plus fiables et isolés. [#2029](https://github.com/proconnect-gouv/proconnect-identite/pull/2029)
- **Publication du package email:** Le package `@proconnect-gouv/proconnect.email` a été rendu publiable en tant que module standalone. [#2017](https://github.com/proconnect-gouv/proconnect-identite/pull/2017)
- **Suppression de Crisp:** Suppression du widget de chat Crisp. [#2014](https://github.com/proconnect-gouv/proconnect-identite/pull/2014)

### Autres changements
- **Documentation:** Mise à jour de la page FranceConnect. [#2013](https://github.com/proconnect-gouv/proconnect-identite/pull/2013)
- **Corrections diverses:** Correction d'une erreur dans la logique de vérification du `given_name`. [#2015](https://github.com/proconnect-gouv/proconnect-identite/pull/2015)
- **Mises à jour de dépendances:** Mises à jour de plusieurs dépendances (nodemailer, undici, form-data, actions/checkout, etc.).
