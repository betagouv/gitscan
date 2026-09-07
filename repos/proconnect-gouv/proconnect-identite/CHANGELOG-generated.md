## Changelog : proconnect-identite (30 derniers jours, au 04/09/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'autonomie des utilisateurs, notamment via la possibilité de déconnecter une identité FranceConnect, et sur l'amélioration de l'expérience de sécurité (Passkeys). En parallèle, le projet a entamé une modernisation importante de son architecture interne pour gagner en robustesse et en maintenabilité.

### Évolutions fonctionnelles
- **Autonomie utilisateur** : possibilité de déconnecter son identité FranceConnect ([#2062](https://github.com/proconnect-gouv/proconnect-identite/issues/2062)).
- **Expérience de sécurité** : déclenchement automatique de la Passkey si elle est déjà configurée, évitant un clic supplémentaire ([#2080](https://github.com/proconnect-gouv/proconnect-identite/issues/2080)).
- **Amélioration des communications** : 
    - Notification par email lorsqu'une demande de modération est annulée ([#2079](https://github.com/proconnect-gouv/proconnect-identite/issues/2079)).
    - Enrichissement des emails d'erreur lors de l'impossibilité de rejoindre une organisation (ajout du SIRET et du libellé) ([#2073](https://github.com/proconnect-gouv/proconnect-identite/issues/2073)).
- **Interface et corrections** : 
    - Uniformisation du format de la date de dernière mise à jour FranceConnect ([#2121](https://github.com/proconnect-gouv/proconnect-identite/issues/2121)).
    - Corrections de fautes de frappe et suppression de liens d'aide en doublon.

### Évolutions techniques
- **Refactorisation majeure (Architecture Connecteurs)** : migration massive de plusieurs modules (authentification, modération, client OIDC, gestion des utilisateurs et des organisations) vers une nouvelle architecture basée sur des connecteurs pour centraliser la logique ([#2089](https://github.com/proconnect-gouv/proconnect-identite/issues/2089), [#2090](https://github.com/proconnect-gouv/proconnect-identite/issues/2090), [#2094](https://github.com/proconnect-gouv/proconnect-identite/issues/2094), [#2095](https://github.com/proconnect-gouv/proconnect-identite/issues/2095), [#2096](https://github.com/proconnect-gouv/proconnect-identite/issues/2096), [#2097](https://github.com/proconnect-gouv/proconnect-identite/issues/2097)).
- **Migration des sources de données** : les listes SIREN et la liste des administrations sont désormais récupérées directement via Grist ([#2078](https://github.com/proconnect-gouv/proconnect-identite/issues/2078)).
- **Optimisations et nettoyage** :
    - Optimisation de la réinitialisation de la base de données lors des tests CI pour accélérer les déploiements.
    - Refactorisation des vues de configuration MFA pour réduire la duplication de code ([#2076](https://github.com/proconnect-gouv/proconnect-identite/issues/2076)).
    - Suppression de l'implémentation héritée `is_service_public` et de variables d'environnement inutilisées.
