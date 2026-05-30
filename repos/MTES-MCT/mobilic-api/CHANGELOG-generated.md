## Changelog : mobilic-api (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité de l'application avec l'ajout de l'authentification à deux facteurs (TOTP), ainsi que sur l'amélioration des outils d'administration et de support. Des corrections et des améliorations ont également été apportées à l'interface administrateur, notamment au tableau de bord et à la gestion des contrôles.

### Évolutions fonctionnelles
- **Authentification:** Ajout de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée. Cela inclut la configuration, la vérification et l'intégration dans le processus de connexion. [#685](https://github.com/MTES-MCT/mobilic-api/pull/685)
- **Administration:** Refonte de la page d'accueil de l'administration avec de nouveaux indicateurs et informations. [#698](https://github.com/MTES-MCT/mobilic-api/pull/698)
- **Administration:** Ajout d'un indicateur pour signaler les jours de multi-employeur sur les alertes réglementaires. [#703](https://github.com/MTES-MCT/mobilic-api/pull/703)
- **Administration:** Exposition d'un indicateur `hasAnyMissionThisWeek` sur le résumé du tableau de bord. [#703](https://github.com/MTES-MCT/mobilic-api/pull/703)
- **Contrôles:** Ajout de l'information `isCTT` aux informations utilisateur du contrôleur. [#700](https://github.com/MTES-MCT/mobilic-api/pull/700)
- **Support Admin:** Ajout de fonctionnalités pour le support administrateur, incluant la possibilité d'impersonner des utilisateurs. [#685](https://github.com/MTES-MCT/mobilic-api/pull/685)
- **Notifications:** Mise en place de rappels par email pour l'activation du compte. [#697](https://github.com/MTES-MCT/mobilic-api/pull/697)

### Évolutions techniques
- **Sécurité:** Implémentation d'un audit pour l'impersonation d'utilisateurs, incluant la journalisation des actions et la protection contre l'impersonation de soi-même ou d'administrateurs.
- **Sécurité:** Ajout de tests de sécurité pour détecter les failles potentielles, notamment les IDOR (Insecure Direct Object Reference).
- **Architecture:** Refactorisation de la logique d'impersonation pour utiliser un JWT claim `impersonate_as` au lieu d'un cookie `admin_token`.
- **Base de données:** Ajout d'une table `support_action_log` pour stocker les informations relatives à l'impersonation.
- **Emails:** Déduplication des requêtes pour les emails de rappel d'activation. [#697](https://github.com/MTES-MCT/mobilic-api/pull/697)
- **Migrations:** Correction de l'ordre des révisions de migrations. [#700](https://github.com/MTES-MCT/mobilic-api/pull/700)
- **Code:** Centralisation d'une fonction dans le module de contrôle pour éviter la duplication de code. [#700](https://github.com/MTES-MCT/mobilic-api/pull/700)
- **Code:** Correction de code smells détectés par SonarLint dans le module d'impersonation.

### Autres changements
- **Documentation:** Amélioration de la documentation pour supporter l'utilisateur super-admin.
- **RGPD:** Ajout d'une purge RGPD pour la table `support_action_log`.
- **Corrections:** Correction d'un problème de désynchronisation du nom de l'offre dans Brevo. [#696](https://github.com/MTES-MCT/mobilic-api/pull/696)
- **Exports:** Correction d'une erreur de transaction imbriquée lors de l'export des données CGU. [#702](https://github.com/MTES-MCT/mobilic-api/pull/702)
