# Synthèse d'activité : tchapgouv (du 2024-03-20 au 2024-05-13)

## Résumé de l'activité
La période a été marquée par des améliorations significatives sur l'ensemble des applications Tchap (iOS, Android, Web, Desktop) avec un focus sur la sécurité, la stabilité et l'expérience utilisateur.  Des correctifs de sécurité critiques ont été déployés sur le web, et des améliorations notables ont été apportées à l'authentification et à la gestion des comptes. Les applications mobiles bénéficient d'une meilleure gestion des liens profonds, d'une réinitialisation d'identité plus fiable et d'une harmonisation de la terminologie.  Des efforts importants ont également été consacrés à la modernisation de l'infrastructure de développement et de déploiement.

## Sécurité
- Correction d'une faille de sécurité critique concernant l'ouverture de fichiers dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Amélioration de la sécurité des cookies dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).
- Suppression de la création de comptes hérités sans MAS dans [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap) et [tchap-e2e-playwright](/repos/tchapgouv/tchap-e2e-playwright).

## Autres changements notables
- Renommage de "Tchap X" en "Tchap" sur Android [tchap-x-android](/repos/tchapgouv/tchap-x-android).
- Refonte du flux de connexion/enregistrement dans [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Migration du projet "TCHAP" vers "element-call-tchap" [element-call](/repos/tchapgouv/element-call).
- Activation de l'expiration des comptes avec MAS [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service).
- Mise à jour des SDK Matrix Rust et Kotlin dans plusieurs dépôts.

## Dépôts les plus actifs
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de sécurité, ajout de thème haute contraste et amélioration des appels groupés.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Renommage de l'application et améliorations de l'interface utilisateur.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Amélioration de la gestion des espaces et des salons, notamment l'accès par lien.
- [tchap-desktop](/repos/tchapgouv/tchap-desktop) : Amélioration de la gestion des liens profonds et des notifications.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Améliorations de la compatibilité, de la sécurité et de la gestion des comptes.
