# Synthèse d'activité : tchapgouv (du 2026-06-20 au 2026-07-08)

## Résumé de l'activité
La période récente a été marquée par des améliorations continues de la sécurité, de la stabilité et de l'expérience utilisateur des différentes applications Tchap. Les efforts se sont concentrés sur l'amélioration de l'authentification, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment dans les applications iOS et Android. L'infrastructure sous-jacente, notamment Synapse et les services associés, a également bénéficié d'améliorations en termes de gestion des accès, de performance et de sécurité. Les dépôts [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) et [tchap-x-android](/repos/tchapgouv/tchap-x-android) ont reçu des mises à jour significatives pour les utilisateurs finaux.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité de la plateforme :
- Mise à jour du certificat de l'application [tchap-ios](/repos/tchapgouv/tchap-ios) pour une meilleure sécurité.
- Mise à jour des signatures d'applications autorisées pour les variantes Tchap X [tchap-android](/repos/tchapgouv/tchap-android).
- Mise à jour de `rustls-webpki` et `wasmtime` dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités.
- Ajout de l'autorité de certification Harica [tchap-android](/repos/tchapgouv/tchap-android).
- Suppression du token npm dans le workflow CI/CD de [element-call](/repos/tchapgouv/element-call).

## Autres changements notables
- Intégration de nouvelles fonctionnalités liées à l'expiration des comptes et aux règles d'accès aux salles dans [synapse](/repos/tchapgouv/synapse).
- Refactorisation de la structure des fichiers et ajout de documentation Docker pour [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).
- Mise à jour du SDK Rust Matrix dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) et [matrix-rust-components-kotlin](/repos/tchapgouv/matrix-rust-components-kotlin).
- Amélioration de la gestion des tests et de la couverture des tests dans [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright).

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Intégration des dernières améliorations d'ElementX, corrections de bugs et ajout de fonctionnalités.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Améliorations de l'expérience utilisateur, corrections de bugs et ajout de nouvelles fonctionnalités.
- [synapse](/repos/tchapgouv/synapse) : Améliorations de la gestion des utilisateurs, des accès et de la performance du serveur.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de bugs et améliorations de la stabilité.
- [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) : Amélioration de la couverture des tests et refactoring du code.
