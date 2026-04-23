## Changelog : data_pass (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'API avec l'ajout de fonctionnalités de création et de mise à jour de demandes, ainsi que sur la gestion des utilisateurs avec l'ajout d'une fonctionnalité de bannissement. Des améliorations ont également été apportées à la documentation, aux tests et à la sécurité du système.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer et mettre à jour des demandes via l'API. [#1504](https://github.com/etalab/data_pass/pull/1504)
- Ajout de la possibilité de bannir un utilisateur administrateur, bloquant ainsi son accès au système. [#1508](https://github.com/etalab/data_pass/pull/1508)
- Amélioration de la gestion des scopes OAuth2, notamment pour les formulaires Solis et les habilitations avec demandes. [#1484](https://github.com/etalab/data_pass/pull/1484)
- Ajout d'un lien vers le formulaire de création de demande dans la liste des habilitations. [#1487](https://github.com/etalab/data_pass/pull/1487)
- Possibilité de remplir les champs `france_connect_authorization_id` lors de la validation d'une demande. [#1459](https://github.com/etalab/data_pass/pull/1459)
- Activation des scopes MEN (statut boursier et échelon de bourse) pour l'API Particulier. [#1473](https://github.com/etalab/data_pass/pull/1473)
- Amélioration de la consultation d'une habilitation avec une organisation non vérifiée. [#1475](https://github.com/etalab/data_pass/pull/1475)
- Correction d'une boucle de redirection sur les dates d'homologation identiques. [#1469](https://github.com/etalab/data_pass/pull/1469)
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur. [#1494](https://github.com/etalab/data_pass/pull/1494)
- Correction d'un bug empêchant les instructeurs de recevoir les notifications de messages. [#1471](https://github.com/etalab/data_pass/pull/1471)

### Évolutions techniques
- Refactorisation du code pour factoriser les étapes communes entre les organisateurs Create/Update AR. [#1504](https://github.com/etalab/data_pass/pull/1504)
- Ajout d'APIErrorsFacade pour traduire les échecs d'interactors en JSON:API. [#1504](https://github.com/etalab/data_pass/pull/1504)
- Introduction de `ApplicationInteractor#fail_with_error`. [#1504](https://github.com/etalab/data_pass/pull/1504)
- Ajout d'événements `create_by_api` et `update_by_api`. [#1504](https://github.com/etalab/data_pass/pull/1504)
- Amélioration des descriptions OpenAPI. [#1504](https://github.com/etalab/data_pass/pull/1504)
- Optimisation des tests CI, notamment en parallélisant les tests Cucumber et RSpec. [#1503](https://github.com/etalab/data_pass/pull/1503)
- Mise à jour de Rails vers la version 8.1.2.1. [#1470](https://github.com/etalab/data_pass/pull/1470)
- Refactorisation de `MaintenanceBanner` en service singleton `AnnouncementBanner`. [#1505](https://github.com/etalab/data_pass/pull/1505)
- Isole la gestion des diffs des changelogs. [#1506](https://github.com/etalab/data_pass/pull/1506)

### Autres changements
- Ajout d'une page de documentation des webhooks.
- Ajout d'une raison privée pour les admins.
- Ajout d'AdminChange pour tracer les changements faits par des admins.
- Mise à jour de la documentation des rôles.
- Correction de typos dans les sujets des emails.
- Rendre les URLs cliquables dans les emails.
- Mise à jour des wordings de la tarification Eaje.
- Ajout d'un guideline CLAUDE pour co-author les commits.
- Diverses mises à jour de dépendances.
