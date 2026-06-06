# Synthèse d'activité : tchapgouv (du 2026-03-20 au 2026-06-04)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment concernant la gestion des utilisateurs, l'accès aux salles et l'expérience utilisateur globale. Des efforts importants ont été déployés pour renforcer la sécurité des applications mobiles (iOS et Android) avec des correctifs pour les vulnérabilités et l'amélioration de l'authentification.  Les applications web et desktop bénéficient également d'améliorations en termes de sécurité et de fonctionnalités, comme l'ajout de liens profonds personnalisables et la gestion de la visibilité des salles. Les dépôts [tchap-x-ios](/repos/tchapgouv/tchap-x-ios), [tchap-x-android](/repos/tchapgouv/tchap-x-android) et [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) sont particulièrement actifs.

## Sécurité
Plusieurs changements ont été apportés pour améliorer la sécurité de la plateforme :

- Correction d'une vulnérabilité lors de l'ouverture de fichiers téléchargés dans [tchap-desktop](/repos/tchapgouv/tchap-desktop).
- Amélioration de la sécurité avec un écran d'expiration de compte dans [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Mise à jour de dépendances critiques dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) pour corriger des vulnérabilités (rustls-webpki, opa-wasm, wasmtime).
- Suppression des captures d'écran pour renforcer la confidentialité dans [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Renforcement de la sécurité du processus de création de compte en supprimant la création de comptes hérités sans passer par le MAS dans [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).

## Autres changements notables
- Refonte de l'authentification avec un pré-check par email dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Suppression du code obsolète lié à l'ancienne fonctionnalité MAS dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Mise à jour du SDK Matrix Rust dans plusieurs dépôts ([tchap-x-android](/repos/tchapgouv/tchap-x-android), [matrix-rust-components-swift](/repos/tchapgouv/matrix-rust-components-swift), [matrix-rust-components-kotlin](/repos/tchapgouv/matrix-rust-components-kotlin)).
- Renommage du projet "TCHAP" en "element-call-tchap" dans [element-call](/repos/tchapgouv/element-call).
- Introduction d'un répertoire utilisateur basique dans [synapse](/repos/tchapgouv/synapse).

## Dépôts les plus actifs
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Amélioration de l'expérience utilisateur et de la sécurité avec de nouvelles fonctionnalités et des corrections de bugs.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Ajout de nouvelles fonctionnalités (partage de position en direct) et renforcement de la sécurité.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Amélioration de l'expérience utilisateur et correction de bugs.
- [synapse](/repos/tchapgouv/synapse) : Amélioration de la gestion des utilisateurs et de la configuration.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de la sécurité et de l'expérience administrateur.
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Corrections de bugs et améliorations de la sécurité.
