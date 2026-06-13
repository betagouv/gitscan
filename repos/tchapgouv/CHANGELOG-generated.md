# Synthèse d'activité : tchapgouv (du 20 avril 2026 au 28 juin 2026)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses applications. Des fonctionnalités importantes ont été ajoutées, comme la possibilité de créer des salons privés non chiffrés dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) et la gestion de l'expiration des comptes utilisateurs via MAS dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service). Des efforts significatifs ont également été déployés pour améliorer les tests automatisés, notamment avec [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright), et pour optimiser les processus de build et de publication.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité lors de l'ouverture de fichiers téléchargés dans [tchap-desktop](/repos/tchapgouv/tchap-desktop).
- Mise à jour de dépendances critiques dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) (rustls-webpki, opa-wasm, wasmtime) pour corriger des vulnérabilités.

## Autres changements notables
- Refonte de la gestion des règles d'accès aux salles avec la possibilité de définir la visibilité (publique/privée) dans [synapse-room-access-rules](/repos/tchapgouv/synapse-room-access-rules).
- Migration du projet [element-call](/repos/tchapgouv/element-call) de "TCHAP" à "element-call-tchap" avec des ajustements de CI/CD.
- Amélioration de la gestion des liens profonds (deep links) dans [tchap-desktop](/repos/tchapgouv/tchap-desktop).
- Introduction d'un répertoire utilisateur basique dans [synapse](/repos/tchapgouv/synapse) pour une meilleure gestion des utilisateurs.

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Ajout de salons privés non chiffrés, gestion des comptes expirés et optimisations diverses.
- [tchap-android](/repos/tchapgouv/tchap-x-android) : Amélioration de l'interface utilisateur, ajout de la lecture MIDI et suppression de fonctionnalités obsolètes.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections du flux d'invitation externe, réactivation de la liste rouge et ajout de la mise à jour automatique.
- [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) : Ajout et amélioration de nombreux tests d'intégration et d'authentification.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Améliorations de la gestion des utilisateurs, corrections de bugs et mises à jour de sécurité.
