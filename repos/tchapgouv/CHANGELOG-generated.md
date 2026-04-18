# Synthèse d'activité : tchapgouv (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des améliorations continues sur les applications Tchap, tant sur le web que sur mobile (Android et iOS), ainsi que sur l'infrastructure sous-jacente. L'accent a été mis sur l'amélioration de la sécurité (désactivation des salons non chiffrés sur iOS, verrouillage de comptes via le MAS), l'expérience utilisateur (arrondi des boutons sur le web, gestion des liens profonds sur desktop, amélioration de la vérification d'appareil sur Android) et la stabilité (corrections de bugs, mises à jour de dépendances). Plusieurs dépôts ont bénéficié de refactorisations et d'optimisations techniques pour faciliter la maintenance et le déploiement.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité de la plateforme :

- Désactivation des salons privés non chiffrés sur [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour une meilleure protection des conversations.
- Possibilité de verrouiller le statut d'un utilisateur via le service d'authentification Matrix (MAS) sur [synapse](/repos/tchapgouv/synapse).
- Suppression de la création de comptes hérités sans passer par le MAS sur [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).
- Masquage du bouton de connexion par QR code sur l'écran d'accueil de [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour limiter les risques potentiels.

## Autres changements notables
- Renommage du projet "TCHAP" en "element-call-tchap" sur [element-call](/repos/tchapgouv/element-call), marquant une évolution de l'identité du projet.
- Mise à jour du SDK Matrix Rust sur [matrix-rust-components-swift](/repos/tchapgouv/matrix-rust-components-swift) et [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour bénéficier des dernières corrections et améliorations.
- Optimisation du cache MAS et de la gestion des requêtes sur [synapse](/repos/tchapgouv/synapse) pour améliorer les performances.
- Migration des dépendances de développement vers des groupes de dépendances PEP 735 sur [synapse](/repos/tchapgouv/synapse).
- Intégration d'une version spécifique de `element-call` pour supporter l'Open Finance sur [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).

## Dépôts les plus actifs
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Nombreuses corrections de bugs et améliorations de l'interface utilisateur, notamment concernant les salons privés et les notifications.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Améliorations significatives de l'expérience utilisateur et corrections de bugs, avec une mise à jour vers la dernière version d'Element.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de la sécurité, corrections de bugs et refactorisation du code pour une meilleure maintenabilité.
- [synapse](/repos/tchapgouv/synapse) : Améliorations de la gestion des utilisateurs, optimisations des performances et préparation de la version 1.150.0.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) et [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap) : Améliorations des tests d'authentification et renforcement de la sécurité du processus d'authentification.
