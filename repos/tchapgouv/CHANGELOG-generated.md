# Synthèse d'activité : tchapgouv (du 04/07 au 29/07)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'optimisation des performances de ses différents composants. Des améliorations significatives ont été apportées à l'authentification, avec l'ajout de certifications et la correction de vulnérabilités. Les applications mobiles (iOS et Android) ont bénéficié de mises à jour de certificats et de corrections d'interface utilisateur. Des efforts importants ont également été déployés pour améliorer la gestion des accès et des règles dans l'infrastructure Matrix sous-jacente, notamment via les dépôts `synapse`, `synapse-room-access-rules` et `matrix-authentication-service`. Enfin, des améliorations de l'expérience utilisateur ont été apportées, notamment avec l'ajout de commandes de visioconférence dans l'application Android et des améliorations de l'invitation dans l'application web.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :

- Mise à jour des certificats SSL/TLS dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour garantir la sécurité des communications.
- Ajout de la certification Harica dans [tchap-android](/repos/tchapgouv/tchap-android) pour renforcer la sécurité.
- Correction du fingerprint du certificat SHA256 pour Tchap X dans [tchap-android](/repos/tchapgouv/tchap-android) pour réactiver la vérification sur F-Droid.
- Mise à jour de `rustls-webpki` et `wasmtime` dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités de sécurité.
- Suppression du token npm dans le workflow CI/CD de [element-call](/repos/tchapgouv/element-call) pour renforcer la sécurité.

## Autres changements notables
- Refactorisation et optimisation du code dans [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright).
- Mise à jour vers la version Element 1.12.17 dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Intégration de code Rust pour la sérialisation d'événements et l'accès à la base de données dans [synapse](/repos/tchapgouv/synapse), améliorant les performances.
- Mise à jour de Gradle dans [matrix-rust-components-kotlin](/repos/tchapgouv/matrix-rust-components-kotlin).
- Ajout d'une authentification npm dans le workflow de CI/CD de [compound-web](/repos/tchapgouv/compound-web) pour faciliter les publications de paquets.

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de l'expérience utilisateur et mises à jour de sécurité.
- [tchap-android](/repos/tchapgouv/tchap-android) : Ajout de la certification Harica et corrections de certificats.
- [synapse](/repos/tchapgouv/synapse) : Optimisation des performances et amélioration de la gestion des règles d'accès.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de bugs et mise à jour de la version d'Element.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de l'expérience administrateur et corrections de sécurité.
