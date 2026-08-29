# Synthèse d'activité : numerique-gouv (du 01/08 au 31/08)

## Résumé de l'activité
L'activité de la période est marquée par des transformations structurelles majeures, notamment la réécriture complète de [oots-france](/repos/numerique-gouv/oots-france) vers Ruby on Rails et le renforcement significatif de la sécurité de l'application mobile [ami-app-ios](/repos/numerique-gouv/ami-app-ios) via l'introduction des Passkeys et de la biométrie. Ces évolutions visent à moderniser les outils et à accroître la robustesse des services proposés.

Parallèlement, l'écosystème des sites web progresse vers une meilleure accessibilité internationale grâce à l'implémentation de l'internationalisation (i18n) sur les plateformes [sites-faciles](/repos/numerique-gouv/sites-faciles), [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) et [sites-conformes](/repos/numerique-gouv/sites-conformes). Ces changements améliorent l'expérience utilisateur et facilitent le déploiement de contenus multilingues.

## Sécurité
- Renforcement de la sécurité mobile avec le support des Passkeys, de l'authentification FaceID et du chiffrement des données locales dans [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- Correction de vulnérabilités critiques via la mise à jour de la bibliothèque `cryptography` dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Amélioration de la protection contre les abus par la mise en place du *rate limiting* dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Mise à jour de l'image de base Keycloak pour intégrer des correctifs de sécurité dans [dockerfiles](/repos/numerique-gouv/dockerfiles).
- Optimisation de la gestion des erreurs et du flux d'authentification FranceConnect dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Mise à jour de secrets pour assurer la sécurité du service [francetransfert](/repos/numerique-gouv/francetransfert).

## Autres changements notables
- **Migrations architecturales :** Transition majeure de [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails, incluant une interface d'administration conforme au DSFR.
- **Évolutions de données et de langage :** Migration vers Python 3.14 et introduction d'un nouveau modèle de données "Record" pour [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- **Internationalisation :** Déploiement de la gestion multilingue pour les formulaires et les interfaces dans [sites-faciles](/repos/numerique-gouv/sites-faciles), [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) et [sites-conformes](/repos/numerique-gouv/sites-conformes).
- **Refonte technique mobile :** Restructuration profonde de la couche de stockage (Keychain/UserDefaults) et de la stratégie de tests dans [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- **Infrastructure et déploiement :** Optimisation des processus de déploiement sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).

## Dépôts les plus actifs
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Travaux intensifs sur la sécurité biométrique, le stockage chiffré et l'architecture de test.
- [oots-france](/repos/numerique-gouv/oots-france) : Réécriture complète du système vers Ruby on Rails et modernisation de l'interface.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Évolution fonctionnelle majeure avec l'introduction du module "Services" et l'amélioration de l'administration.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Améliorations centrées sur l'internationalisation et la simplification du déploiement.
