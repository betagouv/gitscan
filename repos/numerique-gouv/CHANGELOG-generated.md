# Synthèse d'activité : numerique-gouv (du 01/04 au 31/10/2026)

## Résumé de l'activité
L'activité de cette période est marquée par des transformations structurelles majeures, notamment le rebranding de la suite de création de sites vers "Sites Conformes" [sites-conformes-saas](/repos/numerique-gouv/sites-conformes-saas) et la refonte architecturale complète d'OOTS vers Ruby on Rails [oots-france](/repos/numerique-gouv/oots-france). Ces évolutions visent à offrir une base plus robuste et évolutive pour les services de l'État.

Parallèlement, l'organisation a concentré ses efforts sur l'amélioration de l'expérience utilisateur à travers l'internationalisation des outils de création [sites-faciles](/repos/numerique-gouv/sites-faciles) et la montée en puissance des applications mobiles. Ces dernières bénéficient de fonctionnalités modernes comme le support des Passkeys [ami-app-android](/repos/numerique-gouv/ami-app-android) et une navigation optimisée [ami-app-ios](/repos/numerique-gouv/ami-app-ios).

## Sécurité
- **Renforcement de l'authentification** : Introduction de la double authentification (2FA) [sites-conformes](/repos/numerique-gouv/sites-conformes) et intégration des Passkeys pour une connexion plus moderne et sécurisée [ami-app-android](/repos/numerique-gouv/ami-app-android).
- **Protection des données et des accès** : Suppression du logging de clés API et de jetons sensibles [b3desk](/repos/numerique-gouv/b3desk), durcissement des politiques CSP et des cookies [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), et mise en place de listes blanches d'adresses IP [francetransfert](/repos/numerique-gouv/francetransfert) et [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- **Gestion des vulnérabilités** : Mise à jour de dépendances critiques comme `cryptography` [django-dsfr](/repos/numerique-gouv/django-dsfr) et des images de base Keycloak [dockerfiles](/repos/numerique-gouv/dockerfiles), ainsi que l'automatisation du contrôle des vulnérabilités (CVE) dans la chaîne CI [sites-conformes](/repos/numerique-gouv/sites-conformes).

## Autres changements notables
- **Migrations architecturales** : Transition majeure de l'application OOTS vers le framework Ruby on Rails [oots-france](/repos/numerique-gouv/oots-france) et refonte de la structure des packages Swift pour le design system iOS [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).
- **Optimisation de la chaîne de développement (DevEx)** : Modernisation du reporting de tests avec Allure 3 [ami-system-tests](/repos/numerique-gouv/ami-system-tests), simplification de l'installation locale [oots-france](/repos/numerique-gouv/oots-france) et optimisation des processus de déploiement sur Scalingo [sites-faciles](/repos/numerique-gouv/sites-faciles).
- **Évolution de l'identité** : Passage officiel du projet "Sites Faciles" à "Sites Conformes" [sites-conformes-saas](/repos/numerique-gouv/sites-conformes-saas).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux intensifs sur l'internationalisation et l'interface d'administration.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android) : Évolutions majeures de versions, de navigation et de sécurité mobile.
- [oots-france](/repos/numerique-gouv/oots-france) : Réécriture complète de l'architecture logicielle.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Stabilisation et modernisation de l'infrastructure de tests et de la CI/CD.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Améliorations de l'UX, de l'accessibilité et renforcement de la sécurité.
