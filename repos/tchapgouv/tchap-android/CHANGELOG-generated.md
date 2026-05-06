## Changelog : tchap-android (30 derniers jours, au 4 mai 2026)

### Résumé
Cette version apporte des améliorations de sécurité, notamment la vérification des appareils avec les builds nightly d'Element X et la correction d'un problème lié à la réinitialisation des clés de chiffrement. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été implémentées, notamment concernant la réinitialisation de l'identité et la gestion des erreurs de stockage des secrets.

### Évolutions fonctionnelles
- **Vérification des appareils :** Ajout de la prise en charge de la vérification des appareils avec les builds nightly d'Element X, améliorant ainsi la sécurité de la communication. [#9137](https://github.com/tchapgouv/tchap-android/pull/9137)
- **Réinitialisation de l'identité :** Correction d'un bug empêchant la réinitialisation correcte de l'identité, incluant la cross-signature et la clé de récupération. [#1199](https://github.com/tchapgouv/tchap-android/pull/1199)
- **Réinitialisation de tout :** Correction d'une erreur "Cannot find secrets in storage" lors de la réinitialisation complète de l'application. [#1206](https://github.com/tchapgouv/tchap-android/pull/1206)
- **Réactivation de la bannière de vérification d'appareil :** La bannière de vérification d'appareil est de nouveau affichée pour une meilleure sécurité. [#3aa4b16069](https://github.com/tchapgouv/tchap-android/commit/3aa4b16069)

### Évolutions techniques
- **Mise à jour de la base de code :** Intégration des dernières modifications d'Element Android 1.6.58 et 1.6.54. [#1207](https://github.com/tchapgouv/tchap-android/pull/1207), [#1203](https://github.com/tchapgouv/tchap-android/pull/1203)
- **Gestion des exceptions de sécurité :** Ajout d'une exception de sécurité pour OpenMapTiles. [#42a823b63b](https://github.com/tchapgouv/tchap-android/commit/42a823b63b)
- **Correction de bugs et amélioration de la qualité du code :** Plusieurs corrections de lint et de bugs mineurs ont été apportées pour améliorer la qualité du code. [#1205](https://github.com/tchapgouv/tchap-android/pull/1205), [#1204](https://github.com/tchapgouv/tchap-android/pull/1204)
- **Exportation de la version des clés de salle :** Exportation de la version des clés de salle pour une meilleure gestion. [#389bbd8d28](https://github.com/tchapgouv/tchap-android/commit/389bbd8d28)
- **Correction de la gestion du stockage des secrets :** Correction d'un bug lié à la gestion du stockage des secrets lors de la réinitialisation. [#9128](https://github.com/tchapgouv/tchap-android/pull/9128)

### Autres changements
- **Documentation :** Ajout de changelogs pour les différentes modifications.
- **Mise à jour des wordings :** Mise à jour de certains textes dans l'application pour une meilleure clarté.
