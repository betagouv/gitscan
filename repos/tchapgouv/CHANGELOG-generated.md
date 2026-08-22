# Synthèse d'activité : tchapgouv (du 01/07 au 23/07/2026)

## Résumé de l'activité
L'activité de cette période est centrée sur la consolidation de la sécurité et l'amélioration de la performance globale de l'infrastructure. Les efforts majeurs ont porté sur la mise à jour des certificats de sécurité pour les applications mobiles et la correction de vulnérabilités critiques sur le serveur.

Parallèlement, l'expérience utilisateur progresse avec l'introduction de nouvelles fonctionnalités de communication sur Android, une meilleure stabilité de la version Web [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) et des optimisations de l'interface pour une meilleure accessibilité.

## Sécurité
- Correction de vulnérabilités critiques (traversée de chemin et usurpation d'identité) dans [synapse](/repos/tchapgouv/synapse).
- Renforcement de la sécurité des communications via la mise à jour des certificats SSL/TLS et des certificats de confiance (Harica) sur les applications mobiles [tchap-x-ios](/repos/tchapgouv/tchap-x-ios), [tchap-x-android](/repos/tchapgouv/tchap-x-android), [tchap-ios](/repos/tchapgouv/tchap-ios) et [tchap-android](/repos/tchapgouv/tchap-android).
- Sécurisation du service d'authentification et correction de vulnérabilités dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) et [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).
- Protection des identifiants sensibles et suppression de tokens dans [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) et [element-call](/repos/tchapgouv/element-call).

## Autres changements notables
- **Optimisation des performances :** intégration de Rust pour la sérialisation dans [synapse](/repos/tchapgouv/synapse) et mise en place d'un système de limitation de débit (rate limiting) dans [matrix-media-repo](/repos/tchapgouv/matrix-media-repo).
- **Gestion des données et protocoles :** amélioration de l'outil de rétention des messages dans [synapse-room-access-rules](/repos/tchapgouv/synapse-room-access-rules) et mise à jour de la spécification du protocole Matrix dans [matrix-spec](/repos/tchapgouv/matrix-spec).
- **Évolutions fonctionnelles et design :** ajout de la commande de visioconférence `/visio` dans [tchap-x-android](/repos/tchapgouv/tchap-x-android) et amélioration de l'accessibilité des contrastes dans [compound-design-tokens](/repos/tchapgouv/compound-design-tokens).

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de l'expérience utilisateur et mises à jour de sécurité.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Nouvelles fonctionnalités de commande et gestion des certificats.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Stabilisation, corrections de bugs et mises à jour techniques.
- [synapse](/repos/tchapgouv/synapse) : Optimisations de performance majeures et corrections de sécurité critiques.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Évolutions de l'interface administrateur et renforcement de la sécurité.
