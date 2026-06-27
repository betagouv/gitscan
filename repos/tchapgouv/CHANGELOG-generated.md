# Synthèse d'activité : tchapgouv (du 2024-06-07 au 2024-07-07)

## Résumé de l'activité
Au cours des dernières semaines, l'organisation tchapgouv a concentré ses efforts sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses différentes applications. Des fonctionnalités importantes ont été ajoutées, notamment l'activation des salles privées non chiffrées (avec alertes de partage de fichiers) sur les plateformes Android et iOS, ainsi que l'amélioration de l'authentification et de la gestion des comptes. Des corrections de bugs et des optimisations ont également été apportées à plusieurs dépôts, notamment `tchap-web-v4`, `synapse` et `matrix-authentication-service`, pour améliorer la performance et la fiabilité des services. L'ajout de la mise à jour automatique sur tchap-desktop est une amélioration significative pour les utilisateurs.

## Sécurité
Plusieurs améliorations de sécurité ont été implémentées :

*   Correction de vulnérabilités et mise à jour de dépendances critiques dans [tchap-desktop](/repos/tchapgouv/tchap-desktop) et [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).
*   Amélioration de la gestion des certificats Let's Encrypt dans [tchap-x-android](/repos/tchapgouv/tchap-x-android).
*   Corrections de sécurité mineures sur la version desktop de [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
*   Ajout d'un écran d'expiration de compte dans [tchap-x-android](/repos/tchapgouv/tchap-x-android) pour renforcer la sécurité.

## Autres changements notables
*   **Synapse :** Amélioration de la gestion des règles d'accès aux salles et intégration de l'expiration des comptes avec MAS.
*   **tchap-web-v4 :** Réactivation de la "liste rouge" et amélioration du flux d'invitations externes.
*   **tchap-desktop :** Implémentation de la mise à jour automatique et activation de l'installation dans le contexte utilisateur.
*   **matrix-authentication-service :** Amélioration de la gestion des erreurs du serveur d'identité et ajout de la possibilité d'envoyer des notifications à tous les utilisateurs via MAS.
*   **matrix-admin-bot :** Ajout d'une commande `user` pour gérer les utilisateurs et correction de l'affichage du nom et de l'adresse email.

## Dépôts les plus actifs
*   [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Ajout de fonctionnalités et corrections de bugs concernant les salles privées, l'expiration de compte et l'optimisation des images.
*   [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Ajout de fonctionnalités et corrections de bugs concernant les salles privées, les notifications et la gestion des fichiers.
*   [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Amélioration de l'expérience utilisateur et corrections de bugs liés aux invitations externes et à la configuration.
*   [synapse](/repos/tchapgouv/synapse) : Amélioration de la gestion des accès et de l'expiration des comptes.
*   [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de la gestion des utilisateurs et des notifications.
*   [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Ajout de la mise à jour automatique et amélioration de l'installation.
*   [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright) : Ajout de tests d'intégration et refactoring du code.
