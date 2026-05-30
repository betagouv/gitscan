# Synthèse d'activité : tchapgouv (du 20 mars 2026 au 10 mai 2026)

## Résumé de l'activité
Au cours des dernières semaines, l'organisation tchapgouv a concentré ses efforts sur l'amélioration de la sécurité, de l'expérience utilisateur et de la stabilité de ses différentes applications et services. Des fonctionnalités importantes ont été ajoutées, comme l'expiration des comptes utilisateurs et la désactivation des captures d'écran sur Android, ainsi que des améliorations de l'authentification et de la gestion des accès.  L'organisation a également continué à optimiser ses processus de développement et de publication, avec des mises à jour de dépendances et des corrections de bugs dans plusieurs dépôts, notamment [tchap-x-android](/repos/tchapgouv/tchap-x-android), [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) et [tchap-desktop](/repos/tchapgouv/tchap-desktop).

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Correction d'une vulnérabilité lors de l'ouverture de fichiers téléchargés dans [tchap-desktop](/repos/tchapgouv/tchap-desktop).
- Désactivation des captures d'écran dans [tchap-x-android](/repos/tchapgouv/tchap-x-android) pour une confidentialité accrue.
- Mise à jour de dépendances critiques dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités (rustls-webpki, opa-wasm, wasmtime).
- Amélioration des vérifications de sécurité lors de l'invitation d'utilisateurs externes dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).

## Autres changements notables
- Renommage de "TCHAP" en "element-call-tchap" dans [element-call](/repos/tchapgouv/element-call).
- Suppression de la création de comptes hérités sans passer par le service d'authentification Matrix (MAS) dans [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).
- Refonte de l'authentification avec un pré-check par email dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Suppression du code obsolète lié à l'ancienne fonctionnalité MAS dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Ajout d'un répertoire utilisateur basique dans [synapse](/repos/tchapgouv/synapse).

## Dépôts les plus actifs
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Amélioration de l'invitation d'utilisateurs, implémentation d'une liste rouge, déploiement des appels groupés et refonte de l'authentification.
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Corrections de sécurité, amélioration de la gestion des liens profonds et optimisation des versions.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Ajout de l'expiration de compte, désactivation des captures d'écran et renommage de l'application en "Tchap".
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de l'expérience administrateur, correction de bugs et mise à jour des dépendances.
- [synapse](/repos/tchapgouv/synapse) : Introduction d'un répertoire utilisateur et activation de l'expiration des comptes.
