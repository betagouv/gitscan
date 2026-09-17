## Changelog : matrix-authentication-service (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes évolutions améliorent la clarté des interactions lors des processus d'authentification (connexion, inscription, récupération de compte) grâce à des messages d'erreur plus précis et une interface utilisateur affinée. Le projet a également bénéficié d'une mise à jour majeure vers la version 1.22.0.

### Évolutions fonctionnelles
- **Amélioration des retours utilisateurs** : ajout de messages d'erreur explicites en cas de mauvais serveur lors de la connexion ou de la réinitialisation de mot de passe [#144](https://github.com/tchapgouv/matrix-authentication-service/issues/144), de compte désactivé [#146](https://github.com/tchapgouv/matrix-authentication-service/issues/146), ou d'utilisateur déjà existant [#142](https://github.com/tchapgouv/matrix-authentication-service/issues/142).
- **Optimisation des parcours d'authentification** : possibilité de lancer une procédure de récupération de compte même en étant déjà connecté [#145](https://github.com/tchapgouv/matrix-authentication-service/issues/145) et suppression de la réactivation automatique des utilisateurs lors d'une tentative d'inscription avec un nom d'utilisateur déjà pris [#142](https://github.com/tchapgouv/matrix-authentication-service/issues/142).
- **Interface utilisateur (UI)** : mise à jour des libellés pour les pages de connexion, de récupération et d'inscription [#149](https://github.com/tchapgouv/matrix-authentication-service/issues/149), correction de la mise en page de la page de consentement [#140](https://github.com/tchapgouv/matrix-authentication-service/issues/140) et ajout d'un favicon [#141](https://github.com/tchapgouv/matrix-authentication-service/issues/141).

### Évolutions techniques
- **Mise à jour majeure** : passage à la version 1.22.0 [#138](https://github.com/tchapgouv/matrix-authentication-service/issues/138).
- **Maintenance et infrastructure** : création d'un fichier de build dédié, mise à jour du transport Sentry (nouvelle API d'options) et corrections de code via Clippy.

### Autres changements
- Nettoyage général du code [#147](https://github.com/tchapgouv/matrix-authentication-service/issues/147).
