## Changelog : data_pass (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de la sécurité (bannissement d'utilisateurs), l'optimisation des performances (optimisation des tests CI/CD et des requêtes en base de données), et l'enrichissement des fonctionnalités pour les utilisateurs et les administrateurs (gestion des webhooks, édition de contenu, gestion des Data Providers). Des corrections de bugs et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- **Bannissement d'utilisateurs :** Ajout d'une fonctionnalité permettant aux administrateurs de bannir des utilisateurs, bloquant ainsi leur accès au système et aux sessions actives. [#1508](https://github.com/etalab/data_pass/pull/1508)
- **Amélioration de l'expérience utilisateur API Entreprise :** Suppression du scope `beneficiaires_effectifs_inpi` pour le formulaire API Entreprise. [#1482](https://github.com/etalab/data_pass/pull/1482)
- **Gestion des webhooks :** Ajout d'une page de documentation pour les webhooks, accessible aux développeurs. [#1502](https://github.com/etalab/data_pass/pull/1502)
- **Edition de contenu :** Possibilité pour les administrateurs d'éditer le contenu éditorial des types d'habilitation. [#1460](https://github.com/etalab/data_pass/pull/1460)
- **Gestion des Data Providers :** Ajout de la création et de la gestion des Data Providers depuis l'interface d'administration. [#1455](https://github.com/etalab/data_pass/pull/1455)
- **Amélioration des scopes Extenso :** Activation des scopes `men_statut_boursier` et `men_echelon_bourse` pour l'API Particulier. [#1473](https://github.com/etalab/data_pass/pull/1473)
- **Formulaire Extenso :** Ajout du bloc "modalités" au formulaire Extenso et amélioration de sa description. [#1467](https://github.com/etalab/data_pass/pull/1467)
- **Notifications :** Correction d'un bug empêchant les instructeurs de recevoir les notifications de messages. [#1471](https://github.com/etalab/data_pass/pull/1471)
- **Retrait des droits :** Correction du retrait de tous les droits d'un utilisateur. [#1494](https://github.com/etalab/data_pass/pull/1494)

### Évolutions techniques
- **Optimisation CI/CD :** Amélioration significative de la performance des tests CI/CD grâce à la parallélisation des tests Cucumber et RSpec, et à l'optimisation de l'utilisation de Docker. [#1503](https://github.com/etalab/data_pass/pull/1503), [#1498](https://github.com/etalab/data_pass/pull/1498)
- **Optimisation des requêtes :** Correction de requêtes N+1 sur le dashboard demandeur, améliorant ainsi les performances. [#1499](https://github.com/etalab/data_pass/pull/1499)
- **Refactoring :** Remplacement de `before_destroy` par un interactor pour la suppression d'un `HabilitationType`. [#1462](https://github.com/etalab/data_pass/pull/1462)
- **Synchronisation du cache :** Synchronisation du cache `StaticApplicationRecord` entre les workers Puma via Redis pour éviter les incohérences. [#1463](https://github.com/etalab/data_pass/pull/1463)
- **Mise à jour Rails :** Mise à jour de Rails vers la version 8.1.2.1. [#1461](https://github.com/etalab/data_pass/pull/1461)
- **Utilisation d'ID numériques :** Utilisation des ID numériques des autorisations dans les routes pour une meilleure performance. [#1498](https://github.com/etalab/data_pass/pull/1498)

### Autres changements
- **Documentation :** Mise à jour de la documentation des rôles. [#1507](https://github.com/etalab/data_pass/pull/1507)
- **Correction de bug :** Correction d'une boucle de redirection sur les dates d'homologation identiques. [#1469](https://github.com/etalab/data_pass/pull/1469)
- **Amélioration des tests :** Ajout de tests pour les cas d'erreur et de non-régression.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (action_text-trix, rubocop, webmock, etc.).
