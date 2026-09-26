# Synthèse d'activité : numerique-gouv (du 09/09 au 15/09)

## Résumé de l'activité
L'activité de la période est marquée par une forte dynamique de modernisation des interfaces et de renforcement de l'expérience utilisateur. Les efforts se sont concentrés sur l'internationalisation des plateformes [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), l'amélioration de l'accessibilité numérique [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) et l'adoption de standards de design modernes comme le DSFR [oots-france](/repos/numerique-gouv/oots-france).

Parallèlement, une montée en puissance de la sécurité est observée avec l'introduction des Passkeys [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [ami-app-android](/repos/numerique-gouv/ami-app-android) ainsi que le déploiement de l'authentification à deux facteurs [sites-conformes](/repos/numerique-gouv/sites-conformes). Ces évolutions visent à offrir des services plus robustes, accessibles et sécurisés pour les utilisateurs finaux.

## Sécurité
- Renforcement de l'authentification via l'implémentation des Passkeys et WebAuthn [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android).
- Déploiement de l'authentification à deux facteurs (2FA) et amélioration des notifications associées [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Amélioration de la détection de vulnérabilités (CVE) et de malwares au sein des chaînes de production [sites-conformes](/repos/numerique-gouv/sites-conformes) et [action-trivy-cache](/repos/numerique-gouv/action-trivy-cache).
- Corrections de vulnérabilités critiques sur des dépendances [django-dsfr](/repos/numerique-gouv/django-dsfr) et mise à jour d'images de base [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Autres changements notables
- Migration architecturale majeure vers le framework Ruby on Rails pour [oots-france](/repos/numerique-gouv/oots-france).
- Modernisation des processus de test et du reporting (migration vers Allure 3) [ami-system-tests](/repos/numerique-gouv/ami-system-tests).
- Optimisation des environnements de déploiement et création d'environnements de pré-production dédiés [sites-faciles](/repos/numerique-gouv/sites-faciles), [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android).
- Gestion plus flexible du parc d'instances [sites-faciles-saas](/repos/numerique-gouv/sites-faciles-saas).

## Dépôts les plus actifs
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Amélioration de l'expérience utilisateur (téléchargement, démarches en ligne) et renforcement de la sécurité.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Montée en puissance de la sécurité (Passkeys) et automatisation des configurations de build.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Refonte du système de suivi, optimisation de l'authentification et de la gestion des notifications.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Renforcement de la sécurité (2FA, CI/CD) et amélioration de l'expérience de recherche.
- [oots-france](/repos/numerique-gouv/oots-france) : Transition majeure vers Ruby on Rails et modernisation de l'interface utilisateur.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux importants sur l'internationalisation et l'optimisation du déploiement.
