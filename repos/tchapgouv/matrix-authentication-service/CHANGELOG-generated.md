## Changelog : matrix-authentication-service (30 derniers jours, au 08/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur grâce à des messages d'erreur plus explicites et une interface corrigée. Le projet a également franchi une étape importante avec la mise à jour vers la version 1.22.0 et des optimisations de son processus de construction.

### Évolutions fonctionnelles
- **Amélioration de la gestion des erreurs** : les messages d'erreur sont désormais plus clairs, notamment en cas d'erreur de serveur [#136](https://github.com/tchapgouv/matrix-authentication-service/issues/136) ou lorsqu'un nom d'utilisateur est déjà utilisé [#142](https://github.com/tchapgouv/matrix-authentication-service/issues/142).
- **Modification de la logique utilisateur** : la réactivation automatique des utilisateurs a été supprimée [#142](https://github.com/tchapgouv/matrix-authentication-service/issues/142).
- **Interface utilisateur** : correction de la mise en page de la page de consentement [#140](https://github.com/tchapgouv/matrix-authentication-service/issues/140).

### Évolutions techniques
- **Mise à jour majeure** : passage à la version 1.22.0 [#138](https://github.com/tchapgouv/matrix-authentication-service/issues/138).
- **Optimisation du build** : création d'un fichier de build dédié pour améliorer le processus de construction.
- **Observabilité** : mise à jour de l'intégration Sentry pour utiliser la nouvelle API d'options.
- **Qualité et tests** : corrections apportées via clippy et ajustement de la suite de tests (désactivation des tests ESS).

### Autres changements
- **Identité visuelle** : ajout d'un favicon [#141](https://github.com/tchapgouv/matrix-authentication-service/issues/141).
