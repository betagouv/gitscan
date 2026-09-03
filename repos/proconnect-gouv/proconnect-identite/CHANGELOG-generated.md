## Changelog : proconnect-identite (30 derniers jours, au 02 septembre 2026)

### Résumé
Ce mois-ci, ProConnect Identité a franchi une étape importante dans la modernisation de son architecture et a renforcé l'autonomie des utilisateurs. Les évolutions majeures incluent une meilleure assistance pour la double authentification (MFA), une gestion simplifiée des connexions FranceConnect et une migration technique profonde vers un nouveau modèle de composants ("connectors").

### Évolutions fonctionnelles
- **Autonomie de l'utilisateur** : Possibilité de déconnecter l'identité FranceConnect depuis les informations personnelles ([#2062](https://github.com/proconnect-gouv/proconnect-identite/issues/2062)).
- **Amélioration de la sécurité (MFA & Passkeys)** :
    - Ajout d'un assistant MFA (MFA helper) dans les sections "Compte" et "Connexion" pour faciliter la gestion de la double authentification ([#2044](https://github.com/proconnect-gouv/proconnect-identite/issues/2044)).
    - Optimisation de l'expérience Passkey avec un déclenchement automatique lorsque la clé est déjà configurée ([#2080](https://github.com/proconnect-gouv/proconnect-identite/issues/2080)).
    - Mise en place d'un nouveau modèle d'e-mail dédié pour les codes OTP.
- **Notifications et communication** :
    - Envoi automatique d'un e-mail en cas d'annulation d'une demande de modération ([#2079](https://github.com/proconnect-gouv/proconnect-identite/issues/2079)).
    - Enrichissement des e-mails d'échec de jonction d'organisation avec le SIRET et le libellé pour une meilleure identification ([#2073](https://github.com/proconnect-gouv/proconnect-identite/issues/2073)).
- **Interface utilisateur** : Corrections de fautes de frappe et suppression de liens d'aide en doublon.

### Évolutions techniques
- **Refonte de l'architecture** : Migration massive de plusieurs services clés (authentification, modération, gestion des utilisateurs, des organisations et client OIDC) vers un nouveau modèle de "connectors" ([#2094](https://github.com/proconnect-gouv/proconnect-identite/issues/2094), [#2095](https://github.com/proconnect-gouv/proconnect-identite/issues/2095), [#2096](https://github.com/proconnect-gouv/proconnect-identite/issues/2096), [#2097](https://github.com/proconnect-gouv/proconnect-identite/issues/2097), [#2089](https://github.com/proconnect-gouv/proconnect-identite/issues/2089), [#2090](https://github.com/proconnect-gouv/proconnect-identite/issues/2090), [#2093](https://github.com/proconnect-gouv/proconnect-identite/issues/2093)).
- **Gestion des données** : Remplacement des appels à l'Annuaire des Entreprises par une synchronisation directe via Grist pour la récupération des listes SIREN et des administrations ([#2078](https://github.com/proconnect-gouv/proconnect-identite/issues/2078)).
- **Performance et Tests** :
    - Optimisation du temps de réinitialisation de la base de données lors des tests CI.
    - Standardisation des commandes de tests E2E.
- **Nettoyage** : Suppression de l'implémentation legacy `is_service_public` et refactoring des vues de configuration MFA.

### Autres changements
- **Maintenance** : Suppression de la variable d'environnement obsolète `ZAMMAD_TOKEN` ([#2085](https://github.com/proconnect-gouv/proconnect-identite/issues/2085)).
