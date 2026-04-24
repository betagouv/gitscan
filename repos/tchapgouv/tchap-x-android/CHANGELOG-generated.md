## Changelog : tchap-x-android (30 derniers jours, au 13 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment une meilleure gestion des espaces et des salons, des corrections de bugs importants, et des ajustements d'interface pour une expérience utilisateur plus fluide et conforme aux standards Tchap. Plusieurs versions intermédiaires ont été publiées pour assurer une progression stable et continue.

### Évolutions fonctionnelles
- Ajout du filtre des conversations par Espace depuis la liste des Espaces.
- Ajout de l'option "Accès par lien" dans les paramètres du salon [#1639ce9b47](https://github.com/tchapgouv/tchap-x-android/commit/1639ce9b47).
- Renouvellement de l'invitation par email pour les futurs utilisateurs externes [#94efe0da38](https://github.com/tchapgouv/tchap-x-android/commit/94efe0da38).
- Correction de la création des salons privés non chiffrés [#00d401bf21](https://github.com/tchapgouv/tchap-x-android/commit/00d401bf21).
- Mise à jour de l'URL de report de bug [#df5acb2cac](https://github.com/tchapgouv/tchap-x-android/commit/df5acb2cac).
- Alignement du wording avec la taxonomie Tchap [#5bc6b41678](https://github.com/tchapgouv/tchap-x-android/commit/5bc6b41678) et [#295f14d777](https://github.com/tchapgouv/tchap-x-android/commit/295f14d777).

### Évolutions techniques
- Mise à jour du SDK Matrix Rust.
- Utilisation de `BuildTimeConfig` pour les variables publiques [#c2d101853f](https://github.com/tchapgouv/tchap-x-android/commit/c2d101853f).
- Correction du job Compose tests lors du build [#b58c2d8f03](https://github.com/tchapgouv/tchap-x-android/commit/b58c2d8f03).
- Correction du job Sonar lors du build [#d4cda566d8](https://github.com/tchapgouv/tchap-x-android/commit/d4cda566d8).
- Import des `compound-design-tokens` [#66098065c7](https://github.com/tchapgouv/tchap-x-android/commit/66098065c7).
- Changement des couleurs de fond des messages et de l'UI contraste élevé [#6a0c0bef0b](https://github.com/tchapgouv/tchap-x-android/commit/6a0c0bef0b).
- Suppression des délais inutiles lors de la récupération de `access_rules.visibility` via une requête [#b8502d0656](https://github.com/tchapgouv/tchap-x-android/commit/b8502d0656).
- Désactivation du certificat pinning pour les fonds de cartes [#2c63999084](https://github.com/tchapgouv/tchap-x-android/commit/2c63999084) et sur l'environnement de développement [#b4f95c446f](https://github.com/tchapgouv/tchap-x-android/commit/b4f95c446f).

### Autres changements
- Traduction des notes de release [#b284e66d02](https://github.com/tchapgouv/tchap-x-android/commit/b284e66d02).
- Mise à jour des captures d'écran [#413ee7a9e9](https://github.com/tchapgouv/tchap-x-android/commit/413ee7a9e9).
- Publication des versions 0.6.0, 0.7.0, 0.8.0, 0.8.1 et 0.8.2.
