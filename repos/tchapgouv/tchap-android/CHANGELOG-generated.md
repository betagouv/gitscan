## Changelog : tchap-android (30 derniers jours, au 29 avril 2026)

### Résumé
Cette mise à jour apporte des corrections importantes concernant la réinitialisation de l'identité (signatures croisées et clé de récupération) et la gestion des secrets, améliorant ainsi la sécurité et la fiabilité de l'application.  Elle inclut également une réactivation de la bannière de vérification des appareils et des améliorations de la gestion des exceptions de sécurité. Enfin, l'application est mise à jour vers la version 1.6.54 d'Element Android.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la réinitialisation complète de l'application en raison d'une erreur "Cannot find secrets in storage" [#1206](https://github.com/tchapgouv/tchap-android/pull/1206).
- Réactivation de la bannière de vérification des appareils pour une meilleure sécurité des sessions. [#1199](https://github.com/tchapgouv/tchap-android/pull/1199)
- Correction de la réinitialisation de l'identité, notamment pour les signatures croisées et la clé de récupération. [#1199](https://github.com/tchapgouv/tchap-android/pull/1199)
- Mise à jour vers la version 1.6.54 d'Element Android, incluant les correctifs et améliorations de cette version. [#1203](https://github.com/tchapgouv/tchap-android/pull/1203)

### Évolutions techniques
- Ajout d'une exception de sécurité pour OpenMapTiles. [#1204](https://github.com/tchapgouv/tchap-android/pull/1204)
- Correction de problèmes liés aux constantes lint. [#1205](https://github.com/tchapgouv/tchap-android/pull/1205)
- Ajout d'un fichier Fastlane pour la version 1.6.54, facilitant le processus de build et de publication.

### Autres changements
- Mise à jour de la documentation et des libellés dans le code.
- Ajout de changelogs pour les différentes modifications.
- Résolution de conflits lors de la fusion de branches.
- Correction de lint issues.
