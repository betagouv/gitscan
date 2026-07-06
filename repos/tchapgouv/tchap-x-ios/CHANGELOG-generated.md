## Changelog : tchap-x-ios (30 derniers jours, au 26 juin 2026)

### Résumé
Cette mise à jour intègre les dernières améliorations d'ElementX, incluant des corrections de bugs, des optimisations de l'interface utilisateur et l'ajout d'une fonctionnalité permettant de suggérer un badge lors de la création de salles privées chiffrées. L'application est également mise à jour avec la dernière version du SDK Rust Matrix.

### Évolutions fonctionnelles
- Ajout d'un badge suggéré lors de la création de salles privées chiffrées. [#51c4a3a1e](https://github.com/tchapgouv/tchap-x-ios/commit/51c4a3a1e)
- Correction de la couleur d'affichage des mentions dans le mode sombre pour une meilleure lisibilité. [#d4314613c](https://github.com/tchapgouv/tchap-x-ios/commit/d4314613c)
- Suppression du *feature flag* pour les salles privées non chiffrées, cette fonctionnalité est désormais pleinement activée. [#75355418b](https://github.com/tchapgouv/tchap-x-ios/commit/75355418b)
- Correction d'une boucle de tentatives infinie causée par l'abonnement aux threads. [#7bf26f87e](https://github.com/tchapgouv/tchap-x-ios/commit/7bf26f87e)
- Intégration de l'authentification automatique via Tchap Classic. [#755fe0621](https://github.com/tchapgouv/tchap-x-ios/commit/755fe0621)

### Évolutions techniques
- Mise à jour du SDK Rust Matrix vers la dernière version. [#bf059ce67](https://github.com/tchapgouv/tchap-x-ios/commit/bf059ce67)
- Intégration des changements d'ElementX iOS v26.06.0 et v26.05.3. [#2bac4cc7e](https://github.com/tchapgouv/tchap-x-ios/commit/2bac4cc7e), [#452d78622](https://github.com/tchapgouv/tchap-x-ios/commit/452d78622)
- Mise à jour de la librairie `compound-design-tokens` vers la version 10.2.1. [#a24aecbc5](https://github.com/tchapgouv/tchap-x-ios/commit/a24aecbc5)
- Corrections de conflits de rebase lors de l'intégration des changements d'ElementX. [#d051f350a](https://github.com/tchapgouv/tchap-x-ios/commit/d051f350a)
- Correction de problèmes de build Xcode après rebase. [#e755eb650](https://github.com/tchapgouv/tchap-x-ios/commit/e755eb650)

### Autres changements
- Correction de l'affichage flou d'un écran en déplaçant les badges d'éléments dans un `HStack`. [#7cf6fc21e](https://github.com/tchapgouv/tchap-x-ios/commit/7cf6fc21e)
- Incrémentation du numéro de version de l'application. [#dc1a1192d](https://github.com/tchapgouv/tchap-x-ios/commit/dc1a1192d), [#4b35051f1](https://github.com/tchapgouv/tchap-x-ios/commit/4b35051f1)
- Correction des tests unitaires pour assurer leur bon fonctionnement. [#68b16c973](https://github.com/tchapgouv/tchap-x-ios/commit/68b16c973)
