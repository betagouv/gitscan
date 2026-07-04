# Synthèse d'activité : tchapgouv (du 20 mai 2026 au 26 juin 2026)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités pour les applications iOS, Android et web. Des efforts importants ont été déployés pour améliorer l'expérience utilisateur, notamment en simplifiant la création de salles privées chiffrées, en optimisant l'affichage des fichiers et en améliorant la gestion des invitations.  Des mises à jour significatives ont également été apportées à l'infrastructure serveur, notamment au niveau de l'authentification et de la gestion des accès, avec l'introduction de nouvelles fonctionnalités et la correction de vulnérabilités. Les dépôts [tchap-x-ios](/repos/tchapgouv/tchap-x-ios), [tchap-x-android](/repos/tchapgouv/tchap-x-android) et [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) ont été particulièrement actifs.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :
- Correction de vulnérabilités mineures sur la version desktop de [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Mise à jour de dépendances critiques dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) (rustls-webpki, opa-wasm, wasmtime) pour corriger des vulnérabilités.
- Suppression d'un token npm dans le workflow CI/CD de [element-call](/repos/tchapgouv/element-call) pour renforcer la sécurité.

## Autres changements notables
- Intégration de nouvelles versions d'EC (Element Client) dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) pour bénéficier des dernières améliorations et corrections.
- Refactorisation de l'authentification OIDC vers OAuth dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios).
- Amélioration de la gestion des utilisateurs et des accès avec l'introduction de l'expiration des comptes et des règles d'accès aux salles dans [synapse](/repos/tchapgouv/synapse) et [synapse-room-access-rules](/repos/tchapgouv/synapse-room-access-rules).
- Mise à jour des SDK Rust Matrix dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios), [tchap-x-android](/repos/tchapgouv/tchap-x-android) et [matrix-rust-components-kotlin](/repos/tchapgouv/matrix-rust-components-kotlin).

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Amélioration de l'expérience utilisateur avec de nouvelles fonctionnalités et corrections de bugs.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Ajout de badges pour les salles privées chiffrées et amélioration de l'affichage des fichiers.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Améliorations de la sécurité, corrections de bugs et intégration de la dernière version d'EC.
- [synapse](/repos/tchapgouv/synapse) : Amélioration de la gestion des accès aux salles et de l'expiration des comptes.
- [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) : Ajout et amélioration des tests d'intégration et d'authentification.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de la gestion des utilisateurs et correction de vulnérabilités.
