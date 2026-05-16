## Changelog : ami-notifications-api (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur pour les agents, notamment avec l'ajout de fonctionnalités pour la gestion des notifications et des agendas, ainsi que des corrections de bugs et des optimisations de performance. Des travaux importants ont également été réalisés sur la réplication des données et la gestion des rôles d'administration.

### Évolutions fonctionnelles
- **Gestion des notifications (Agent Admin):** Ajout de la possibilité pour les agents d'envoyer des notifications directement depuis l'interface d'administration, incluant une recherche d'AMI partenaire via un autocomplete. [#773](https://github.com/numerique-gouv/ami-notifications-api/issues/773)
- **Agenda et Suivi:** Intégration d'un agenda avec affichage des vacances scolaires, configurable par l'utilisateur en fonction de sa zone géographique.  Possibilité de définir des préférences de zone pour l'affichage des vacances. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Confirmation de déconnexion:** Ajout d'une modal de confirmation lors de la déconnexion pour éviter les actions involontaires. [#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)
- **Améliorations de l'interface:** Corrections de padding et d'alignement sur la page d'accueil. [#764](https://github.com/numerique-gouv/ami-notifications-api/issues/764)
- **Gestion des rôles:** Ajout d'une commande pour attribuer le rôle d'administrateur à un agent. [#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795)
- **Amélioration de l'expérience utilisateur:** Correction d'un problème de défilement sur la page d'adresse et ajout de sticky headers. [#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)
- **FranceConnect:** Centrage vertical du bouton FranceConnect. [#515](https://github.com/numerique-gouv/ami-notifications-api/issues/515)

### Évolutions techniques
- **Réplication des données:** Refonte de la logique de réplication des utilisateurs avec ajout de tests et d'une commande Django pour la réplication. [#791](https://github.com/numerique-gouv/ami-notifications-api/issues/791)
- **Mise à jour de Django:** Mise à jour de Django vers la version 6.0.5.
- **Utilisation de mkcert:** Utilisation de `mkcert` pour la gestion des certificats SSL en local. [#828](https://github.com/numerique-gouv/ami-notifications-api/issues/828)
- **Cache HTTPX:** Ajout de cache aux requêtes GET via httpx pour améliorer les performances.
- **Linting Front:** Correction de plusieurs avertissements de linting dans le code front-end. [#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)
- **Suppression de django-admin:** Suppression de la commande `django-admin` et remplacement par des commandes customisées. [#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795)

### Autres changements
- **Documentation:** Mise à jour de la documentation CONTRIBUTING.
- **Correction de bugs:** Correction de plusieurs bugs mineurs dans l'interface utilisateur et l'API.
- **Amélioration du logging:** Amélioration des logs pour faciliter le débogage.
- **Refactoring:** Refactoring de code pour améliorer la lisibilité et la maintenabilité.
- **Gestion des dépendances:** Mises à jour de plusieurs dépendances (twisted, urllib3, uuid, @cucumber/cucumber, python-dotenv, lxml, uv, pytest, postcss, @sveltejs/kit).
