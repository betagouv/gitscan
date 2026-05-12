## Changelog : data_pass (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une recherche d'utilisateurs dans la gestion des droits, et l'amélioration des performances. Des corrections de bugs et des mises à jour de sécurité ont également été apportées. L'API s'enrichit de nouvelles fonctionnalités, notamment pour la gestion des demandes et l'exposition de données supplémentaires.

### Évolutions fonctionnelles
- Ajout d'une recherche d'utilisateurs dans la gestion des droits [#1544](https://github.com/etalab/data_pass/pull/1544).
- Amélioration de l'interface de gestion des droits utilisateur avec l'ajout de l'interface et des règles métier correspondantes [#1521](https://github.com/etalab/data_pass/pull/1521).
- Ajout de la possibilité de bannir un utilisateur [#1508](https://github.com/etalab/data_pass/pull/1508).
- Amélioration de l'affichage du statut des demandes (revendiqué/non revendiqué) [#1539](https://github.com/etalab/data_pass/pull/1539).
- Suppression du compteur de longlet "Demandes" pour les instructeurs [#1538](https://github.com/etalab/data_pass/pull/1538).
- Amélioration de l'affichage des erreurs de validation d'email lors de la soumission [#1505](https://github.com/etalab/data_pass/pull/1505).
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API v1 [#1523](https://github.com/etalab/data_pass/pull/1523).
- Ajout d'une bannière de maintenance ProConnect sur toutes les pages.
- Amélioration de l'affichage des URLs cliquables dans les emails.
- Mise à jour des libellés de la tarification Eaje.

### Évolutions techniques
- Mise à jour de la version de View Component en 4.x [#1559](https://github.com/etalab/data_pass/pull/1559).
- Amélioration de la gestion des tests Cucumber pour éviter les faux échecs [#1562](https://github.com/etalab/data_pass/pull/1562).
- Ajout d'un script `bin/test-parallel` pour lancer les tests en parallèle en local [#1560](https://github.com/etalab/data_pass/pull/1560).
- Optimisation de la configuration CI/CD pour réduire le temps d'exécution des tests [#1503](https://github.com/etalab/data_pass/pull/1503).
- Mise à jour de Rails Pulse en 0.3.1 [#1553](https://github.com/etalab/data_pass/pull/1553).
- Refactorisation de la gestion des rôles avec l'introduction de `RoleHierarchy` et `RoleSet`.
- Ajout de gestion des diffs des changelogs.
- Correction d'une régression suite à une mise à jour précédente.
- Amélioration de la gestion des erreurs et des exceptions dans l'API.
- Ajout de webhooks pour les événements liés aux organisations.
- Amélioration de la documentation de l'API.
- Correction de N+1 queries sur le dashboard demandeur [#1499](https://github.com/etalab/data_pass/pull/1499).
- Ajout de tests contractuels.

### Autres changements
- Réorganisation de la documentation dans des sous-dossiers (technique, métier, api_particulier) [#1549](https://github.com/etalab/data_pass/pull/1549).
- Ajout de la documentation du système HabilitationType dynamique [#1548](https://github.com/etalab/data_pass/pull/1548).
- Mise à jour des informations des groupes de services CISIRH [#1546](https://github.com/etalab/data_pass/pull/1546), [#1545](https://github.com/etalab/data_pass/pull/1545), [#1543](https://github.com/etalab/data_pass/pull/1543).
- Diverses mises à jour de dépendances.
- Ajout d'un guide de style pour les commits (CLAUDE).
- Ajout d'instructions pour l'utilisation de `make build`.
- Amélioration de la lisibilité du code et correction de typos.
