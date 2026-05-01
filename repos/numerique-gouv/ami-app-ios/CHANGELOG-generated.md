## Changelog : ami-app-ios (30 derniers jours, au 29 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la navigation et à l'expérience utilisateur, notamment en gérant mieux les liens externes et le retour en arrière depuis les pages web. L'application a également été optimisée pour une meilleure gestion des notifications et des partenaires. Des corrections de bugs et des améliorations techniques ont été apportées pour une plus grande stabilité et performance.

### Évolutions fonctionnelles
- **Gestion des liens et navigation :** Amélioration de la gestion du bouton "Retour" lors de la navigation vers des services partenaires ou des pages externes, assurant un retour cohérent à l'application. [#82](https://github.com/numerique-gouv/ami-app-ios/pull/82) et [#78](https://github.com/numerique-gouv/ami-app-ios/pull/78)
- **Partage de logs :** Le bouton de partage de logs a été mis à jour avec le nouveau design DSFR. [#83](https://github.com/numerique-gouv/ami-app-ios/pull/83) et [#73](https://github.com/numerique-gouv/ami-app-ios/pull/73)
- **Gestion des notifications :** L'application ouvre désormais la page des notifications lorsqu'un utilisateur clique sur une notification push. [#59](https://github.com/numerique-gouv/ami-app-ios/pull/59)
- **Onboarding Notifications :** Promotion de la page d'onboarding des notifications en natif. [#71](https://github.com/numerique-gouv/ami-app-ios/pull/71)
- **Liens "mailto" :** La gestion des liens "mailto" (pour envoyer un email) a été réactivée sur les pages partenaires. [#65](https://github.com/numerique-gouv/ami-app-ios/pull/65)
- **Affichage des partenaires :** Amélioration de l'affichage des partenaires et de la navigation vers leurs pages.

### Évolutions techniques
- **Refactoring de la navigation :** Refonte de la navigation avec l'introduction d'un `AppState` et l'utilisation d'un `NavigationStack` pour une meilleure gestion de la navigation et du retour en arrière.
- **Gestion des WebView :** Amélioration de la gestion des WebView, notamment pour la gestion des liens et la navigation.
- **Architecture :** Introduction d'un `ViewModel` pour la vue racine de l'application pour une meilleure séparation des préoccupations. [#80](https://github.com/numerique-gouv/ami-app-ios/pull/80)
- **Gestion des certificats :**  Acceptation uniquement des certificats auto-signés en mode DEBUG. [#edc2b85](https://github.com/numerique-gouv/ami-app-ios/commit/edc2b85)
- **Firebase :** Amélioration de la gestion de l'enregistrement des tokens Firebase.
- **Observable :** La classe `InformationBanner` adopte le protocole `@Observable`.
- **Suppression de code obsolète :** Suppression de fichiers de configuration et de code commenté inutiles.

### Autres changements
- Correction de typos et amélioration des messages de log.
- Mise à jour de la documentation et des commentaires.
- Amélioration de la structure du code et de la lisibilité.
- Suppression de dépendances inutiles.
- Correction de bugs mineurs liés à l'affichage et à la navigation.
