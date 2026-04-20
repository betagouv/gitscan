# Synthèse d'activité : numerique-gouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv s'est concentrée sur l'amélioration de l'expérience utilisateur et la modernisation de ses applications. L'application [ami-app-ios](/repos/numerique-gouv/ami-app-ios) bénéficie de nouvelles fonctionnalités comme un écran d'onboarding et la gestion des liens "mailto", tandis que [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) a subi une migration majeure vers Django pour une meilleure maintenabilité. Des améliorations d'accessibilité sont également notables sur la page d'accueil de [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage). Enfin, des efforts de sécurité et d'optimisation sont visibles sur [francetransfert](/repos/numerique-gouv/francetransfert) et [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Sécurité
- [francetransfert](/repos/numerique-gouv/francetransfert) a renforcé sa sécurité en ajoutant des types de fichiers (HTML, HTM) à la liste noire pour prévenir les téléchargements potentiellement dangereux.
- [dockerfiles](/repos/numerique-gouv/dockerfiles) a mis à jour l'image de base Keycloak pour bénéficier des dernières corrections de sécurité.

## Autres changements notables
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) a été migré de Litestar vers Django, une migration majeure visant à améliorer la maintenabilité et l'évolutivité. L'intégration de Sentry permet une meilleure surveillance des erreurs et des performances.
- [b3desk](/repos/numerique-gouv/b3desk) a implémenté la délégation de réunion, une nouvelle fonctionnalité permettant de déléguer la gestion d'une réunion.

## Dépôts les plus actifs
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Amélioration de l'expérience utilisateur avec un nouvel écran d'onboarding et la réactivation de fonctionnalités existantes.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Migration vers Django et intégration de Sentry pour une meilleure gestion et surveillance des notifications.
- [b3desk](/repos/numerique-gouv/b3desk) : Ajout de la fonctionnalité de délégation de réunion et corrections de compatibilité avec Keycloak.
- [francetransfert](/repos/numerique-gouv/francetransfert) : Renforcement de la sécurité et optimisation de l'infrastructure.
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) : Amélioration de l'accessibilité et ajout d'un processus de sélection pour la prise de rendez-vous.
