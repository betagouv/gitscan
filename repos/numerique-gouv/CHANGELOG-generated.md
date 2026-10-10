# Synthèse d'activité : numerique-gouv (du 01/09 au 30/09)

## Résumé de l'activité
L'activité de cette période est marquée par des transformations structurelles majeures, notamment la refonte complète de l'architecture de [oots-france](/repos/numerique-gouv/oots-france) et des évolutions importantes sur les applications mobiles [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android). Ces changements visent à moderniser les outils et à préparer les services à des usages plus larges et plus robustes.

Parallèlement, un effort soutenu a été porté sur l'accessibilité numérique avec [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) et sur l'internationalisation des plateformes de création de sites via [sites-faciles](/repos/numerique-gouv/sites-faciles). L'ensemble de l'organisation continue de renforcer la fiabilité de ses services grâce à une amélioration constante des processus de test et de sécurité.

## Sécurité
- Renforcement de l'authentification par l'introduction de la double authentification (2FA) dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Amélioration de la protection des accès et de la gestion des données (politiques CSP, durcissement des cookies, listes blanches d'IP) pour [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [francetransfert](/repos/numerique-gouv/francetransfert).
- Corrections de vulnérabilités critiques via la mise à jour de dépendances essentielles dans [django-dsfr](/repos/numerique-gouv/django-dsfr) et [dockerfiles](/repos/numerique-gouv/dockerfiles).
- Mise en place d'un contrôle automatique des vulnérabilités (CVE) dans la chaîne de déploiement de [sites-conformes](/repos/numerique-gouv/sites-conformes).

## Autres changements notables
- Migration architecturale majeure de [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails et intégration du Design System de l'État (DSFR).
- Modernisation de la chaîne de validation et du reporting de tests avec l'adoption d'Allure 3 pour [ami-system-tests](/repos/numerique-gouv/ami-system-tests).
- Refonte de la couche de composition WebView pour [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et automatisation des processus de build pour [ami-app-android](/repos/numerique-gouv/ami-app-android).
- Lancement initial du projet [agent-harness](/repos/numerique-gouv/agent-harness), un nouvel environnement dédié à l'évaluation d'agents.

## Dépôts les plus actifs
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Amélioration de l'expérience utilisateur dans la WebView et de l'intégration avec France Identité.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Introduction des Passkeys et mise en place d'environnements de pré-production.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux intensifs sur l'internationalisation et l'interface d'administration.
- [oots-france](/repos/numerique-gouv/oots-france) : Transition complète vers une nouvelle architecture logicielle.
- [ami-system-tests](/repos/numerique-gouv/ami-system-tests) : Optimisation de la fiabilité des tests et modernisation du reporting.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Évolutions fonctionnelles sur la gestion des consentements et de l'accessibilité.
