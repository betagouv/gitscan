## Changelog : tchap-x-android (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, la compatibilité et l'expérience utilisateur de Tchap. Des corrections ont été apportées pour assurer le bon fonctionnement sur différents appareils et configurations, notamment en lien avec l'authentification OAuth et les appareils 32 bits. De nouvelles fonctionnalités, comme la commande `/visio`, ont été ajoutées et des améliorations apportées à l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de la commande `/visio` pour lancer une visioconférence. [#132aeafe86](https://github.com/tchapgouv/tchap-x-android/commit/132aeafe86)
- Activation des commandes dans les messages. [#2157fcc8b4](https://github.com/tchapgouv/tchap-x-android/commit/2157fcc8b4)
- Badge "Recommandé" ajouté pour les salons privés chiffrés, facilitant leur identification. [#519ed37fd8](https://github.com/tchapgouv/tchap-x-android/commit/519ed37fd8)
- Affichage d'un message d'alerte lors du partage d'un fichier dans un salon non chiffré, sensibilisant l'utilisateur aux risques. [#48e7c8410e](https://github.com/tchapgouv/tchap-x-android/commit/48e7c8410e)
- Instructions ajoutées pour activer la sauvegarde automatique dans Tchap Classique. [#4712546b22](https://github.com/tchapgouv/tchap-x-android/commit/4712546b22)
- Suppression du bandeau de réinitialisation d'identité d'un membre. [#61ecf4c478](https://github.com/tchapgouv/tchap-x-android/commit/61ecf4c478)
- Renommage de l'application Tchap beta en Tchap. [#a3fea70d86](https://github.com/tchapgouv/tchap-x-android/commit/a3fea70d86)

### Évolutions techniques
- Amélioration de la connexion OAuth avec détection du package de l'application. [#29e54cf664](https://github.com/tchapgouv/tchap-x-android/commit/29e54cf664)
- Autorisation des certificats CRL-only (sans OCSP) pour une meilleure flexibilité en matière de sécurité. [#b3873999b3](https://github.com/tchapgouv/tchap-x-android/commit/b3873999b3)
- Correction pour la compatibilité avec les appareils 32 bits. [#916280a72c](https://github.com/tchapgouv/tchap-x-android/commit/916280a72c) et [#13e9519074](https://github.com/tchapgouv/tchap-x-android/commit/13e9519074)
- Configuration des URL de Push en fonction de l'environnement. [#0b8d1a6dbe](https://github.com/tchapgouv/tchap-x-android/commit/0b8d1a6dbe)
- Mise à jour des certificats de juillet 2026. [#7518e72b7f](https://github.com/tchapgouv/tchap-x-android/commit/7518e72b7f)
- Suppression des noms de domaine Element non utilisés. [#a5bcfa26b4](https://github.com/tchapgouv/tchap-x-android/commit/a5bcfa26b4)
- Correction pour la connexion via Tchap Classique avec ProConnect. [#7bd7a33f01](https://github.com/tchapgouv/tchap-x-android/commit/7bd7a33f01)

### Autres changements
- Désactivation temporaire de Unified Push en raison de problèmes de fonctionnement. [#35e1699a51](https://github.com/tchapgouv/tchap-x-android/commit/35e1699a51)
- Suppression de la bordure pour les badges neutres. [#31839dba2d](https://github.com/tchapgouv/tchap-x-android/commit/31839dba2d)
- Mise à jour de Compound et amélioration des badges. [#624e73bb76](https://github.com/tchapgouv/tchap-x-android/commit/624e73bb76)
- Changement du format de numéro de version. [#72f5f3555f](https://github.com/tchapgouv/tchap-x-android/commit/72f5f3555f)
- Ajout du lien du Play Store dans le script de release. [#f17037e507](https://github.com/tchapgouv/tchap-x-android/commit/f17037e507)
- Listing des hash des APKs lors de la génération de la release. [#d860e38504](https://github.com/tchapgouv/tchap-x-android/commit/d860e38504)
