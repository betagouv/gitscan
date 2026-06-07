## Changelog : tchap-x-android (30 derniers jours, au 06 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la stabilité et à l'expérience utilisateur de l'application. Les points clés incluent des corrections de bugs, des optimisations de performance, l'ajout de nouvelles fonctionnalités comme le partage de position en direct, et des améliorations de l'interface utilisateur, notamment pour les appels et la gestion des salons. Des efforts ont également été faits pour améliorer la compatibilité et la sécurité de l'application.

### Évolutions fonctionnelles
- **Partage de position en direct :** Ajout de la fonctionnalité permettant de partager sa position en temps réel. [#6741](https://github.com/tchapgouv/tchap-x-android/pull/6741)
- **Appels :** Amélioration de l'affichage de l'écran d'appel en mode plein écran. [#6751](https://github.com/tchapgouv/tchap-x-android/pull/6751)
- **Salons :** Correction de la création de salons publics. [#6725](https://github.com/tchapgouv/tchap-x-android/pull/6725)
- **DM :** Amélioration de l'affichage des détails des conversations directes (DM), affichant uniquement l'avatar de l'autre utilisateur. [#6738](https://github.com/tchapgouv/tchap-x-android/pull/6738)
- **Connexion :** Possibilité de se connecter à Tchap Legacy. [#1218f37b77](https://github.com/tchapgouv/tchap-x-android/commit/1218f37b77)
- **Expiration de compte :** Ajout d'un écran pour gérer l'expiration du compte. [#07202fbe6b](https://github.com/tchapgouv/tchap-x-android/commit/07202fbe6b)
- **Médias :** Amélioration du formatage des légendes des médias dans le visualiseur de médias. [#6729](https://github.com/tchapgouv/tchap-x-android/pull/6729)
- **Notifications :** Correction de l'affichage des notifications lors des appels.
- **QR Code :** Amélioration de la gestion du scan de QR code depuis un appareil non connecté. [#6783](https://github.com/tchapgouv/tchap-x-android/pull/6783)
- **Cache :** Correction pour ne pas supprimer le dossier `logs` lors du nettoyage du cache. [#6765](https://github.com/tchapgouv/tchap-x-android/pull/6765)

### Évolutions techniques
- **Rust SDK :** Correction d'ID dupliqués dans le SDK Rust. [#e1c04ea084](https://github.com/tchapgouv/tchap-x-android/commit/e1c04ea084)
- **Compilation :** La compilation du SDK Rust se fait désormais en mode release par défaut. [#ee3c1091fa](https://github.com/tchapgouv/tchap-x-android/commit/ee3c1091fa)
- **Thèmes :** Mise à jour des thèmes (compound-design-tokens). [#0c7fcb9313](https://github.com/tchapgouv/tchap-x-android/commit/0c7fcb9313)
- **Cartes :** Amélioration de la génération des snapshots et nettoyage automatique des anciennes cartes. [#47c95ba41e](https://github.com/tchapgouv/tchap-x-android/commit/47c95ba41e)
- **Build :** Ajout d'une build de développement et configuration des options de build. [#b436f337e1](https://github.com/tchapgouv/tchap-x-android/commit/b436f337e1)
- **Localazy :** Synchronisation des chaînes de caractères depuis Localazy. [#6761](https://github.com/tchapgouv/tchap-x-android/pull/6761)
- **Firebase :** Mise à jour de la version de Firebase. [#6789](https://github.com/tchapgouv/tchap-x-android/pull/6789)
- **Dépendances :** Mises à jour de plusieurs dépendances (Kotlin, Sentry, Compose, etc.).

### Autres changements
- **Paramètres avancés :** Ajout des options "Rageshake" et "ClearCache" dans les paramètres avancés. [#c02c175f07](https://github.com/tchapgouv/tchap-x-android/commit/c02c175f07)
- **Logo :** Ajout du nouveau logo Tchap dans la liste des sessions. [#ce12cda04a](https://github.com/tchapgouv/tchap-x-android/commit/ce12cda04a)
- **Screenshots :** Mise à jour des captures d'écran. [#6750](https://github.com/tchapgouv/tchap-x-android/pull/6750)
- **Documentation :** Autorisation des certificats Let's Encrypt sur l'environnement de développement. [#e3da88f812](https://github.com/tchapgouv/tchap-x-android/commit/e3da88f812)
- **Nom de l'application :** Suffixe le nom de l'application avec le buildType (debug / nightly). [#f38b2e3453](https://github.com/tchapgouv/tchap-x-android/commit/f38b2e3453)
- **Suppression de versions :** Suppression de la version 0.11.0. [#ee4041c368](https://github.com/tchapgouv/tchap-x-android/commit/ee4041c368)
- **Corrections de bugs mineurs :** Plusieurs corrections de bugs et améliorations de la qualité du code.
