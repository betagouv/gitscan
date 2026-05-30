# Synthèse d'activité : numerique-gouv (du 06 mai 2026 au 28 mai 2026)

## Résumé de l'activité
L'activité de l'organisation numerique-gouv au cours des dernières semaines s'est concentrée sur l'amélioration de l'expérience utilisateur et la modernisation des infrastructures. Plusieurs dépôts ont bénéficié d'améliorations d'internationalisation, notamment [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), permettant une meilleure adaptation aux utilisateurs multilingues. Des efforts importants ont également été déployés pour renforcer la sécurité, avec des mises à jour de dépendances et l'intégration de Sentry dans [sites-conformes](/repos/numerique-gouv/sites-conformes). L'ajout de nouvelles fonctionnalités, comme le stockage des médias en base de données dans [sites-conformes](/repos/numerique-gouv/sites-conformes) et l'amélioration de la délégation de réunions dans [b3desk](/repos/numerique-gouv/b3desk), témoignent d'une volonté d'enrichir l'offre et de répondre aux besoins des utilisateurs.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances visant à corriger des vulnérabilités et à améliorer la sécurité globale des applications :
- Mise à jour de `postcss` et `next` dans [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage)
- Mise à jour de plusieurs dépendances dans [django-dsfr](/repos/numerique-gouv/django-dsfr)
- Mise à jour de l'image de base Keycloak dans [dockerfiles](/repos/numerique-gouv/dockerfiles)

## Autres changements notables
- Intégration de Sentry pour la surveillance des erreurs dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Simplification du déploiement sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Refonte de l'architecture frontend dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Amélioration de la gestion des URLs spéciales dans [ami-app-android](/repos/numerique-gouv/ami-app-android).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Ajout d'un sélecteur de langue et internationalisation des champs de formulaire pour une meilleure gestion du contenu multilingue.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Préparation de la version 3.2.0 avec packagification, stockage des médias en PostgreSQL et intégration de Sentry.
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de la délégation de réunions, correction de bugs d'affichage et ajout de documentation sur la personnalisation du scope OIDC.
- [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) : Amélioration de la gestion des appels à l'API FranceConnect et correction des problèmes de déploiement sur Scalingo.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Ajout de fonctionnalités de gestion des utilisateurs et amélioration de l'affichage des notifications.
