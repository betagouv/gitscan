# Synthèse d'activité : numerique-gouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv s'est concentrée sur l'amélioration de l'expérience utilisateur des applications Ami (Android et iOS) avec des fonctionnalités comme l'ouverture directe des notifications et une meilleure gestion de l'authentification FranceConnect. Des efforts importants ont également été déployés pour renforcer la sécurité, notamment sur [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [francetransfert](/repos/numerique-gouv/francetransfert), et pour améliorer l'accessibilité et l'internationalisation de [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1). Enfin, des optimisations et corrections de bugs ont été apportées à plusieurs projets, notamment [b3desk](/repos/numerique-gouv/b3desk) et [django-dsfr](/repos/numerique-gouv/django-dsfr).

## Sécurité
Plusieurs changements liés à la sécurité ont été apportés :
- Correction d'une vulnérabilité potentielle concernant l'URL du secteur dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Restriction des types de fichiers autorisés dans [francetransfert](/repos/numerique-gouv/francetransfert) pour bloquer les fichiers HTML et HTM.

## Autres changements notables
- Mise à jour du Design System FR (DSFR) vers la version 1.14.4 dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Mise en place d'un déploiement en un clic sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).
- Suppression de fonctionnalités obsolètes (synchronisation Notion, Makefile) dans [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1).
- Internationalisation des formulaires et menus dans [sites-faciles](/repos/numerique-gouv/sites-faciles).

## Dépôts les plus actifs
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Amélioration de l'authentification FranceConnect, gestion des notifications et adoption du Design System FR.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Ajout de l'ouverture directe de la page de notifications et amélioration de la navigation.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Gestion des zones géographiques pour les vacances scolaires et amélioration de la sécurité.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Internationalisation de la plateforme et déploiement simplifié sur Scalingo.
- [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Amélioration de l'internationalisation, gestion des sitemaps et suppression de fonctionnalités obsolètes.
