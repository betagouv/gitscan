# Synthèse d'activité : numerique-gouv (du 25/09 au 01/10)

## Résumé de l'activité
L'activité de cette période est marquée par une volonté de modernisation des interfaces et un renforcement de l'accessibilité et de la sécurité. Les efforts se sont concentrés sur l'adoption de méthodes d'authentification plus modernes (Passkeys) pour les applications mobiles [ami-app-android](/repos/numerique-gouv/ami-app-android) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios), ainsi que sur l'amélioration de l'inclusion numérique via des optimisations d'accessibilité sur [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage).

Parallèlement, l'organisation a franchi des étapes structurelles importantes, notamment avec la refonte architecturale majeure de [oots-france](/repos/numerique-gouv/oots-france) et l'internationalisation des outils de création de sites [sites-faciles](/repos/numerique-gouv/sites-faciles). Ces évolutions visent à offrir des services plus robustes, multilingues et conformes aux standards de l'État.

## Sécurité
- **Authentification moderne** : Implémentation du support des Passkeys (WebAuthn) pour sécuriser l'accès sur [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), [ami-app-android](/repos/numerique-gouv/ami-app-android) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- **Renforcement des accès** : Mise en place de la double authentification (2FA) et de notifications d'incitation sur [sites-conformes](/repos/numerique-gouv/sites-conformes), ainsi que sécurisation des redirections FranceConnect sur [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- **Contrôle et corrections** : Mise en place d'un contrôle automatique des vulnérabilités (CVE) lors des mises à jour de dépendances sur [sites-conformes](/repos/numerique-gouv/sites-conformes) et correction de vulnérabilités critiques via la mise à jour de la bibliothèque `cryptography` sur [django-dsfr](/repos/numerique-gouv/django-dsfr).

## Autres changements notables
- **Migrations architecturales** : Transition complète de l'application [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails et intégration du Design System de l'État (DSFR).
- **Optimisation de la qualité logicielle** : Modernisation du système de reporting de tests avec Allure 3 et optimisation de la chaîne CI/CD pour [ami-system-tests](/repos/numerique-gouv/ami-system-tests).
- **Évolutions techniques mobiles** : Refonte de l'architecture de la WebView sur [ami-app-ios](/repos/numerique-gouv/ami-app-ios) pour améliorer la navigation et la gestion des documents.
- **Simplification du déploiement** : Mise en place d'un déploiement en un clic sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).

## Dépôts les plus actifs
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Amélioration de l'expérience utilisateur mobile, de la navigation et de la gestion documentaire.
- [oots-france](/repos/numerique-gouv/oots-france) : Refonte complète de l'architecture et modernisation de l'interface utilisateur.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Évolutions majeures sur la sécurité (Passkeys) et l'optimisation des notifications.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux importants sur l'internationalisation et la facilité de déploiement.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Stabilisation de la suite de tests et modernisation du reporting de qualité.
