# Synthèse d'activité : numerique-gouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv a été marquée par des améliorations significatives sur plusieurs de ses applications mobiles ([ami-app-android](/repos/numerique-gouv/ami-app-android), [ami-app-ios](/repos/numerique-gouv/ami-app-ios)), notamment en termes d'expérience utilisateur avec l'intégration de FranceConnect, la gestion des notifications push et l'adoption du Design System FR.  Des efforts importants ont également été consacrés à l'amélioration de la sécurité et de la maintenabilité de plusieurs projets, comme [francetransfert](/repos/numerique-gouv/francetransfert) et [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), avec des migrations vers des technologies plus modernes et des corrections de vulnérabilités. Enfin, des améliorations d'accessibilité et de gestion de contenu ont été apportées à [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) et [sites-faciles](/repos/numerique-gouv/sites-faciles).

## Sécurité
- Ajout de types de fichiers HTML et HTM à la liste noire dans [francetransfert](/repos/numerique-gouv/francetransfert) pour renforcer la sécurité des transferts.
- Mise à jour de l'image de base Keycloak dans [dockerfiles](/repos/numerique-gouv/dockerfiles) pour bénéficier des dernières corrections de sécurité.

## Autres changements notables
- Migration majeure de [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) de Litestar vers Django pour une meilleure maintenabilité et évolutivité.
- Suppression de la synchronisation Notion et du Makefile dans [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) et [sites-faciles](/repos/numerique-gouv/sites-faciles) pour simplifier la maintenance.
- Intégration de ProConnection pour l'authentification dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

## Dépôts les plus actifs
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Amélioration de l'authentification FranceConnect, gestion des notifications push et adoption du Design System FR.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Ajout d'un écran d'onboarding, réactivation de la gestion des liens "mailto" et amélioration de la gestion des notifications.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Améliorations de l'internationalisation, de la gestion des menus et corrections de bugs.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Migration vers Django et intégration de ProConnection pour l'authentification.
