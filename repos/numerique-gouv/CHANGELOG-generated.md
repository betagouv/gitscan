# Synthèse d'activité : numerique-gouv (du 02/04 au 10/09)

## Résumé de l'activité
L'activité récente est portée par trois axes majeurs : l'ouverture internationale des outils de création de sites, la modernisation de la sécurité utilisateur et la refonte profonde des infrastructures techniques. Les outils de création de sites [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) progressent significativement vers le multilingue, facilitant ainsi l'usage de la plateforme dans des contextes variés.

Parallèlement, l'écosystème mobile AMI franchit un cap technologique avec l'introduction des Passkeys et de la biométrie pour une authentification plus fluide et sécurisée [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android). Enfin, des transitions architecturales majeures, notamment sur [oots-france](/repos/numerique-gouv/oots-france), préparent les services à une meilleure robustesse et une maintenance simplifiée pour les développeurs.

## Sécurité
- Renforcement de l'authentification via l'introduction des Passkeys (WebAuthn), du support JWT et de la validation des jetons FranceConnect [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Sécurisation des accès mobiles par l'intégration de la biométrie (FaceID) et le chiffrement des données locales [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- Mise en place de l'authentification à deux facteurs (2FA) pour sécuriser l'accès aux plateformes [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Corrections de vulnérabilités critiques sur des dépendances clés et des images de base [django-dsfr](/repos/numerique-gouv/django-dsfr) et [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Autres changements notables
- Migration architecturale majeure vers le framework Ruby on Rails pour améliorer la robustesse et l'expérience de développement [oots-france](/repos/numerique-gouv/oots-france).
- Modernisation de la chaîne de tests et du reporting (passage à Allure 3) pour une meilleure visibilité sur la qualité logicielle [ami-system-tests](/repos/numerique-gouv/ami-system-tests).
- Optimisation des processus de déploiement et de configuration (Scalingo, variables d'environnement) [sites-faciles](/repos/numerique-gouv/sites-faciles) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Alignement visuel sur le Design System de l'État (DSFR) pour les interfaces web et mobiles [oots-france](/repos/numerique-gouv/oots-france) et [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux intensifs sur l'internationalisation et la simplification du déploiement.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Refonte de la sécurité (Passkeys, biométrie) et de l'architecture de stockage local.
- [oots-france](/repos/numerique-gouv/oots-france) : Transition majeure vers une nouvelle architecture et refonte de l'interface utilisateur.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Stabilisation de la suite de tests et optimisation de la chaîne CI/CD.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Améliorations de l'authentification et de la gestion des notifications.
