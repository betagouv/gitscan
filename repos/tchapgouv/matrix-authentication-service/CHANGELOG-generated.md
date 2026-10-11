## Changelog : matrix-authentication-service (30 derniers jours, au 09 octobre 2026)

### Résumé
Les dernières semaines ont été marquées par les passages aux versions 1.24.0 et 1.25.1. L'accent a été mis sur l'amélioration de l'expérience utilisateur via des messages d'erreur plus explicites et une meilleure gestion des comptes (réactivation et récupération), tout en renforçant la qualité du code et la robustesse des processus de déploiement.

### Évolutions fonctionnelles
- **Gestion des comptes** : 
    - Possibilité de réactiver un compte si les permissions le permettent ([#151](https://github.com/tchapgouv/matrix-authentication-service/issues/151)).
    - Autorisation de lancer une procédure de récupération de compte même si l'utilisateur est déjà connecté ([#145](https://github.com/tchapgouv/matrix-authentication-service/issues/145)).
- **Expérience utilisateur et messages d'erreur** :
    - Amélioration de la précision des messages d'erreur lors de la connexion ou de la réinitialisation de mot de passe (mauvais serveur, compte désactivé, ou aide via `login_hint`) ([#144](https://github.com/tchapgouv/matrix-authentication-service/issues/144), [#146](https://github.com/tchapgouv/matrix-authentication-service/issues/146), [#154](https://github.com/tchapgouv/matrix-authentication-service/issues/154)).
    - Mise à jour des libellés sur les interfaces de connexion, de récupération et d'inscription ([#149](https://github.com/tchapgouv/matrix-authentication-service/issues/149), [#150](https://github.com/tchapgouv/matrix-authentication-service/issues/150)).
- **Corrections de bugs** :
    - Résolution de problèmes d'affichage du composant CAPTCHA sur la page d'inscription ([#5992](https://github.com/tchapgouv/matrix-authentication-service/issues/5992)).

### Évolutions techniques
- **Versions et déploiement** :
    - Mise à jour majeure vers les versions 1.24.0 et 1.25.1.
    - Refonte du workflow de build (`build.yaml`) et ajout de configurations pour les workers.
    - Amélioration des tests de templates pour valider la configuration du CAPTCHA.
- **Qualité du code** :
    - Nettoyage et correction des avertissements (Clippy et variables inutilisées) pour améliorer la maintenabilité du code.

### Autres changements
- **Documentation** : Mise à jour des fichiers `MODIFICATIONS.md` pour les versions 1.24.0 et 1.25.1 (incluant la documentation de la fonctionnalité `end_session`).
- **Internationalisation** : Plusieurs mises à jour des fichiers de traduction.
- **Maintenance** : Opérations de nettoyage général du code ([#147](https://github.com/tchapgouv/matrix-authentication-service/issues/147)).
