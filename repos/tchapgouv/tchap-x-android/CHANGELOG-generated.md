## Changelog : tchap-x-android (30 derniers jours, au 24 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une meilleure gestion des espaces et des salons, des corrections de bugs et des améliorations de l'interface utilisateur. Des efforts ont été faits pour aligner la terminologie avec la taxonomie Tchap et pour faciliter le processus de publication de nouvelles versions.

### Évolutions fonctionnelles
- Ajout du filtre des conversations par Espace depuis la liste des Espaces. [#49afd5d933](https://github.com/tchapgouv/tchap-x-android/commit/49afd5d933)
- Ajout de l'option "Accès par lien" dans les paramètres du salon. [#1639ce9b47](https://github.com/tchapgouv/tchap-x-android/commit/1639ce9b47)
- Renouvellement de l'invitation par email pour les futurs utilisateurs externes. [#94efe0da38](https://github.com/tchapgouv/tchap-x-android/commit/94efe0da38)
- Affichage d'un message lorsque Tchap est inaccessible. [#a18e3f4ebe](https://github.com/tchapgouv/tchap-x-android/commit/a18e3f4ebe)
- Correction de la création des salons privés non chiffrés. [#00d401bf21](https://github.com/tchapgouv/tchap-x-android/commit/00d401bf21)
- Modification de la description de l'onglet Espace pour plus de clarté. [#305ee9355e](https://github.com/tchapgouv/tchap-x-android/commit/305ee9355e)

### Évolutions techniques
- Mise à jour du SDK Matrix Rust et intégration de Element X 26.03.3. [#f9024f5067](https://github.com/tchapgouv/tchap-x-android/commit/f9024f5067) et [#89e887440e](https://github.com/tchapgouv/tchap-x-android/commit/89e887440e)
- Utilisation du `BuildTimeConfig` pour les variables publiques afin d'améliorer la gestion de la configuration. [#c2d101853f](https://github.com/tchapgouv/tchap-x-android/commit/c2d101853f)
- Correction du job Compose tests lors du build. [#b58c2d8f03](https://github.com/tchapgouv/tchap-x-android/commit/b58c2d8f03)
- Correction du job Sonar lors du build. [#d4cda566d8](https://github.com/tchapgouv/tchap-x-android/commit/d4cda566d8)
- Désactivation du certificat pinning pour les fonds de cartes. [#2c63999084](https://github.com/tchapgouv/tchap-x-android/commit/2c63999084)
- Désactivation du certificate pinning sur l'environnement de développement. [#b4f95c446f](https://github.com/tchapgouv/tchap-x-android/commit/b4f95c446f)
- Mise en place d'un script de génération de release pour Tchap. [#ddf1521460](https://github.com/tchapgouv/tchap-x-android/commit/ddf1521460)
- Utilisation temporaire du format de version Major/Minor/Patch. [#1e4d0240fd](https://github.com/tchapgouv/tchap-x-android/commit/1e4d0240fd)

### Autres changements
- Alignement du wording avec la taxonomie Tchap. [#5bc6b41678](https://github.com/tchapgouv/tchap-x-android/commit/5bc6b41678) et [#295f14d777](https://github.com/tchapgouv/tchap-x-android/commit/295f14d777)
- Correction du dégradé pour le surlignage des messages. [#515adb81d0](https://github.com/tchapgouv/tchap-x-android/commit/515adb81d0)
- Correction de textes. [#f2a9997ef4](https://github.com/tchapgouv/tchap-x-android/commit/f2a9997ef4)
- Correction des délais inutiles lors de la récupération de `access_rules.visibility` via une requête. [#b8502d0656](https://github.com/tchapgouv/tchap-x-android/commit/b8502d0656)
- Changement des couleurs de fond des messages et de l'UI contraste élevé. [#6a0c0bef0b](https://github.com/tchapgouv/tchap-x-android/commit/6a0c0bef0b)
- Import des `compound-design-tokens`. [#66098065c7](https://github.com/tchapgouv/tchap-x-android/commit/66098065c7)
- Mise à jour des screenshots. [#413ee7a9e9](https://github.com/tchapgouv/tchap-x-android/commit/413ee7a9e9)
- Traduction des notes de release. [#b284e66d02](https://github.com/tchapgouv/tchap-x-android/commit/b284e66d02)
