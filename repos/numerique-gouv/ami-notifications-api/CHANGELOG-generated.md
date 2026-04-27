## Changelog : ami-notifications-api (30 derniers jours, au 23 avril 2026)

### Résumé
Les dernières mises à jour de l'API de notifications AMI se concentrent sur l'amélioration de l'expérience utilisateur de l'interface web, notamment l'ajout de fonctionnalités d'agenda et de préférences utilisateur, ainsi que sur la gestion des accès et des rôles des agents. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- **Agenda :** Intégration d'un agenda affichant les jours fériés scolaires, configurable par l'utilisateur en fonction de sa zone géographique.  L'affichage de l'agenda nécessite une connexion utilisateur. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Préférences utilisateur :** Possibilité pour l'utilisateur de définir ses préférences de zone géographique pour l'affichage de l'agenda. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Gestion des accès :** Ajout d'une page de gestion des accès permettant de gérer les agents et leurs rôles (agent, agent administrateur).  Possibilité de donner le rôle administrateur à un agent. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Confirmation de déconnexion :** Affichage d'une modal de confirmation lors de la déconnexion de l'utilisateur. [#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)
- **Amélioration de l'interface :** Correction de problèmes de padding sur la page d'accueil. [#764](https://github.com/numerique-gouv/ami-notifications-api/issues/764)
- **Affichage des journaux d'audit :** Affichage des journaux d'audit sur la page de gestion des accès. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Amélioration de la navigation :** Correction du centrage vertical du bouton FranceConnect. [#515](https://github.com/numerique-gouv/ami-notifications-api/issues/515)
- **Amélioration de l'interface :** Correction du défilement des champs de saisie d'adresse. [#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)

### Évolutions techniques
- **Refactoring API :** Déplacement des endpoints `/agenda` et `/follow-p` derrière le préfixe `/api/v1`. [#762](https://github.com/numerique-gouv/ami-notifications-api/issues/762)
- **Cache HTTP :** Ajout de la mise en cache des requêtes GET avec `httpx`. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Configuration :** Migration des variables d'environnement vers les fichiers de configuration Django. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Authentification :** Amélioration de l'intégration avec ProConnection et FranceConnect. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Journalisation :** Ajout des headers dans les logs d'erreurs d'API Part.
- **Tests :** Mise à jour des tests unitaires suite aux refactorings.
- **Linting :** Correction de plusieurs avertissements de linting (noNonNullAssertion, noExplicitAny, noDescendingSpecificity, useTemplate, noImportantStyles). [#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)

### Autres changements
- **Documentation :** Mise à jour de la documentation CONTRIBUTING.
- **Suppression de code obsolète :** Suppression de `django-admin`.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (uuid, @cucumber/cucumber, python-dotenv, lxml, @sveltejs/kit, uv, pytest, pygments, cryptography).
- **Correction de bug :** Correction d'un problème lié à l'URL du secteur d'activité. [#747](https://github.com/numerique-gouv/ami-notifications-api/issues/747)
- **Correction de bug :** Correction d'un problème lié à la duplication des requêtes de notifications. [#647](https://github.com/numerique-gouv/ami-notifications-api/issues/647)
- **Correction de bug :** Correction d'un problème lié à l'envoi des notifications planifiées avec des headers incorrects. [#782](https://github.com/numerique-gouv/ami-notifications-api/issues/782)
- **Correction de bug :** Correction d'un problème lié à l'envoi de l'URL interne lors de la création de notifications planifiées. [#779](https://github.com/numerique-gouv/ami-notifications-api/issues/779)
- **Correction de bug :** Correction d'un problème lié à l'expiration des données si la zone est une chaîne de caractères. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Correction de bug :** Correction d'un problème lié à la boucle de rafraîchissement de la fenêtre.
- **Correction de bug :** Correction d'un problème lié à l'affichage des journaux d'audit.
- **Correction de bug :** Correction d'un problème lié à la gestion des identifiants partenaires. [#798](https://github.com/numerique-gouv/ami-notifications-api/issues/798)
