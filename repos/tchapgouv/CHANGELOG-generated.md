# Synthèse d'activité : tchapgouv (du 04/04 au 20/07/2026)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses applications. Des mises à jour de certificats et des corrections de vulnérabilités ont été déployées sur plusieurs dépôts, notamment [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) et [tchap-android](/repos/tchapgouv/tchap-android).  Des améliorations significatives ont également été apportées à la gestion des accès et des utilisateurs, en particulier via les dépôts [synapse](/repos/tchapgouv/synapse) et [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).  Plusieurs dépôts ont bénéficié de mises à jour de dépendances et de refactorisations pour améliorer la performance et la maintenabilité du code.

## Sécurité
Plusieurs changements liés à la sécurité ont été implémentés :

- Mise à jour des certificats Let's Encrypt et ajout d'un nouveau certificat Harica sur [tchap-x-ios](/repos/tchapgouv/tchap-x-ios).
- Mise à jour des certificats de juillet 2026 sur [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Correction du fingerprint du certificat SHA256 pour Tchap X sur [tchap-android](/repos/tchapgouv/tchap-android) pour une meilleure compatibilité avec F-Droid.
- Mise à jour de `rustls-webpki` et `wasmtime` sur [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités.
- Suppression d'un token npm dans le workflow CI/CD de [element-call](/repos/tchapgouv/element-call).

## Autres changements notables
- Refactorisation et optimisation du code sur [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright).
- Mise à jour de la version d'Element sur [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Mise à jour de Gradle et des dépendances sur [matrix-rust-components-kotlin](/repos/tchapgouv/matrix-rust-components-kotlin).
- Amélioration de la gestion des utilisateurs et des accès sur [synapse](/repos/tchapgouv/synapse) avec l'intégration de nouvelles fonctionnalités liées à l'expiration des comptes et aux règles d'accès aux salles.
- Ajout de la gestion de la visibilité des salles sur [synapse-room-access-rules](/repos/tchapgouv/synapse-room-access-rules).

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Amélioration de l'expérience utilisateur avec des corrections et des nouvelles fonctionnalités pour les salles privées chiffrées.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Corrections de compatibilité, améliorations de la connexion et activation des salons privés non-chiffrés.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de bugs et améliorations de la stabilité, notamment concernant les appels et l'intégration avec Scalingo.
- [synapse](/repos/tchapgouv/synapse) : Améliorations de la gestion des utilisateurs, des accès et de la performance du serveur.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de l'expérience administrateur et corrections de bugs liés à l'authentification.
- [tchap-android](/repos/tchapgouv/tchap-android) : Ajout de la certification Harica et correction du fingerprint du certificat pour F-Droid.
