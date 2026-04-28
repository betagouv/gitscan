## Changelog : data_pass (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'accusés de réception pour les demandes, une meilleure gestion des rôles et des droits, ainsi que des corrections de bugs critiques. Des améliorations techniques ont également été apportées pour optimiser les performances et la sécurité de la plateforme, notamment au niveau des tests et de la gestion des dépendances.

### Évolutions fonctionnelles

- Ajout d'un accusé de réception envoyé à l'utilisateur lors du dépôt d'une demande. [#1536](https://github.com/etalab/data_pass/pull/1536)
- Amélioration de l'affichage des scopes boursier MEN sur les formulaires CNAF, en les masquant. [#1514](https://github.com/etalab/data_pass/pull/1514)
- Ajout d'un lien vers le formulaire de création de demande dans la liste des habilitations. [#1487](https://github.com/etalab/data_pass/pull/1487)
- Amélioration de la gestion des rôles et des droits, notamment avec la prise en charge des rôles de niveau FD (Finance Développement). [#1520](https://github.com/etalab/data_pass/pull/1520) et [#1484](https://github.com/etalab/data_pass/pull/1484)
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur. [#1494](https://github.com/etalab/data_pass/pull/1494)
- Correction d'un bug critique provoquant une boucle de redirection. [#1469](https://github.com/etalab/data_pass/pull/1469)
- Correction d'un bug empêchant la consultation des habilitations pour les organisations non vérifiées. [#1554](https://github.com/etalab/data_pass/pull/1478)
- Ajout de la possibilité de bannir un utilisateur. [#1508](https://github.com/etalab/data_pass/pull/1508)
- Amélioration de l'affichage des erreurs de connexion. [#1531](https://github.com/etalab/data_pass/pull/1531)
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API. [#1523](https://github.com/etalab/data_pass/pull/1523)

### Évolutions techniques

- Optimisation des tests CI/CD, réduisant significativement leur durée d'exécution. [#1503](https://github.com/etalab/data_pass/pull/1503)
- Refactoring de la gestion des erreurs et amélioration de l'affichage des messages d'erreur. [#1515](https://github.com/etalab/data_pass/pull/1515)
- Mise à jour de plusieurs dépendances (Rubocop, Yard, Zlib, Rack-Session, etc.).
- Migration des tables rails_pulse et lazy_load faker. [#1533](https://github.com/etalab/data_pass/pull/1533)
- Ajout de tests contractuels pour garantir la cohérence des définitions. [#1528](https://github.com/etalab/data_pass/pull/1528)
- Amélioration de la documentation et ajout de tutoriels pour les développeurs. [#1522](https://github.com/etalab/data_pass/pull/1522)
- Ajout d'un service singleton `AnnouncementBanner` pour gérer les bannières de maintenance. [#1506](https://github.com/etalab/data_pass/pull/1506)
- Amélioration de la gestion des webhooks. [#1500](https://github.com/etalab/data_pass/pull/1500)

### Autres changements

- Mise à jour de la documentation des rôles. [#1507](https://github.com/etalab/data_pass/pull/1507)
- Correction de fautes de frappe dans les sujets des emails. [#1537](https://github.com/etalab/data_pass/pull/1537)
- Ajout d'instructions pour l'exécution de `make build` en cas de dépendances manquantes. [#1525](https://github.com/etalab/data_pass/pull/1525)
- Clarification des messages d'erreur de `SkipLinksImplementedChecker`. [#1524](https://github.com/etalab/data_pass/pull/1524)
- Ajout d'un checker pour forcer la définition du titre sur chaque vue. [#1523](https://github.com/etalab/data_pass/pull/1523)
- Mise à jour du fichier CLAUDE.md. [#1522](https://github.com/etalab/data_pass/pull/1522)
- Correction d'un problème de timezone en CI. [#1517](https://github.com/etalab/data_pass/pull/1517)
- Suppression de scopes inutiles pour l'API entreprise-entrouvert. [#1482](https://github.com/etalab/data_pass/pull/1482)
