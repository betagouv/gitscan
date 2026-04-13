## Changelog : matrix-authentication-service (30 derniers jours, au 13 avril 2026)

### Résumé
Ce service d'authentification Matrix a bénéficié d'améliorations récentes axées sur la compatibilité avec différents clients (notamment Windows), la gestion des comptes utilisateurs et la sécurité des cookies. Des ajustements ont également été apportés au pipeline d'intégration continue (CI) pour optimiser le processus de construction.

### Évolutions fonctionnelles
- Correction d'un problème affectant l'URI pour le client de bureau Windows, améliorant ainsi la compatibilité. [#107](https://github.com/tchapgouv/matrix-authentication-service/issues/107)
- Réactivation silencieuse des comptes lors de l'inscription ou de la connexion via OIDC. [#114](https://github.com/tchapgouv/matrix-authentication-service/issues/114)
- Suppression du `matrix_id` du sujet des emails. [#106](https://github.com/tchapgouv/matrix-authentication-service/issues/106)

### Évolutions techniques
- Modification de la politique `SameSite` des cookies pour autoriser leur utilisation dans des iframes, améliorant ainsi l'intégration avec d'autres applications web. [#111](https://github.com/tchapgouv/matrix-authentication-service/issues/111)
- Activation exclusive de la construction Docker dans le pipeline CI, optimisant ainsi le processus de build. [#112](https://github.com/tchapgouv/matrix-authentication-service/issues/112)
- Rétractation de la modification du support email avec numerique.gouv. [#115](https://github.com/tchapgouv/matrix-authentication-service/issues/115)
