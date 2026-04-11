# Synthèse d'activité : numerique-gouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv se concentre sur l'amélioration de l'expérience utilisateur de ses applications mobiles [ami-app-android](/repos/numerique-gouv/ami-app-android) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios), notamment en facilitant l'authentification via FranceConnect et l'accès aux notifications. Des efforts importants ont également été déployés pour moderniser l'infrastructure de [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) avec une migration vers Django et l'ajout de websockets pour des notifications en temps réel. Plusieurs projets ont bénéficié d'améliorations de sécurité, d'accessibilité et de maintenabilité, comme [sites-faciles](/repos/numerique-gouv/sites-faciles) et [django-dsfr](/repos/numerique-gouv/django-dsfr).

## Sécurité
- Correction d'un crash potentiel au lancement de [django-dsfr](/repos/numerique-gouv/django-dsfr) si l'extension Markdown n'est pas activée.
- Ajout d'une liste noire pour le type de fichier HTML dans [francetransfert](/repos/numerique-gouv/francetransfert) afin d'améliorer la sécurité.
- Acceptation des certificats auto-signés uniquement en mode DEBUG dans [ami-app-ios](/repos/numerique-gouv/ami-app-ios) pour une meilleure sécurité en production.

## Autres changements notables
- Migration majeure de [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) vers Django, remplaçant l'ancien framework Litestar.
- Implémentation de websockets pour la gestion des notifications en temps réel dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Suppression de la synchronisation Notion et du Makefile dans [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) pour simplifier la maintenance.

## Dépôts les plus actifs
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Amélioration de l'authentification FranceConnect, gestion des notifications push et adoption du Design System FR.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Correction de l'ouverture des notifications push et optimisation de la structure des vues.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Migration vers Django, implémentation de websockets et ajout de fonctionnalités de gestion des agents et des notifications.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Amélioration de l'internationalisation, gestion des menus et correction de bugs.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Corrections de bugs et préparation de nouvelles versions avec des améliorations de stabilité et de sécurité.
