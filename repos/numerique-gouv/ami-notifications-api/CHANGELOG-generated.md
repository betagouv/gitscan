## Changelog : ami-notifications-api (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des agents et de leurs accès, ainsi que sur des corrections et optimisations de l'API et de l'interface utilisateur. L'ajout de fonctionnalités de gestion des rôles et d'audit renforce la sécurité et la traçabilité du système. Des améliorations ont également été apportées à l'expérience utilisateur, notamment la gestion des notifications et la page de déconnexion.

### Évolutions fonctionnelles
- Ajout d'une page de gestion des accès pour les agents, permettant de gérer leurs rôles et permissions. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- Implémentation d'un audit des actions réalisées par les agents, notamment les changements de rôle. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- Amélioration de la gestion de la déconnexion avec une confirmation visuelle pour l'utilisateur. [#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)
- L'URL de l'application est désormais incluse dans les notifications envoyées aux applications mobiles. [#648](https://github.com/numerique-gouv/ami-notifications-api/issues/648)
- Correction d'un problème où l'identifiant du secteur n'était pas correctement utilisé. [#747](https://github.com/numerique-gouv/ami-notifications-api/issues/747)
- Simplification de l'endpoint des notifications. [#468](https://github.com/numerique-gouv/ami-notifications-api/issues/468)
- Correction de l'envoi des headers lors de la création de notifications planifiées. [#782](https://github.com/numerique-gouv/ami-notifications-api/issues/782)
- Envoi de l'URL interne lors de la création de notifications planifiées. [#779](https://github.com/numerique-gouv/ami-notifications-api/issues/779)

### Évolutions techniques
- Refactorisation de la gestion des erreurs dans l'API Particulier, ajout des headers dans les logs.
- Déplacement des endpoints `agenda` et `follow-p` sous `/api/v1` pour une meilleure organisation. [#762](https://github.com/numerique-gouv/ami-notifications-api/issues/762)
- Simplification des commandes et des tests pour les notifications planifiées. [#786](https://github.com/numerique-gouv/ami-notifications-api/issues/786)
- Suppression de l'utilisation de `settings.CONFIG` au profit de variables d'environnement plus explicites. [#729](https://github.com/numerique-gouv/ami-notifications-api/issues/729)
- Mise à jour de la configuration pour utiliser `fr-fr` comme langue par défaut. [#662](https://github.com/numerique-gouv/ami-notifications-api/issues/662)
- Suppression de `django-admin` et ajout d'une commande pour attribuer le rôle d'administrateur à un agent. [#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795)
- Initialisation du SDK Firebase. [#712](https://github.com/numerique-gouv/ami-notifications-api/issues/712)
- Reconnexion automatique de la websocket en cas de besoin. [#652](https://github.com/numerique-gouv/ami-notifications-api/issues/652)
- Mise à jour de l'URL du schéma OpenAPI. [#717](https://github.com/numerique-gouv/ami-notifications-api/issues/717)

### Autres changements
- Amélioration de la documentation CONTRIBUTING. [#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795)
- Corrections de linting et de style dans l'interface utilisateur (Svelte). [#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)
- Suppression de variables d'environnement inutilisées. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- Correction de padding sur la page d'accueil. [#764](https://github.com/numerique-gouv/ami-notifications-api/issues/764)
- Ajout d'un lien vers l'élément concerné dans les requêtes. [#726](https://github.com/numerique-gouv/ami-notifications-api/issues/726)
- Correction d'un bug empêchant la création d'un agent si `partner_id` était manquant. [#798](https://github.com/numerique-gouv/ami-notifications-api/issues/798)
- Suppression du champ `name` dans le log pour simplifier le message. [#626](https://github.com/numerique-gouv/ami-notifications-api/issues/626)
