## Changelog : ami-app-android (30 derniers jours, au 9 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment une meilleure gestion de l'authentification FranceConnect et l'ouverture directe de l'application sur la page de notifications lors de la réception d'une notification push. Des améliorations techniques ont également été apportées pour faciliter le développement et le débogage. L'application commence également à adopter le Design System FR (DSFR).

### Évolutions fonctionnelles
- **Authentification FranceConnect :** L'écran de FranceConnect est maintenant mis en avant pour une meilleure expérience utilisateur [#38](https://github.com/numerique-gouv/ami-app-android/pull/38).
- **Notifications :** L'application ouvre désormais directement la page des notifications lorsqu'un utilisateur clique sur une notification push [#39](https://github.com/numerique-gouv/ami-app-android/issues/39).
- **Gestion de l'authentification :** Le token d'authentification est maintenant effacé en cas d'échec d'authentification, améliorant ainsi la sécurité et la robustesse de l'application.
- **Correction d'un bug :** Correction d'un problème lié à l'URL de connexion FranceConnect [#50f8dac](https://github.com/numerique-gouv/ami-app-android/commit/50f8dac).

### Évolutions techniques
- **DSFR :** Intégration des couleurs, polices et icônes du Design System FR (DSFR) pour une cohérence visuelle accrue et une meilleure maintenabilité.
- **Débogage :** Désactivation de la vérification SSL en mode DEBUG pour simplifier le développement et le débogage [#ea84e1a](https://github.com/numerique-gouv/ami-app-android/commit/ea84e1a).
- **Configuration de l'API :** Mise à jour de l'URL de l'API Retrofit pour permettre l'utilisation d'une URL d'application de revue spécifique [#29](https://github.com/numerique-gouv/ami-app-android/pull/29).

### Autres changements
- Correction d'une réversion de suppression sur l'écran WebView.
- Amélioration de la gestion des revues de code.
