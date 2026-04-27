## Changelog : ami-app-android (30 derniers jours, au 16 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment l'ajout d'un mécanisme de rafraîchissement par glissement vers le bas (swipe-to-refresh) sur plusieurs écrans, une meilleure gestion de l'authentification FranceConnect, et l'intégration de la nouvelle identité visuelle du gouvernement français (DSFR). Des corrections de couleurs et de polices ont également été apportées.

### Évolutions fonctionnelles
- **Rafraîchissement par glissement vers le bas:** Ajout de la fonctionnalité de rafraîchissement par glissement vers le bas sur l'écran de revue des applications et dans les webviews. [#49](https://github.com/numerique-gouv/ami-app-android/pull/49)
- **Amélioration de l'authentification FranceConnect:** Promotion de l'écran de FranceConnect pour une meilleure visibilité et un accès plus facile. [#38](https://github.com/numerique-gouv/ami-app-android/pull/38)
- **Notifications:** Ouverture de la page des notifications lors du clic sur une notification push. [#39](https://github.com/numerique-gouv/ami-app-android/issues/39)
- **Gestion de l'authentification:** Suppression du token d'authentification (bearer) en cas d'échec de l'authentification. [#95f918f](https://github.com/numerique-gouv/ami-app-android/commit/95f918f)

### Évolutions techniques
- **Intégration de la DSFR:**
    - Ajout des polices DSFR.
    - Ajout des couleurs DSFR.
    - Ajout des icônes DSFR.
- **Gestion du rafraîchissement:** Refactorisation de la gestion de l'état de rafraîchissement (isRefreshing) dans le ViewModel. [#7999862](https://github.com/numerique-gouv/ami-app-android/commit/7999862)
- **Sécurité (Debug):** Contournement de la vérification SSL en mode DEBUG pour faciliter le développement. [#ea84e1a](https://github.com/numerique-gouv/ami-app-android/commit/ea84e1a)

### Autres changements
- Correction des couleurs et des polices pour une meilleure cohérence visuelle. [#51927e8](https://github.com/numerique-gouv/ami-app-android/commit/51927e8)
- Ajout de l'icône infinity_line. [#65ffd98](https://github.com/numerique-gouv/ami-app-android/commit/65ffd98)
