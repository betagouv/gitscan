## Changelog : data_pass (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur pour les administrateurs, notamment avec la gestion des rôles et des droits, ainsi que sur l'ajout de nouvelles fonctionnalités pour l'API et la gestion des documents. Des corrections et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Gestion des droits :** Ajout d'une interface pour gérer les droits utilisateur, incluant la recherche d'utilisateurs et la gestion des rôles ([#1567](https://github.com/etalab/data_pass/issues/1567), [#1559](https://github.com/etalab/data_pass/issues/1559), [#1544](https://github.com/etalab/data_pass/issues/1544), [#1521](https://github.com/etalab/data_pass/issues/1521)).
- **API :** Ajout d'endpoints POST et PATCH pour la création et la mise à jour de demandes via l'API ([#1504](https://github.com/etalab/data_pass/issues/1504)). Exposition du numéro de téléphone de l'applicant dans l'API v1 ([#1523](https://github.com/etalab/data_pass/issues/1523)).
- **Gestion des documents :** Limitation du nombre de fichiers uploadés à 6 par champ document ([#1554](https://github.com/etalab/data_pass/issues/1554)).
- **Authentification :** Possibilité de contourner l'étape de connexion en environnement hors production pour faciliter le développement et les tests ([#1565](https://github.com/etalab/data_pass/issues/1565)).
- **Interface utilisateur :** Ajout d'un bouton "Précédent" manquant dans l'étape de traitement des données personnelles ([#1542](https://github.com/etalab/data_pass/issues/1542)). Suppression du compteur de longlet "Demandes" pour les instructeurs ([#1538](https://github.com/etalab/data_pass/issues/1538)).
- **Informations services CISIRH :** Mise à jour et ajout d'informations concernant les services CISIRH ([#1546](https://github.com/etalab/data_pass/issues/1546), [#1543](https://github.com/etalab/data_pass/issues/1543)).

### Évolutions techniques
- **Tests :** Correction de tests Cucumber instables causés par des fuites de Capybara.app_host ([#1562](https://github.com/etalab/data_pass/issues/1562)). Ajout d'un wrapper pour lancer la suite de tests en parallèle en local ([#1562](https://github.com/etalab/data_pass/issues/1562)).
- **Dépendances :** Mise à jour de plusieurs dépendances (view_component, rubocop, css_parser, etc.).
- **Rails Pulse :** Mise à jour et migration vers la dernière version de rails_pulse ([#1567](https://github.com/etalab/data_pass/issues/1567)).
- **Refactoring :** Refactorisation de l'alerte et simplification du code.
- **Changelogs :** Isole la gestion des diffs des changelogs et ajoute la raison privée pour les admins.
- **API :** Amélioration des descriptions OpenAPI.

### Autres changements
- **Documentation :** Réorganisation du dossier `docs/` et ajout de documentation sur le système HabilitationType dynamique ([#1549](https://github.com/etalab/data_pass/issues/1549), [#1548](https://github.com/etalab/data_pass/issues/1548)).
- **Sécurité :** Correction d'un problème bloquant l'authentification sur un SIRET invalide ([#1553](https://github.com/etalab/data_pass/issues/1553)).
- **Améliorations diverses :** Ajout de tutoriels, amélioration des messages d'erreur et correction de problèmes mineurs.
