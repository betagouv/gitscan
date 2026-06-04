## Changelog : tchap-x-android (30 derniers jours, au 2 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à la stabilité et à l'expérience utilisateur. Parmi les nouveautés, on note l'amélioration de la gestion des codes PIN, des correctifs pour les problèmes de duplication d'éléments dans l'interface, et l'ajout de la possibilité de partager sa position en direct. Des mises à jour de dépendances et des corrections de bugs mineurs ont également été intégrées.

### Évolutions fonctionnelles
- Ajout de la possibilité de partager sa position en direct dans les conversations [#6741](https://github.com/tchapgouv/tchap-x-android/pull/6741).
- Amélioration de l'expérience utilisateur lors de la configuration du code PIN, avec des messages d'erreur plus clairs et une meilleure gestion des tentatives infructueuses [#6780](https://github.com/tchapgouv/tchap-x-android/pull/6780).
- Ajout d'un écran d'expiration de compte pour une meilleure gestion de la sécurité [#6720](https://github.com/tchapgouv/tchap-x-android/pull/6720).
- Correction de bugs liés à la création de salons publics [#6720](https://github.com/tchapgouv/tchap-x-android/pull/6720).
- Amélioration de la gestion des invitations dans les conversations privées, avec la création automatique d'une salle si nécessaire [#6756](https://github.com/tchapgouv/tchap-x-android/pull/6756).
- Possibilité de se connecter depuis Tchap Legacy [#6712](https://github.com/tchapgouv/tchap-x-android/pull/6712).
- Amélioration de l'affichage des images, avec une meilleure qualité par défaut [#6718](https://github.com/tchapgouv/tchap-x-android/pull/6718).
- Ajout du nouveau logo Tchap dans la liste des sessions [#6699](https://github.com/tchapgouv/tchap-x-android/pull/6699).
- Amélioration de l'affichage des médias, notamment pour les légendes [#6715](https://github.com/tchapgouv/tchap-x-android/pull/6715).
- Suppression de la possibilité de prendre des captures d'écran dans l'application [#6695](https://github.com/tchapgouv/tchap-x-android/pull/6695).
- Ajout de la lecture MIDI [#6770](https://github.com/tchapgouv/tchap-x-android/pull/6770).

### Évolutions techniques
- Mise à jour du SDK Matrix Rust vers la version 26.05.18 [#6805](https://github.com/tchapgouv/tchap-x-android/pull/6805).
- Mises à jour de plusieurs dépendances, incluant Firebase, Compose, et d'autres bibliothèques.
- Amélioration du script de release pour une meilleure automatisation et fiabilité.
- Correction d'ID dupliqués dans le SDK Rust (BWI) [#6696](https://github.com/tchapgouv/tchap-x-android/pull/6696).
- Amélioration de la gestion des certificats Let's Encrypt en environnement de développement.
- Ajout de builds de développement avec des options spécifiques pour le débogage.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Suppression de l'utilisation de Feature Flags pour certaines fonctionnalités, les activant définitivement.
- Amélioration de la gestion des erreurs et des exceptions.

### Autres changements
- Synchronisation des chaînes de caractères depuis Localazy pour les traductions.
- Mise à jour des captures d'écran de l'application.
- Corrections de bugs mineurs et améliorations de la stabilité.
- Ajout de previews spécifiques à Tchap.
- Nettoyage du code et amélioration de la documentation.
- Correction de problèmes liés à la duplication d'éléments dans la liste des salles [#6793](https://github.com/tchapgouv/tchap-x-android/pull/6793).
- Correction de problèmes avec le bouton retour dans la vue web [#6725](https://github.com/tchapgouv/tchap-x-android/pull/6725).
- Amélioration de la fiabilité de `FetchPushForegroundService` [#6757](https://github.com/tchapgouv/tchap-x-android/pull/6757).
- Correction de problèmes liés à l'affichage des avatars dans les conversations privées [#6738](https://github.com/tchapgouv/tchap-x-android/pull/6738).
- Suppression de l'indicateur de fonctionnalité LiveLocationSharing.
- Désactivation du déverrouillage biométrique lors de la désactivation du code PIN [#6781](https://github.com/tchapgouv/tchap-x-android/pull/6781).
