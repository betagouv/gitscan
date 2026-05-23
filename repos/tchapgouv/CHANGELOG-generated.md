# Synthèse d'activité : tchapgouv (du 28 mars 2026 au 10 mai 2026)

## Résumé de l'activité
Au cours des dernières semaines, l'organisation tchapgouv a concentré ses efforts sur l'amélioration de la sécurité, la correction de bugs et la préparation de nouvelles versions de ses applications. Des améliorations significatives ont été apportées à l'authentification, notamment avec l'intégration de nouvelles fonctionnalités et la correction de vulnérabilités. Les applications mobiles (iOS et Android) ont bénéficié de corrections de bugs et d'améliorations de l'expérience utilisateur, tandis que les composants web et de design ont été mis à jour pour améliorer l'accessibilité et la cohérence visuelle. Le service d'authentification a également été renforcé avec des tests supplémentaires et une suppression de méthodes d'authentification obsolètes.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Correction d'une vulnérabilité lors de l'ouverture de fichiers téléchargés.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Mise à jour de dépendances (rustls-webpki, opa-wasm, wasmtime) pour corriger des vulnérabilités.

## Autres changements notables
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Refonte de l'authentification avec un pré-check par email et implémentation d'une liste rouge configurable. Suppression du code obsolète MAS.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Changement de nom de l'application de "Tchap X" à "Tchap" et préparation pour les releases avec un script dédié.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Amélioration de la gestion des espaces et correction de problèmes liés aux liens d'invitation.
- [element-call](/repos/tchapgouv/element-call) : Renommage du projet et ajustements du CI/CD.
- [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap) : Suppression de la création de comptes hérités sans passer par le MAS.

## Dépôts les plus actifs
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Corrections de bugs, améliorations de la gestion des liens profonds et préparation des releases.
- [tchap-android](/repos/tchapgouv/tchap-android) : Changement de nom de l'application, préparation des releases et corrections de bugs.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Améliorations de l'expérience administrateur, corrections de bugs et mises à jour de sécurité.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Améliorations de la sécurité et de l'authentification, déploiement des appels groupés.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de la gestion des espaces et corrections de bugs.
