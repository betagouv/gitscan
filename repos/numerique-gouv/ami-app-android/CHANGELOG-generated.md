## Changelog : ami-app-android (30 derniers jours, au 08 septembre 2026)

### Résumé
Cette période a été marquée par une montée en puissance de la sécurité et de la robustesse de l'application. L'introduction des Passkeys et la création d'un environnement de pré-production préparent l'application à des usages plus modernes et à des cycles de déploiement plus rigoureux, tandis que l'automatisation des configurations de build améliore la fiabilité du développement.

### Évolutions fonctionnelles
- Support des Passkeys dans les WebViews pour permettre une authentification plus moderne et sécurisée [#86](https://github.com/numerique-gouv/ami-app-android/pull/86).
- Amélioration de la gestion des notifications push sur Android [#94](https://github.com/numerique-gouv/ami-app-android/pull/94).

### Évolutions techniques
- **Sécurité & Compatibilité** : Augmentation du SDK minimum à la version 28 pour permettre l'usage des technologies de Passkeys [#83](https://github.com/numerique-gouv/ami-app-android/pull/84).
- **Gestion des environnements** : Mise en place d'un environnement de pré-production (PreProd) avec sa propre configuration Firebase dédiée [#85](https://github.com/numerique-gouv/ami-app-android/pull/87).
- **Automatisation du Build** : Génération dynamique des fichiers de configuration (`BuildConfig` et `network_security_config.xml`) à partir de variables d'environnement pour sécuriser les paramètres sensibles et faciliter les déploiements.
- **Optimisation des performances** : Passage en mode asynchrone de la récupération de l'identifiant de l'appareil (`deviceId`) pour éviter tout blocage de l'interface [#79](https://github.com/numerique-gouv/ami-app-android/pull/79).
- **Maintenance Firebase** : Correction du contexte du service Firebase et renommage du jeton de notification en `fcmToken` pour plus de clarté.
- **Déploiement** : Optimisation de la gestion des clés de signature (`keystore`) pour les processus de publication sur le Play Store.

### Autres changements
- Nettoyage général du code source (campagne "nettoyage de printemps") [#81](https://github.com/numerique-gouv/ami-app-android/pull/82).
- Amélioration de la documentation de configuration avec l'ajout de fichiers d'exemple pour les variables d'environnement (`.env.example`).
