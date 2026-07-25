# Synthèse d'activité : tchapgouv (du 2026-04-23 au 2026-07-27)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses différentes applications et composants. Des mises à jour de certificats et de dépendances ont été effectuées pour renforcer la sécurité, notamment sur [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) et [tchap-android](/repos/tchapgouv/tchap-android). Des fonctionnalités ont été ajoutées, comme les visioconférences sur [tchap-x-android](/repos/tchapgouv/tchap-x-android) et la gestion des comptes utilisateurs sur [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service). L'équipe a également travaillé sur l'amélioration des tests et de l'infrastructure de build pour assurer une meilleure qualité et un déploiement plus facile.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Mise à jour des certificats SSL/TLS sur [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour garantir la sécurité des communications.
- Restriction des domaines autorisés sur [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour une meilleure sécurité.
- Ajout de la certification Harica sur [tchap-android](/repos/tchapgouv/tchap-android) pour renforcer la sécurité.
- Correction du fingerprint du certificat SHA256 pour Tchap X sur [tchap-android](/repos/tchapgouv/tchap-android) pour une meilleure compatibilité avec F-Droid.
- Mise à jour de `rustls-webpki` et `wasmtime` sur [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités de sécurité.
- Suppression d'un token npm dans le workflow CI/CD de [element-call](/repos/tchapgouv/element-call) pour renforcer la sécurité.

## Autres changements notables
- Refactorisation et optimisation du code sur [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright).
- Mise à jour de l'intégration Docker sur [tchap-docker-integration](/repos/tchapgouv/tchap-docker-integration) pour simplifier la configuration.
- Mise à jour de la version Element sur [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Amélioration de la gestion des comptes utilisateurs sur [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).
- Refonte de la construction de la configuration de MAS sur [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).
- Ajout de tests pour la réactivation silencieuse de compte sur [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de l'expérience utilisateur et corrections de bugs, notamment concernant la gestion des clés et la création de salles.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Ajout de la commande `/visio` pour les visioconférences et améliorations de la sécurité.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de bugs et améliorations de la stabilité, notamment concernant les appels et l'intégration avec Scalingo.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de la gestion des utilisateurs et de la sécurité.
- [synapse](/repos/tchapgouv/synapse) : Correction d'un bug concernant la réactivation des comptes utilisateurs.
- [matrix-admin-bot](/repos/tchapgouv/matrix-admin-bot) : Ajout de nouvelles commandes pour la gestion des utilisateurs et l'envoi de notifications.
