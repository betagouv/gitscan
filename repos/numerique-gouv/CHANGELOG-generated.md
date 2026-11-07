# Synthèse d'activité : numerique-gouv (du 21/10 au 03/11)

## Résumé de l'activité
L'activité de cette période est marquée par des évolutions structurelles majeures, notamment la transition vers de nouvelles architectures pour [oots-france](/repos/numerique-gouv/oots-france) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios), ainsi que le rebranding de la gamme de services vers [sites-conformes](/repos/numerique-gouv/sites-conformes). Ces changements visent à renforcer la robustesse des services et à simplifier la maintenance à long terme.

Parallèlement, un effort important est porté sur l'internationalisation des plateformes, comme pour [sites-faciles](/repos/numerique-gouv/sites-faciles), et sur l'amélioration de l'expérience utilisateur via l'accessibilité et l'introduction de technologies modernes comme les Passkeys pour [ami-app-android](/repos/numerique-gouv/ami-app-android).

## Sécurité
- **Modernisation de l'authentification et des accès** : Introduction du support des Passkeys pour [ami-app-android](/repos/numerique-gouv/ami-app-android), renforcement de la protection via la 2FA et la lutte contre les fuites de secrets dans [sites-conformes](/repos/numerique-gouv/sites-conformes), et suppression du logging de données sensibles (clés API, jetons) dans [b3desk](/repos/numerique-gouv/b3desk).
- **Durcissement des politiques de sécurité** : Mise en place de politiques CSP, de durcissement des cookies et de whitelists IP dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), et renforcement de la protection via des règles de sécurité et la gestion d'adresses IP dans [francetransfert](/repos/numerique-gouv/francetransfert).
- **Maintenance et mises à jour critiques** : Correction de vulnérabilités via la mise à jour de dépendances clés (`cryptography`, image de base Keycloak) dans [django-dsfr](/repos/numerique-gouv/django-dsfr) et [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Autres changements notables
- **Migrations architecturales et refontes** : Transition majeure de [oots-france](/repos/numerique-gouv/oots-france) vers Ruby on Rails et refonte profonde du composant WebView pour [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- **Évolution de l'identité et nouveaux projets** : Rebranding officiel vers [sites-conformes](/repos/numerique-gouv/sites-conformes) et lancement initial du projet [agent-harness](/repos/numerique-gouv/agent-harness).
- **Optimisation de l'expérience développeur (DevEx) et des tests** : Migration vers WebdriverIO 10 pour [ami-system-tests](/repos/numerique-gouv/ami-system-tests), refonte du Swift Package pour [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) et simplification des déploiements sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux intensifs sur l'internationalisation et l'amélioration de l'interface utilisateur.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Évolutions fonctionnelles importantes et renforcement de la sécurité.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Refonte technique majeure et ajout de fonctionnalités de navigation et de mode hors-ligne.
- [oots-france](/repos/numerique-gouv/oots-france) : Transition complète vers une nouvelle architecture logicielle et modernisation de l'interface.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Améliorations de l'accessibilité, du SEO et de la fiabilité du déploiement.
