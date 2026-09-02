## Changelog : tchap-x-android (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur, notamment grâce à une meilleure gestion des statuts de profil (emojis) et une simplification du processus de connexion. La sécurité a été renforcée avec l'intégration de nouveaux mécanismes de scan, tandis que la stabilité de l'application a été consolidée par de nombreuses corrections sur les appels, la gestion des médias et l'interface utilisateur.

### Évolutions fonctionnelles
- **Profil et Statut** : Ajout de badges d'emoji pour afficher le statut de l'utilisateur sur son avatar et synchronisation automatique des changements de profil via le SDK Rust.
- **Appels et Communication** : 
    - Affichage des participants actifs dans la liste des personnes lors d'un appel [#7199](https://github.com/tchapgouv/tchap-x-android/pull/7300).
    - Ajout du menu "ajouter des réactions" dans l'écran des fils de discussion (threads) [#7388](https://github.com/tchapgouv/tchap-x-android/pull/7388).
    - Amélioration de la lecture des messages vocaux (maintien de la lecture même quand l'écran s'éteint).
- **Connexion et Sécurité** :
    - Possibilité de se connecter via l'email partagé par Tchap Classique.
    - Amélioration du processus de liaison d'un nouvel appareil (gestion du timer pour le scan de QR Code et corrections de la biométrie) [#7303](https://github.com/tchapgouv/tchap-x-android/pull/7303).
    - Intégration de fonctionnalités de scan anti-virus et récupération de l'URL du scanner depuis le serveur.
- **Interface Utilisateur** :
    - Amélioration de l'affichage de l'emoji picker et de la galerie média.
    - Affichage d'un indicateur "Message non trouvé" lorsqu'une réponse pointe vers un message chargé impossible à récupérer [#7376](https://github.com/tchapgouv/tchap-x-android/pull/7376).
    - Affichage de l'ID Matrix dans le sélecteur de salon pour les messages directs.

### Évolutions techniques
- **Architecture et SDK** : 
    - Refonte majeure de la gestion de la configuration d'entreprise (`WellknownRetriever`) et de la récupération d'URL pour une meilleure modularité.
    - Correction du SDK Rust pour assurer la compatibilité avec les architectures arm64.
- **Performance et Build** :
    - Activation de la synchronisation parallèle sur Gradle pour accélérer les temps de compilation.
    - Mise à jour des outils de déploiement (Fastlane).
- **Maintenance et Correctifs** :
    - Corrections de l'accessibilité [#7136](https://github.com/tchapgouv/tchap-x-android/pull/7136).
    - Résolution de divers problèmes de mise en page (layout) et de gestion du débit vidéo (bitrate).

### Autres changements
- **Documentation et Support** : Remplacement des liens vers l'aide d'Element par la FAQ officielle de Tchap.
- **Maintenance du code** : Nettoyage général (Linter, suppression de TODOs) et mise à jour des captures d'écran de l'application.
