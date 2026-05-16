## Changelog : data_pass (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une recherche d'utilisateurs dans la gestion des droits, la gestion des utilisateurs bannis et l'amélioration des messages d'erreur. Des efforts ont également été faits pour optimiser les performances et la robustesse de l'application, ainsi que pour améliorer la documentation et les tests. L'API s'enrichit de nouvelles fonctionnalités d'écriture.

### Évolutions fonctionnelles
- Ajout d'une recherche d'utilisateurs dans la gestion des droits [#1544](https://github.com/etalab/data_pass/pull/1544).
- Implémentation d'une fonctionnalité de bannissement d'utilisateurs, avec interface d'administration associée [#1508](https://github.com/etalab/data_pass/pull/1508).
- Amélioration de l'affichage du statut des demandes (revendiqué/non revendiqué) [#1539](https://github.com/etalab/data_pass/pull/1539).
- Suppression du compteur de longlet "Demandes" pour les instructeurs [#1538](https://github.com/etalab/data_pass/pull/1538).
- Ajout d'une bannière de maintenance ProConnect visible sur toutes les pages [#1508](https://github.com/etalab/data_pass/pull/1508).
- Amélioration des messages d'erreur, notamment lors de la soumission de formulaires [#1511](https://github.com/etalab/data_pass/pull/1511) et en cas de problème de connexion [#1531](https://github.com/etalab/data_pass/pull/1531).
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API v1 [#1523](https://github.com/etalab/data_pass/pull/1523).
- Ajout d'une recherche d'utilisateurs sur la gestion des droits [#1544](https://github.com/etalab/data_pass/pull/1544).
- Ajout de nouveaux scopes OAuth2 pour les demandes [#1484](https://github.com/etalab/data_pass/pull/1484).
- Ajout d'une gestion des événements historiques pour les mises à jour [#1553](https://github.com/etalab/data_pass/pull/1553).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `view_component`, `css_parser`, `rubocop`, `erb`, `zlib`, `openapi_first`, `bullet` et autres.
- Amélioration de la suite de tests : ajout de tests Cucumber pour la gestion des droits, correction de tests flaky, parallélisation des tests pour réduire le temps d'exécution [#1533](https://github.com/etalab/data_pass/pull/1533).
- Refactoring de la gestion des rôles avec l'introduction de `RoleHierarchy` et `RoleSet`.
- Amélioration de la gestion des diffs et des changelogs.
- Mise en place d'un système de webhook pour les mises à jour de l'INSEE des organisations [#1512](https://github.com/etalab/data_pass/pull/1512).
- Amélioration de la gestion des erreurs et des exceptions.
- Migration vers rails_pulse 0.3.0 et 0.3.1.
- Ajout de la possibilité d'utiliser des paramètres forts pour les tableaux dynamiques.
- Amélioration de la gestion des erreurs lors de la soumission de formulaires.
- Ajout d'une gestion des événements pour les actions des administrateurs.
- Implémentation d'une API d'écriture (POST et PATCH) pour les demandes [#1504](https://github.com/etalab/data_pass/pull/1504).

### Autres changements
- Réorganisation de la documentation dans des sous-dossiers (technique, métier, API particulier) [#1549](https://github.com/etalab/data_pass/pull/1549).
- Ajout de documentation pour le système HabilitationType dynamique [#1548](https://github.com/etalab/data_pass/pull/1548).
- Mise à jour des informations des services CISIRH [#1546](https://github.com/etalab/data_pass/pull/1546) et [#1543](https://github.com/etalab/data_pass/pull/1543).
- Ajout d'un guide de style pour les commits (CLAUDE) [#1511](https://github.com/etalab/data_pass/pull/1511).
- Amélioration de la lisibilité du code avec Rubocop.
- Correction de typos et amélioration de la qualité des textes.
