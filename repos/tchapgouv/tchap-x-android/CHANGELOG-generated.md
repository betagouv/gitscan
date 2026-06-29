## Changelog : tchap-x-android (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment dans la gestion des médias, la sécurité et la convivialité générale. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que la préparation pour de futures fonctionnalités comme le partage de position.

### Évolutions fonctionnelles
- Ajout d'un badge "Recommandé" pour les salons privés chiffrés [#519ed37fd8](https://github.com/tchapgouv/tchap-x-android/commit/519ed37fd8).
- Activation des salons privés non-chiffrés [#6b812802f0](https://github.com/tchapgouv/tchap-x-android/commit/6b812802f0).
- Amélioration de l'affichage des fichiers et de leur taille dans les médias [#1c058037be](https://github.com/tchapgouv/tchap-x-android/commit/1c058037be).
- Amélioration de la visualisation des images et ajout d'options de retournement [#a095190902](https://github.com/tchapgouv/tchap-x-android/commit/a095190902).
- Re-organisation des éléments dans les détails d'une salle (room details) [#6222416b17](https://github.com/tchapgouv/tchap-x-android/commit/6222416b17).
- Ajout d'indicateurs de nombre de messages non lus dans les salons [#27cdc0fe7d](https://github.com/tchapgouv/tchap-x-android/commit/27cdc0fe7d).
- Suppression du support d'Android Auto (mode voiture) [#d824afd998](https://github.com/tchapgouv/tchap-x-android/commit/d824afd998).
- Renommage de la section "Direct" en "Personnes" [#3656d854c6](https://github.com/tchapgouv/tchap-x-android/commit/3656d854c6).
- Amélioration de la gestion des erreurs de localisation et arrêt du partage en cas de problème [#1a40e460ae](https://github.com/tchapgouv/tchap-x-android/commit/1a40e460ae).
- Ajout de sections "Rageshake" et "ClearCache" dans les paramètres avancés [#c02c175f07](https://github.com/tchapgouv/tchap-x-android/commit/c02c175f07).

### Évolutions techniques
- Mise à jour du SDK Matrix Rust en version 26.06.3 [#1863b3aef7](https://github.com/tchapgouv/tchap-x-android/commit/1863b3aef7).
- Mise à jour de la librairie Maplibre GL Android SDK en version 13.2.0 [#be0eb003bf](https://github.com/tchapgouv/tchap-x-android/commit/be0eb003bf).
- Mise à jour de la librairie Posthog Android en version 3.47.0 [#a6ca210558](https://github.com/tchapgouv/tchap-x-android/commit/a6ca210558).
- Mise à jour de la librairie Kotlin en version 2.3.9 [#ea529261da](https://github.com/tchapgouv/tchap-x-android/commit/ea529261da).
- Intégration de Compound Design Tokens 10.2.1 [#1a73ab0094](https://github.com/tchapgouv/tchap-x-android/commit/1a73ab0094).
- Amélioration de la compilation du SDK Rust et passage en mode release par défaut [#0f5c6eb9cf](https://github.com/tchapgouv/tchap-x-android/commit/0f5c6eb9cf).
- Optimisation de la génération des snapshots et nettoyage automatique des anciennes [#47c95ba41e](https://github.com/tchapgouv/tchap-x-android/commit/47c95ba41e).
- Correction de bugs liés à la compilation et aux tests [#b6d7b6cb76](https://github.com/tchapgouv/tchap-x-android/commit/b6d7b6cb76), [#021251e42e](https://github.com/tchapgouv/tchap-x-android/commit/021251e42e).
- Correction de l'affichage du menu d'historique [#b6d7b6cb76](https://github.com/tchapgouv/tchap-x-android/commit/b6d7b6cb76).
- Suppression de la version 0.11.0 [#ee4041c368](https://github.com/tchapgouv/tchap-x-android/commit/ee4041c368).

### Autres changements
- Correction de l'icône d'envoi de message en mode sombre [#a8491c7c6d](https://github.com/tchapgouv/tchap-x-android/commit/a8491c7c6d).
- Remplacement du logo Tchap sur Android Studio [#f15bcee146](https://github.com/tchapgouv/tchap-x-android/commit/f15bcee146).
- Rendu monochrome du logo Tchap dans les notifications [#33a4c997bb](https://github.com/tchapgouv/tchap-x-android/commit/33a4c997bb).
- Réduction de la taille des logs pour éviter les erreurs serveur [#873a43a968](https://github.com/tchapgouv/tchap-x-android/commit/873a43a968).
- Mise à jour des captures d'écran [#ce18c5eb2e](https://github.com/tchapgouv/tchap-x-android/commit/ce18c5eb2e), [#959fd008ea](https://github.com/tchapgouv/tchap-x-android/commit/959fd008ea), [#b016fb3dc2](https://github.com/tchapgouv/tchap-x-android/commit/b016fb3dc2), [#31776a74f7](https://github.com/tchapgouv/tchap-x-android/commit/31776a74f7), [#a9bf48779b](https://github.com/tchapgouv/tchap-x-android/commit/a9bf48779b).
- Corrections de tests et de linting [#337528bce3](https://github.com/tchapgouv/tchap-x-android/commit/337528bce3), [#a6000a6745](https://github.com/tchapgouv/tchap-x-android/commit/a6000a6745).
