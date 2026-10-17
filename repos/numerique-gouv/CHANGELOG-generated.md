# Synthèse d'activité : numerique-gouv (du 01/09 au 30/09)

## Résumé de l'activité
L'activité de cette période est marquée par une volonté de modernisation profonde, tant sur le plan architectural que sur celui de l'expérience utilisateur. Les efforts se sont concentrés sur l'amélioration de la sécurité (introduction des Passkeys et renforcement de l'authentification), l'accessibilité numérique et l'internationalisation des services.

Des projets majeurs comme [oots-france](/repos/numerique-gouv/oots-france) ont franchi des étapes clés avec des refontes technologiques complètes, tandis que l'écosystème mobile [ami](/repos/numerique-gouv/ami-app-ios) et [ami](/repos/numerique-gouv/ami-app-android) se modernise pour offrir des standards de sécurité et de performance accrus.

## Sécurité
- **Authentification moderne** : Introduction du support des Passkeys pour une connexion plus sécurisée sur [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android), et renforcement de la double authentification (2FA) sur [sites-conformes](/repos/numerique-gouv/sites-conformes).
- **Protection des infrastructures** : Durcissement des politiques de sécurité (CSP, gestion des cookies, listes blanches d'IP) sur [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [francetransfert](/repos/numerique-gouv/francetransfert).
- **Maintenance de sécurité** : Corrections de vulnérabilités critiques via la mise à jour de dépendances clés sur [django-dsfr](/repos/numerique-gouv/django-dsfr) et [dockerfiles](/repos/numerique-gouv/dockerfiles).
- **Sécurité CI/CD** : Mise en place de contrôles automatiques des vulnérabilités lors des changements de dépendances sur [sites-conformes](/repos/numerique-gouv/sites-conformes).

## Autres changements notables
- **Refontes architecturales** : Transition majeure vers Ruby on Rails pour [oots-france](/repos/numerique-gouv/oots-france) et restructuration de l'architecture mobile pour [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- **Internationalisation** : Déploiement de fonctionnalités multilingues (sélecteur de langue, traduction des formulaires) sur [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1).
- **Accessibilité (A11y)** : Travaux importants pour garantir une expérience inclusive et conforme sur [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage).
- **Optimisation de la chaîne de développement** : Modernisation du reporting de tests avec Allure 3 sur [ami-system-tests](/repos/numerique-gouv/ami-system-tests) et automatisation des configurations de build sur [ami-app-android](/repos/numerique-gouv/ami-app-android).
- **Lancement de projet** : Initialisation de [agent-harness](/repos/numerique-gouv/agent-harness), un nouvel environnement dédié à l'évaluation d'agents.

## Dépôts les plus actifs
- [oots-france](/repos/numerique-gouv/oots-france) : Migration architecturale complète et intégration du Design System de l'État.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Montée en puissance de la sécurité et automatisation des processus de déploiement.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Stabilisation de la suite de tests et modernisation de la chaîne CI/CD.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Améliorations significatives sur l'internationalisation et l'interface utilisateur.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Évolutions fonctionnelles majeures et renforcement de la sécurité.
