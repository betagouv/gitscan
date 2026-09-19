# Synthèse d'activité : numerique-gouv (du 02/09 au 15/09)

## Résumé de l'activité
L'activité de l'organisation est marquée par une montée en puissance de la sécurité et de l'accessibilité des services. Les efforts se sont concentrés sur l'adoption de nouvelles méthodes d'authentification (Passkeys, 2FA) et l'amélioration de l'expérience utilisateur, notamment via l'internationalisation des outils de création de sites et l'optimisation de l'accessibilité numérique pour les utilisateurs en situation de handicap.

Parallèlement, l'organisation engage des transformations structurelles importantes, avec des refontes architecturales majeures et une modernisation des chaînes de tests et de déploiement pour garantir des services plus robustes, plus observables et plus faciles à maintenir.

## Sécurité
- **Authentification moderne** : Implémentation des Passkeys/WebAuthn et renforcement de la sécurité FranceConnect dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android).
- **Protection des accès** : Mise en place de l'authentification à deux facteurs (2FA) dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- **Maintenance de la sécurité logicielle** : Mise à jour de dépendances critiques (notamment `cryptography`) et des images de base (Keycloak) dans [django-dsfr](/repos/numerique-gouv/django-dsfr) et [dockerfiles](/repos/numerique-gouv/dockerfiles), ainsi que l'intégration d'outils d'analyse statique (Bandit) dans [sites-conformes](/repos/numerique-gouv/sites-conformes).

## Autres changements notables
- **Migrations architecturales** : Transition majeure de l'application [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails, incluant une interface modernisée conforme au DSFR.
- **Modernisation de la CI/CD et des tests** : Optimisation de la fiabilité des tests et modernisation du reporting (Allure 3) dans [ami-system-tests](/repos/numerique-gouv/ami-system-tests), et découplage des cycles de tests par rapport aux déploiements dans [ami-system-tests](/repos/numerique-gouv/ami-system-tests).
- **Infrastructure et environnements** : Création d'environnements de pré-production dédiés pour [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android), et simplification du déploiement sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).
- **Observabilité** : Renforcement de la traçabilité et de la gestion des logs pour faciliter le diagnostic technique dans [francetransfert](/repos/numerique-gouv/francetransfert).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Travaux importants sur l'internationalisation (i18n) et l'interface d'administration.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android) : Évolutions centrées sur la sécurité (Passkeys) et la gestion des environnements de test.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Refonte du système de suivi et optimisation des parcours d'authentification.
- [oots-france](/repos/numerique-gouv/oots-france) : Migration complète de l'architecture logicielle.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Stabilisation de la suite de tests et modernisation de la chaîne de validation.
