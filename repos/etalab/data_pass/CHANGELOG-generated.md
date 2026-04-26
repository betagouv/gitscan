## Changelog : data_pass (30 derniers jours, au 2026-04-24)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'API (ajout de fonctionnalités d'écriture, exposition de nouvelles données), la gestion des droits d'accès (nouveaux rôles, suppression de droits), et la correction de bugs, notamment concernant les redirections et les requêtes en base de données. Des améliorations de la sécurité ont également été apportées avec l'ajout d'une fonctionnalité de bannissement d'utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une interface d'administration pour bannir des utilisateurs et bloquer leurs accès [#1508](https://github.com/etalab/data_pass/pull/1508).
- Possibilité d'ajouter de nouveaux scopes aux HabilitationType avec des demandes [#1484](https://github.com/etalab/data_pass/pull/1484).
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur [#1494](https://github.com/etalab/data_pass/pull/1494).
- L'API expose désormais le numéro de téléphone de l'applicant [#1523](https://github.com/etalab/data_pass/pull/1523).
- Ajout d'endpoints POST et PATCH pour la création et la mise à jour de demandes via l'API v1 [#1504](https://github.com/etalab/data_pass/pull/1504).
- Ajout d'un lien vers le formulaire de création de demande dans la liste des habilitations [#1487](https://github.com/etalab/data_pass/pull/1487).
- Correction d'un bug de redirection infinie [#1469](https://github.com/etalab/data_pass/pull/1469).
- Correction d'un bug empêchant la consultation d'habilitations pour les organisations non vérifiées [#1478](https://github.com/etalab/data_pass/pull/1478).
- Affichage d'un message d'erreur plus clair en cas d'échec de connexion [#1531](https://github.com/etalab/data_pass/pull/1531).
- Amélioration de l'affichage des scopes dans l'interface utilisateur (suppression d'une ligne inutile, harmonisation des liens).

### Évolutions techniques
- Refactorisation de la gestion des rôles avec l'introduction de `RoleHierarchy` et `RoleSet` pour supporter les rôles de niveau FD avec wildcard [#1520](https://github.com/etalab/data_pass/pull/1520).
- Ajout d'un service `MarkdownRenderer` pour gérer le rendu du Markdown.
- Amélioration de la gestion des erreurs API avec `APIErrorsFacade` pour traduire les erreurs d'interactors en JSON:API.
- Introduction d'un `ApplicationInteractor#fail_with_error` pour simplifier la gestion des erreurs.
- Ajout d'événements `create_by_api` et `update_by_api` pour le suivi des actions via l'API.
- Optimisation des requêtes en base de données sur le dashboard demandeur [#1499](https://github.com/etalab/data_pass/pull/1499).
- Amélioration de la configuration des tests CI/CD (parallélisation, utilisation d'images Docker fixes).
- Passage de la timezone Rails à Chronic pour éviter des problèmes en CI.
- Refactorisation de `MaintenanceBanner` en un service singleton `AnnouncementBanner`.

### Autres changements
- Mise à jour de la documentation des rôles.
- Ajout d'une documentation pour les webhooks.
- Mise à jour de plusieurs dépendances (rubocop, yard, zlib, rack-session, action_text-trix, webmock, mcp).
- Suppression des scopes `beneficiaires_effectifs_inpi` pour l'API entreprise-entrouvert.
- Ajout de la raison privée pour les admins.
- Ajout des logs pour les changements faits par les admins.
- Amélioration des descriptions OpenAPI.
- Correction de typos dans les emails.
- Rendre les URLs cliquables dans les emails.
- Activation des scopes MEN.
- Ajout d'un suffixe au slug des HabilitationType.
- Correction d'un bug lié à la gestion des CGU vides.
- Ajout de la gestion des personnes physiques et des organisations étrangères dans le nom de l'organisation.
- Ajout d'un mécanisme pour ignorer la tâche d'update INSEE en développement si les credentials INSEE ne sont pas disponibles.
