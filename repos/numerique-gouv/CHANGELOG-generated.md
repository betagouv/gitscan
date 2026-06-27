# Synthèse d'activité : numerique-gouv (du 2024-05-20 au 2024-06-20)

## Résumé de l'activité
L'organisation numerique-gouv a connu une période d'activité soutenue, avec des améliorations significatives sur plusieurs de ses dépôts. Les efforts se sont concentrés sur l'internationalisation des plateformes [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), permettant une meilleure accessibilité pour un public plus large.  Des améliorations importantes ont également été apportées à la sécurité et à la robustesse de services comme [sites-conformes](/repos/numerique-gouv/sites-conformes) avec l'intégration de Sentry et l'ajout de stockage des médias en PostgreSQL.  Enfin, des mises à jour ont été déployées pour améliorer l'expérience utilisateur sur les applications mobiles [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android), ainsi que pour optimiser les processus de développement et de déploiement.

## Sécurité
- Intégration de Sentry pour la surveillance et la gestion des erreurs sur [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Mise à jour de l'image de base Keycloak dans [dockerfiles](/repos/numerique-gouv/dockerfiles) pour bénéficier des dernières corrections de sécurité.

## Autres changements notables
- Implémentation de l'authentification via FranceConnect FI sur [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Refactoring de la structure du projet [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) pour une meilleure organisation.
- Automatisation de la publication des releases GitHub sur [b3desk](/repos/numerique-gouv/b3desk).
- Ajout de la possibilité de stocker les médias en PostgreSQL sur [sites-conformes](/repos/numerique-gouv/sites-conformes).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Ajout d'un sélecteur de langue et internationalisation des champs de formulaire pour une meilleure gestion du contenu multilingue.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Amélioration de la robustesse avec l'intégration de Sentry et ajout du stockage des médias en PostgreSQL.
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de la gestion des réunions et des utilisateurs, avec la délégation de gestion et le mapping des informations utilisateur OIDC.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Intégration de FranceConnect FI et amélioration de l'affichage des notifications.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Correction de l'affichage des formulaires DSFR et amélioration du processus de publication des releases.
