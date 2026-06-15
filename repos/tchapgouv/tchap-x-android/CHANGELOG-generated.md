## Changelog : tchap-x-android (30 derniers jours, au 12 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à la stabilité et à l'expérience utilisateur.  Plusieurs correctifs ont été implémentés pour améliorer la gestion des connexions, des salons, des médias et des autorisations. Des mises à jour de l'interface utilisateur ont également été effectuées, notamment le renommage d'une section et la correction d'icônes.

### Évolutions fonctionnelles
- Renommage de la section "Direct" en "Personnes" pour une meilleure clarté. [#3656d854c6](https://github.com/tchapgouv/tchap-x-android/commit/3656d854c6)
- Correction de l'icône d'envoi de message en mode sombre. [#a8491c7c6d](https://github.com/tchapgouv/tchap-x-android/commit/a8491c7c6d)
- Support pour la connexion à partir de Tchap Legacy. [#1218f37b77](https://github.com/tchapgouv/tchap-x-android/commit/1218f37b77)
- Ajout d'un écran d'expiration de compte. [#07202fbe6b](https://github.com/tchapgouv/tchap-x-android/commit/07202fbe6b)
- Amélioration de la création de salons publics. [#efee76bff3](https://github.com/tchapgouv/tchap-x-android/commit/efee76bff3)
- Possibilité de créer un nouveau salon lors de l'invitation de personnes en DM. [#174a6cad0d](https://github.com/tchapgouv/tchap-x-android/commit/174a6cad0d)
- Lecture MIDI ajoutée. [#e6c3a8ff1d](https://github.com/tchapgouv/tchap-x-android/commit/e6c3a8ff1d)
- Correction pour la création de salons publiques. [#2954174c56](https://github.com/tchapgouv/tchap-x-android/commit/2954174c56)
- Amélioration du script de release. [#9768a9b5fe](https://github.com/tchapgouv/tchap-x-android/commit/9768a9b5fe)
- Correction des ID dupliqués dans le rust-sdk (BWI). [#e1c04ea084](https://github.com/tchapgouv/tchap-x-android/commit/e1c04ea084)
- Suppression de la version 0.11.0. [#ee4041c368](https://github.com/tchapgouv/tchap-x-android/commit/ee4041c368)

### Évolutions techniques
- Mise à jour du SDK Matrix Rust vers la version 26.05.18.
- Mise à jour des thèmes (compound-design-tokens). [#0c7fcb9313](https://github.com/tchapgouv/tchap-x-android/commit/0c7fcb9313)
- Compilation du SDK en release par défaut pour optimiser les performances. [#ee3c1091fa](https://github.com/tchapgouv/tchap-x-android/commit/ee3c1091fa)
- Cartes : Amélioration de la génération des snapshots et nettoyage automatique des anciennes. [#47c95ba41e](https://github.com/tchapgouv/tchap-x-android/commit/47c95ba41e)
- Correction de la compilation du rust-sdk. [#0f5c6eb9cf](https://github.com/tchapgouv/tchap-x-android/commit/0f5c6eb9cf)
- Suppression du support pour Android Auto (mode voiture). [#d824afd998](https://github.com/tchapgouv/tchap-x-android/commit/d824afd998)
- Mise à jour de Firebase BOM vers la version 34.13.0.
- Mise à jour de androidx.webkit:webkit vers la version 1.16.0.
- Suppression du flag de fonctionnalité LiveLocationSharing.
- Correction pour la numérotation des badges de mentions. [#a9152c9049](https://github.com/tchapgouv/tchap-x-android/commit/a9152c9049)

### Autres changements
- Ajout des sections RageShake et ClearCache dans les paramètres avancés. [#c02c175f07](https://github.com/tchapgouv/tchap-x-android/commit/c02c175f07)
- Petites corrections du linter et du script de release. [#a6000a6745](https://github.com/tchapgouv/tchap-x-android/commit/a6000a6745)
- Désactivation des screenshots sur l'application. [#6f09957591](https://github.com/tchapgouv/tchap-x-android/commit/6f09957591)
- Nettoyage des access_rules à la création de salons. [#69404aedae](https://github.com/tchapgouv/tchap-x-android/commit/69404aedae)
- Ajout du nouveau logo Tchap dans la liste des sessions. [#ce12cda04a](https://github.com/tchapgouv/tchap-x-android/commit/ce12cda04a)
- Mise à jour des captures d'écran.
- Correction pour l'utilisation de QR code pour la connexion depuis un appareil non connecté.
- Suppression de la fonctionnalité biometric unlock lorsque le code PIN est désactivé.
- Correction de la duplication d'éléments dans la liste des salles.
- Augmentation de la qualité des images par défaut. [#07b5b0c3e0](https://github.com/tchapgouv/tchap-x-android/commit/07b5b0c3e0)
- Autorisation des certificats Let's Encrypt sur l'environnement de développement. [#e3da88f812](https://github.com/tchapgouv/tchap-x-android/commit/e3da88f812)
- Suffixe le nom de l'application avec le buildType (debug / nightly). [#f38b2e3453](https://github.com/tchapgouv/tchap-x-android/commit/f38b2e3453)
- Vérification de la connexion avec le code de récupération si disponible. [#20d3b81f30](https://github.com/tchapgouv/tchap-x-android/commit/20d3b81f30)
- Limitation des espaces au mode consultation. [#0440e6071e](https://github.com/tchapgouv/tchap-x-android/commit/0440e6071e)
