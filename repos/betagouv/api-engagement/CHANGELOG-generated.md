## Changelog : api-engagement (30 derniers jours, au 12 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'API Engagement au cours des 30 derniers jours. Les principales évolutions concernent la sécurité (validation des webhooks Brevo, règles d'accès à l'API, limitation du débit), l'ajout de journaux d'audit, l'amélioration de l'interface utilisateur du back-office (gestion des clés API, affichage d'URL de test) et des optimisations techniques pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'un onglet pour gérer les clés API des annonceurs dans le back-office. [#1015](https://github.com/betagouv/api-engagement/issues/1015)
- Affichage de l'URL de l'environnement sandbox pour les testeurs de l'API dans le back-office. [#1012](https://github.com/betagouv/api-engagement/issues/1012)
- Activation des missions de service civique dans le job Grimpio. [#977](https://github.com/betagouv/api-engagement/issues/977)
- Correction de l'affichage des filtres de modération et des débordements dans le back-office. [#975](https://github.com/betagouv/api-engagement/issues/975)
- Correction de l'alignement horizontal du sélecteur de date dans le back-office. [#976](https://github.com/betagouv/api-engagement/issues/976)
- Correction d'un bug de déconnexion pour les utilisateurs accédant à la page "mes missions". [#799](https://github.com/betagouv/api-engagement/issues/799)
- Amélioration de la conception réactive du back-office pour les petites vues. [#930](https://github.com/betagouv/api-engagement/issues/930)

### Évolutions techniques
- Mise en place de règles de contrôle d'accès à l'API avec tests associés. [#1013](https://github.com/betagouv/api-engagement/issues/1013)
- Refactorisation du middleware de contrôle d'accès pour une meilleure maintenabilité.
- Ajout de journaux d'audit pour suivre les actions effectuées sur l'API. [#1019](https://github.com/betagouv/api-engagement/issues/1019)
- Sécurisation des webhooks Brevo. [#1026](https://github.com/betagouv/api-engagement/issues/1026)
- Suppression de la validation des adresses IP Brevo. [#1027](https://github.com/betagouv/api-engagement/issues/1027)
- Implémentation de limiteurs de débit pour les requêtes API (publisherRateLimiter et ipRateLimiter). [#932](https://github.com/betagouv/api-engagement/issues/932)
- Refactorisation de l'exécution des agrégations du widget pour une meilleure performance. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Refactorisation de la gestion des missions avec exclusion de l'organisation de l'annonceur. [#965](https://github.com/betagouv/api-engagement/issues/965)
- Utilisation de `tsvector` pour la recherche d'organisations par texte. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Suppression du magasin partagé de limite de taux. [#959](https://github.com/betagouv/api-engagement/issues/959)
- Ajout de configuration Mockoon pour les tests. [#978](https://github.com/betagouv/api-engagement/issues/978)
- Correction de la construction du job. [#1018](https://github.com/betagouv/api-engagement/issues/1018)
- Correction de la version de dbt pour les dépendances. [#1023](https://github.com/betagouv/api-engagement/issues/1023)
- Déploiement de la spécification OpenAPI sur le CI. [#1014](https://github.com/betagouv/api-engagement/issues/1014)

### Autres changements
- Mise à jour de plusieurs dépendances (actions/checkout, orhun/git-cliff-action, scaleway/action-scw, etc.).
- Correction de la documentation et du changelog.
- Amélioration du script de vérification des champs orphelins des événements statistiques.
- Ajout d'un WAF proxy. [#795](https://github.com/betagouv/api-engagement/issues/795)
- Suppression de la relation activity_id des missions. [#787](https://github.com/betagouv/api-engagement/issues/787)
