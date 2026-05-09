# Synthèse d'activité : tchapgouv (du 23 mars 2026 au 10 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation tchapgouv s'est concentrée sur l'amélioration de la sécurité, de l'accessibilité et de l'expérience utilisateur de ses applications et services. Des correctifs de sécurité critiques ont été déployés pour tchap-web-v4, et des améliorations significatives ont été apportées aux applications mobiles (iOS et Android) avec l'ajout de nouvelles fonctionnalités et la correction de bugs. L'authentification et la gestion des utilisateurs ont également été renforcées grâce à des mises à jour de matrix-authentication-service et de ses composants associés. Plusieurs dépôts ont bénéficié d'améliorations techniques, notamment des mises à jour de dépendances et des optimisations de configuration.

## Sécurité
Plusieurs changements liés à la sécurité ont été implémentés :
- Correction d'une faille de sécurité critique concernant l'ouverture de fichiers dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Mise à jour de `opa-wasm` et `wasmtime` pour corriger des vulnérabilités de sécurité dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).
- Correction d'un bug lié à la réinitialisation des clés de chiffrement dans [tchap-android](/repos/tchapgouv/tchap-android).

## Autres changements notables
- Refonte du flux de connexion/enregistrement dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Renommage de l'application "Tchap X" en "Tchap" dans [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Transition du projet "TCHAP" à "element-call-tchap" dans [element-call](/repos/tchapgouv/element-call).
- Introduction d'un répertoire utilisateur basique dans [synapse](/repos/tchapgouv/synapse).
- Amélioration du contraste des gradients d'informations pour une meilleure accessibilité dans [compound-design-tokens](/repos/tchapgouv/compound-design-tokens).

## Dépôts les plus actifs
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de sécurité, refonte du flux de connexion et ajout de nouvelles fonctionnalités.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Ajout de l'accès par lien aux salons et améliorations de la gestion des espaces.
- [tchap-android](/repos/tchapgouv/tchap-android) : Renommage de l'application, corrections de bugs et améliorations de la sécurité.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de la gestion des utilisateurs et correction de vulnérabilités.
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Corrections de sécurité et amélioration de la gestion des liens profonds.
