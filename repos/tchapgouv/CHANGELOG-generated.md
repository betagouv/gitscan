# Synthèse d'activité : tchapgouv (du 23 mars 2026 au 7 mai 2026)

## Résumé de l'activité
Au cours des dernières semaines, l'organisation tchapgouv a concentré ses efforts sur l'amélioration de la sécurité, la correction de bugs et l'optimisation de l'expérience utilisateur. Des améliorations significatives ont été apportées à l'application Android (renommée simplement "Tchap" et avec un nouveau processus de release), à l'authentification (avec une meilleure gestion des utilisateurs et des liens profonds) et aux appels (avec une transition de nommage et des corrections de compatibilité).  L'accent a également été mis sur la préparation des releases et la modernisation des outils de développement, notamment avec l'intégration de npm et la mise à jour de dépendances critiques.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Correction d'une vulnérabilité lors de l'ouverture de fichiers téléchargés.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Mise à jour de dépendances critiques (rustls-webpki, opa-wasm, wasmtime) pour corriger des vulnérabilités.

## Autres changements notables
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : L'application a été renommée de "Tchap X" à "Tchap" et un nouveau processus de release a été mis en place.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Suppression du code obsolète lié à l'ancienne fonctionnalité MAS et refonte de l'authentification.
- [element-call](/repos/tchapgouv/element-call) : Renommage du projet en "element-call-tchap" et ajustements de l'environnement CI/CD.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Refonte de la construction de la configuration de MAS avec des templates Jinja2.

## Dépôts les plus actifs
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Renommage de l'application et mise en place d'un nouveau processus de release.
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Améliorations de sécurité, gestion des liens profonds et préparation des releases.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Amélioration de l'invitation d'utilisateurs, implémentation d'une liste rouge et déploiement progressif des appels groupés.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de l'expérience administrateur et correction de bugs liés à l'intégration avec le serveur d'identité.
- [tchap-ios](/repos/tchapgouv/tchap-ios) : Corrections de bugs et améliorations de la compatibilité avec les dernières versions d'iOS.
