# Synthèse d'activité : tchapgouv (du 13 avril 2026 au 23 avril 2026)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de l'expérience utilisateur et la sécurité de la plateforme. L'application Android [tchap-x-android](/repos/tchapgouv/tchap-x-android) a bénéficié de nombreuses corrections et améliorations, notamment dans la gestion des espaces et des salons, ainsi que des ajustements d'interface.  tchap-web-v4 [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) a introduit la possibilité de créer des salons privés non chiffrés et a amélioré la gestion des appels groupés. Des optimisations de performance et des corrections de bugs ont également été apportées à Synapse [synapse](/repos/tchapgouv/synapse) et tchap-desktop [tchap-desktop](/repos/tchapgouv/tchap-desktop).

## Sécurité
- Activation de l'expiration des comptes via MAS dans [synapse](/repos/tchapgouv/synapse).
- Ajout de la possibilité de créer des salons privés non chiffrés dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4), avec un affichage clair de leur statut non chiffré.
- Désactivation du certificat pinning pour les fonds de cartes dans [tchap-x-android](/repos/tchapgouv/tchap-x-android) sur l'environnement de développement.

## Autres changements notables
- Mise à jour du SDK Matrix Rust dans [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Refonte du routage et suppression du code MAS obsolète dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Mise en cache de l'introspection MAS dans [synapse](/repos/tchapgouv/synapse) pour améliorer les performances.
- Correction du comportement de l'application sur macOS concernant l'ouverture des fenêtres depuis le dock dans [tchap-desktop](/repos/tchapgouv/tchap-desktop).

## Dépôts les plus actifs
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Amélioration significative de l'application Android avec de nombreuses corrections de bugs et améliorations de l'interface utilisateur.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Ajout de nouvelles fonctionnalités et améliorations de la sécurité pour la version web de Tchap.
- [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) : Amélioration des tests d'authentification et de création de salles.
- [synapse](/repos/tchapgouv/synapse) : Optimisations de performance et corrections de bugs pour le serveur Matrix.
