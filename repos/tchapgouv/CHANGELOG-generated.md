# Synthèse d'activité : tchapgouv (du 20 avril 2026 au 12 juin 2026)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, de la gestion des utilisateurs et de l'expérience utilisateur globale. Des fonctionnalités importantes ont été ajoutées, comme la création de salles privées non chiffrées ([tchap-x-ios](/repos/tchapgouv/tchap-x-ios)) et la gestion des comptes expirés ([tchap-x-ios](/repos/tchapgouv/tchap-x-ios), [tchap-x-android](/repos/tchapgouv/tchap-x-android)). Des efforts significatifs ont également été déployés pour améliorer la gestion des accès aux salles et l'intégration avec les services d'authentification ([synapse-room-access-rules](/repos/tchapgouv/synapse-room-access-rules), [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service)). L'organisation a également continué à investir dans l'automatisation des tests et l'amélioration de l'infrastructure de développement.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité lors de l'ouverture de fichiers téléchargés ([tchap-desktop](/repos/tchapgouv/tchap-desktop)).
- Mise à jour de dépendances critiques dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités (rustls-webpki, opa-wasm, wasmtime).
- Correction d'une vulnérabilité de sécurité dans l'ouverture de fichiers téléchargés ([tchap-desktop](/repos/tchapgouv/tchap-desktop)).

## Autres changements notables
- Refactorings importants dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) et [tchap-desktop](/repos/tchapgouv/tchap-desktop) pour améliorer la qualité du code et la maintenabilité.
- Suppression du support d'Android Auto dans [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Mise à jour et simplification de la configuration Docker pour faciliter le déploiement ([tchap-docker-integration](/repos/tchapgouv/tchap-docker-integration)).
- Renommage du projet `TCHAP` en `element-call-tchap` ([element-call](/repos/tchapgouv/element-call)).

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Ajout de nouvelles fonctionnalités et corrections de bugs pour l'application iOS.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Améliorations de l'interface utilisateur et corrections de bugs pour l'application Android.
- [synapse](/repos/tchapgouv/synapse) : Amélioration de la gestion des accès et de l'expiration des comptes.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de bugs et améliorations de la gestion des invitations externes.
- [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) : Développement de tests d'intégration pour assurer la qualité du code.
