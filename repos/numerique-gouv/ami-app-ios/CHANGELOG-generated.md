## Changelog : ami-app-ios (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la navigation et à l'expérience utilisateur, notamment en gérant mieux le retour en arrière depuis les pages partenaires et en intégrant une page d'onboarding pour les notifications. L'apparence du bouton de partage de logs a également été mise à jour et l'application est plus robuste face aux liens externes.

### Évolutions fonctionnelles
- **Navigation améliorée :** Le bouton de retour est maintenant correctement affiché lors de la navigation vers des services partenaires et permet de revenir à la page précédente. [#82](https://github.com/numerique-gouv/ami-app-ios/pull/82), [#78](https://github.com/numerique-gouv/ami-app-ios/pull/78)
- **Bouton de partage de logs :** Le bouton de partage de logs a été mis à jour avec le nouveau design DSFR et est maintenant positionné en bas de page. [#72](https://github.com/numerique-gouv/ami-app-ios/pull/72)
- **Onboarding Notifications :** Une nouvelle page d'onboarding a été ajoutée pour promouvoir l'activation des notifications en natif. [#71](https://github.com/numerique-gouv/ami-app-ios/pull/71)
- **Gestion des liens :** L'application gère maintenant correctement les liens `mailto` sur les pages partenaires.
- **Retour à la page d'accueil :** Navigation vers la page d'accueil après avoir effectué un choix concernant la réception des notifications. [#76](https://github.com/numerique-gouv/ami-app-ios/pull/76)
- **Affichage des bannières d'information :** Réactivation de l'affichage des bannières d'information. [#91](https://github.com/numerique-gouv/ami-app-ios/pull/91)

### Évolutions techniques
- **Refonte de la navigation :** La navigation a été refactorisée en utilisant un `NavigationStack` pour une meilleure gestion de la pile de navigation.
- **Introduction de `AppState` :** Une nouvelle classe `AppState` a été introduite pour gérer l'état de l'application, notamment la connectivité réseau.
- **Utilisation de `@Observable` :** La classe `InformationBanner` a été mise à jour pour adopter le pattern `@Observable` pour une meilleure réactivité.
- **Gestion des URL :** Utilisation d'un `enum` pour détecter les URL spéciales et simplification de la gestion des URL racine. [#86](https://github.com/numerique-gouv/ami-app-ios/pull/86)
- **Architecture ViewModel :** Introduction d'un ViewModel pour la vue racine de l'application. [#80](https://github.com/numerique-gouv/ami-app-ios/pull/80)
- **Suppression de code inutile :** Plusieurs sections de code inutilisées ont été supprimées pour améliorer la maintenabilité.

### Autres changements
- Suppression du container de bannières inutile dans la vue principale. [#93](https://github.com/numerique-gouv/ami-app-ios/pull/93)
- Correction de messages de log incorrects sur les pages partenaires.
- Amélioration de la lisibilité du code et correction de typos.
- Mise à jour du titre de navigation AMI pour le long press du bouton retour.
- Suppression de code redondant.
