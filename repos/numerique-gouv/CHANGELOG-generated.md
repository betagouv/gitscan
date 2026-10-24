# Synthèse d'activité : numerique-gouv (du 13/10 au 23/10)

## Résumé de l'activité
L'activité de cette période est marquée par des transformations structurelles majeures, notamment le rebranding de la solution de création de sites vers [sites-conformes](/repos/numerique-gouv/sites-conformes) et la refonte complète de l'architecture de [oots-france](/repos/numerique-gouv/oots-france) vers Ruby on Rails. Les efforts se sont également concentrés sur l'internationalisation des outils de création de sites et la modernisation de l'expérience utilisateur.

Parallèlement, une montée en puissance de la sécurité est observée à travers l'adoption des Passkeys sur les applications mobiles [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android), ainsi que le renforcement des protocoles d'authentification et de protection des données sur l'ensemble des services.

## Sécurité
- Renforcement de l'authentification via la double authentification (2FA) dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Introduction du support des Passkeys pour une authentification moderne et sécurisée sur [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android).
- Sécurisation des données sensibles par la suppression du logging des clés API et des jetons utilisateurs dans [b3desk](/repos/numerique-gouv/b3desk).
- Amélioration de la protection contre les vulnérabilités via le contrôle automatique des CVE dans [sites-conformes](/repos/numerique-gouv/sites-conformes) et la mise à jour de dépendances critiques dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Durcissement des politiques de sécurité (CSP, cookies, listes blanches d'IP) dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [francetransfert](/repos/numerique-gouv/francetransfert).

## Autres changements notables
- Migration architecturale majeure de [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails avec intégration du Design System de l'État (DSFR).
- Rebranding officiel du projet vers [sites-conformes-saas](/repos/numerique-gouv/sites-conformes-saas).
- Modernisation de la chaîne de tests et du reporting (passage à Allure 3) pour [ami-system-tests](/repos/numerique-gouv/ami-system-tests).
- Refonte de l'architecture des applications mobiles [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).
- Optimisation des processus de déploiement sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Travaux intensifs sur l'internationalisation et l'interface d'administration.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android) : Évolutions majeures sur la sécurité (Passkeys) et l'architecture.
- [oots-france](/repos/numerique-gouv/oots-france) : Réécriture complète du système et modernisation de l'interface.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Amélioration des fonctionnalités de suivi, de gestion des consentements et de l'accessibilité.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Optimisation de la fiabilité des tests et de la chaîne CI/CD.
