## Changelog : tchap-x-ios (30 derniers jours, au 22 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la stabilité et à l'expérience utilisateur de Tchap X iOS. Les principales évolutions concernent la gestion des salles privées non chiffrées, la correction de bugs liés à l'authentification et à l'affichage des messages, ainsi que des mises à jour de l'interface utilisateur pour une meilleure cohérence visuelle. Des optimisations de performance et des corrections de tests ont également été intégrées.

### Évolutions fonctionnelles
- **Salles privées non chiffrées:** Activation de la fonctionnalité de salles privées non chiffrées en production, via un flag dans les paramètres avancés. [#341](https://github.com/tchapgouv/tchap-x-ios/pull/341)
- **Authentification:** Correction d'un problème lié à l'expiration du compte lors de l'authentification. [#344](https://github.com/tchapgouv/tchap-x-ios/issues/344)
- **Cache:** Ajout d'une option pour effacer le cache de l'application dans les paramètres avancés. [#348](https://github.com/tchapgouv/tchap-x-ios/issues/348)
- **Images optimisées:** Amélioration de la résolution des images optimisées. [#350](https://github.com/tchapgouv/tchap-x-ios/issues/350)
- **Gestion des pièces jointes:** Correction d'un problème empêchant la reconnaissance des captures d'écran iOS glissées dans l'application.
- **Partage de messages:** Possibilité de transférer le même message à plusieurs salles simultanément.
- **Appels:** Correction d'un problème d'état des appels entrants.
- **Connexion Tchap Classic:** Intégration de la connexion avec Tchap Classic pour l'authentification automatique.
- **MapLibre:** Utilisation de l'URL de tuiles MapLibre à partir de well-known si disponible. [#5633](https://github.com/tchapgouv/tchap-x-ios/issues/5633)

### Évolutions techniques
- **Mise à jour du SDK Rust:** Mise à jour du SDK Rust vers la version 26.06.03 et 26.06.18.
- **Refactoring OIDC/OAuth:** Correction d'un refactoring lié à l'authentification OIDC vers OAuth.
- **Compound Design System:** Mise à jour de la librairie Compound Design System vers la version 10.2.0 et 10.2.1.
- **XcodeGen:** Mise à jour de XcodeGen.
- **Tests:** Amélioration et correction de tests unitaires et d'instantanés.
- **Mocks:** Refonte des mocks pour les tests d'interface utilisateur, avec utilisation de Compound pour les icônes.
- **CI/CD:** Mise à jour des actions CI/CD (actions/stale action et codecov/codecov-action).
- **SwiftFormat:** Intégration de SwiftFormat pour le formatage du code.

### Autres changements
- **Documentation:** Mise à jour de la documentation pour l'ajout de la section étiquette dans le guide de contribution. [#5625](https://github.com/tchapgouv/tchap-x-ios/issues/5625)
- **Traduction:** Mise à jour des traductions.
- **Corrections de conflits:** Résolution de conflits de fusion lors de l'intégration de branches.
- **Améliorations UI:** Ajustements de l'interface utilisateur pour une meilleure cohérence visuelle (icônes, espacements, ordre des sections). [#5653](https://github.com/tchapgouv/tchap-x-ios/issues/5653), [#5665](https://github.com/tchapgouv/tchap-x-ios/issues/5665), [#5680](https://github.com/tchapgouv/tchap-x-ios/issues/5680), [#5691](https://github.com/tchapgouv/tchap-x-ios/issues/5691), [#5696](https://github.com/tchapgouv/tchap-x-ios/issues/5696)
- **Correction d'un bug d'affichage:** Correction d'un problème d'affichage lié au chevauchement de l'état vide et de la bannière.
- **Correction d'un bug d'affichage:** Correction d'un problème d'affichage lié au changement d'état du timestamp.
- **Suppression d'un flag de fonctionnalité:** Suppression du flag de fonctionnalité pour les salles privées non chiffrées.
- **Désactivation d'un abonnement:** Désactivation d'un abonnement causant une boucle de nouvelle tentative infinie.
