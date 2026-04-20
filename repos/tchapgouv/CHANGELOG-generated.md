# Synthèse d'activité : tchapgouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation tchapgouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses applications. Des efforts significatifs ont été déployés pour renforcer la sécurité des communications, notamment en désactivant les salons privés non chiffrés et en améliorant la gestion des identités.  Plusieurs dépôts ont bénéficié de mises à jour de dépendances et de corrections de bugs, notamment [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) et [tchap-x-ios](/repos/tchapgouv/tchap-x-ios), améliorant ainsi la qualité globale de la plateforme.

## Sécurité
Plusieurs changements visent à renforcer la sécurité de la plateforme :

*   Désactivation des salons privés non chiffrés dans [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour une meilleure protection des conversations.
*   Masquage de l'option de connexion par QR code sur l'écran d'accueil de [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) pour réduire les risques potentiels.
*   Suppression de la création de comptes hérités sans passer par le service d'authentification Matrix (MAS) dans [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap).
*   Correction d'un problème de compatibilité sur Firefox avec les appareils utilisant un proxy dans [element-call](/repos/tchapgouv/element-call).

## Autres changements notables
*   **Refactoring et mises à jour d'infrastructure :** [synapse](/repos/tchapgouv/synapse) a bénéficié d'optimisations du cache MAS et de la migration des dépendances de développement vers PEP 735.
*   **Spécification Matrix :** Des ajouts à la spécification Matrix ([matrix-spec](/repos/tchapgouv/matrix-spec)) concernant l'autorisation d'appareil et les serveurs de politiques.
*   **Renommage de dépôt :** Le dépôt [element-call](/repos/tchapgouv/element-call) a été renommé en "element-call-tchap".
*   **Simplification de l'intégration Docker :** [tchap-docker-integration](/repos/tchapgouv/tchap-docker-integration) a été mis à jour pour utiliser une stack complète avec Element et Synapse par défaut.

## Dépôts les plus actifs
*   [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Nombreuses améliorations fonctionnelles et techniques, incluant l'ajout de salons privés non chiffrés et des appels groupés.
*   [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de la sécurité, corrections de bugs et refactorisation du code.
*   [synapse](/repos/tchapgouv/synapse) : Optimisations de performance et préparation de la version 1.150.0.
*   [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap) : Ajout de tests et suppression de la création de comptes hérités.
*   [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Amélioration de l'expérience utilisateur et mises à jour de dépendances.
