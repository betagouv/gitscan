# Synthèse d'activité : numerique-gouv (du 06 mai 2026 au 07 juin 2026)

## Résumé de l'activité
L'organisation numerique-gouv a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses dépôts. Les efforts se sont concentrés sur l'internationalisation des plateformes [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), avec l'ajout de la gestion multilingue et de sélecteurs de langue.  Des avancées importantes ont également été réalisées sur les applications mobiles AMI ([ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android)) avec des corrections et des améliorations de l'interface utilisateur. L'intégration de FranceConnect et l'amélioration de la sécurité sont également des thèmes récurrents, notamment avec le proxy [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) et la mise à jour des dépendances sur plusieurs dépôts.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances visant à corriger des vulnérabilités de sécurité :
- Mise à jour de `postcss` et `next` dans [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage).
- Mise à jour de plusieurs dépendances dans [b3desk](/repos/numerique-gouv/b3desk) via Dependabot.
- Utilisation de `mkcert` pour la gestion des certificats SSL locaux dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

## Autres changements notables
- Implémentation du support complet de l'API FranceConnect Identity dans [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Ajout de la possibilité de stocker les médias directement en base de données (PostgreSQL) dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Intégration de Sentry pour la surveillance des erreurs dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Automatisation de la publication des releases sur GitHub dans [b3desk](/repos/numerique-gouv/b3desk).
- Refactoring de la structure du projet et publication de composants pour une utilisation plus aisée dans [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).
- Mise en place d'un mécanisme de réplication de la base de données vers un datawarehouse dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

## Dépôts les plus actifs
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de la délégation de réunions, intégration des claims OIDC et automatisation de la publication des releases.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Internationalisation de la plateforme avec ajout d'un sélecteur de langue et traduction des champs de formulaire.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Amélioration de la gestion des préférences de localisation et implémentation d'un nouveau flux d'authentification avec FranceConnect.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Ajout du stockage des médias en PostgreSQL, intégration de Sentry et préparation de la release v3.2.0.
- [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) : Implémentation du support complet de l'API FranceConnect Identity.
